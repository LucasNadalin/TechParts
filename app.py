"""
Aplicação Flask para loja de informática com peças usadas e recondicionadas
Integrada com API do Gemini para assistente de IA
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from catalog import PRODUCTS, CATEGORIES, CONDITIONS
from ai_assistant import AIAssistant

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configurações
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY', '')

# Inicializar assistente de IA
ai_assistant = AIAssistant(api_key=app.config['GEMINI_API_KEY'])

# ==================== ROTAS PRINCIPAIS ====================

@app.route('/')
def index():
    """Página principal da loja"""
    return render_template('index.html', 
                         categories=CATEGORIES,
                         conditions=CONDITIONS)

@app.route('/api/products', methods=['GET'])
def get_products():
    """API para obter produtos com filtros"""
    category = request.args.get('category', None)
    condition = request.args.get('condition', None)
    search = request.args.get('search', '').lower()
    
    # Filtrar produtos
    filtered_products = PRODUCTS
    
    if category and category != 'todos':
        filtered_products = [p for p in filtered_products if p['category'] == category]
    
    if search:
        filtered_products = [p for p in filtered_products 
                           if search in p['name'].lower() or 
                              search in p['description'].lower()]
    
    # Calcular preços com base na condição
    result = []
    for product in filtered_products:
        product_data = product.copy()
        
        # Se uma condição foi especificada, calcular o preço
        if condition and condition in CONDITIONS:
            multiplier = CONDITIONS[condition]['price_multiplier']
            product_data['price'] = round(product['base_price'] * multiplier, 2)
            product_data['condition'] = condition
        else:
            # Mostrar preço base se nenhuma condição foi selecionada
            product_data['price'] = product['base_price']
            product_data['condition'] = 'nova'
        
        result.append(product_data)
    
    return jsonify({
        'success': True,
        'products': result,
        'total': len(result)
    })

@app.route('/api/product/<product_id>', methods=['GET'])
def get_product_detail(product_id):
    """API para obter detalhes de um produto específico"""
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    
    if not product:
        return jsonify({'success': False, 'error': 'Produto não encontrado'}), 404
    
    condition = request.args.get('condition', 'nova')
    
    product_data = product.copy()
    if condition in CONDITIONS:
        multiplier = CONDITIONS[condition]['price_multiplier']
        product_data['price'] = round(product['base_price'] * multiplier, 2)
        product_data['condition'] = condition
        product_data['condition_label'] = CONDITIONS[condition]['label']
    
    return jsonify({
        'success': True,
        'product': product_data
    })

@app.route('/api/chat', methods=['POST'])
def chat_with_ai():
    """API para conversar com o assistente de IA"""
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'success': False, 'error': 'Mensagem vazia'}), 400
    
    if not app.config['GEMINI_API_KEY']:
        return jsonify({
            'success': False, 
            'error': 'Chave da API Gemini não configurada'
        }), 500
    
    try:
        # Obter resposta do assistente de IA
        response = ai_assistant.chat(user_message, PRODUCTS, CATEGORIES, CONDITIONS)
        
        return jsonify({
            'success': True,
            'response': response
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro ao processar mensagem: {str(e)}'
        }), 500

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """API para obter categorias disponíveis"""
    return jsonify({
        'success': True,
        'categories': CATEGORIES
    })

@app.route('/api/conditions', methods=['GET'])
def get_conditions():
    """API para obter condições disponíveis"""
    conditions_data = {k: v['label'] for k, v in CONDITIONS.items()}
    return jsonify({
        'success': True,
        'conditions': conditions_data
    })

# ==================== TRATAMENTO DE ERROS ====================

@app.errorhandler(404)
def not_found(error):
    """Página 404"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Página 500"""
    return render_template('500.html'), 500

# ==================== INICIALIZAÇÃO ====================

if __name__ == '__main__':
    # Verificar se a chave da API foi configurada
    if not app.config['GEMINI_API_KEY']:
        print("⚠️  AVISO: GEMINI_API_KEY não foi configurada!")
        print("   A funcionalidade de IA não funcionará sem a chave da API.")
        print("   Configure a variável de ambiente GEMINI_API_KEY para ativar.")
    
    print("🚀 Iniciando TechParts Store...")
    print(f"📍 Acesse em http://localhost:5000")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response