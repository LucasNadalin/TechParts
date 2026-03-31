"""
Assistente de IA integrado com Google Gemini
Fornece respostas sobre especificações de peças e preços
"""

import google.generativeai as genai
import json
from typing import List, Dict, Any

class AIAssistant:
    """Assistente de IA para consultas sobre peças de informática"""
    
    def __init__(self, api_key: str):
        """Inicializar o assistente com a chave da API Gemini 2.5 Flash"""
        self.api_key = api_key
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
        else:
            self.model = None
    
    def _format_catalog_context(self, products: List[Dict], 
                               categories: Dict, 
                               conditions: Dict) -> str:
        """Formatar o catálogo em um contexto para o modelo de IA"""
        
        context = "# Catálogo de Peças de Informática\n\n"
        
        # Adicionar categorias
        context += "## Categorias Disponíveis:\n"
        for cat_id, cat_name in categories.items():
            context += f"- {cat_name} ({cat_id})\n"
        
        context += "\n## Condições de Peças:\n"
        for cond_id, cond_info in conditions.items():
            multiplier = cond_info['price_multiplier']
            context += f"- {cond_info['label']} ({cond_id}): {multiplier*100:.0f}% do preço base\n"
        
        # Adicionar produtos
        context += "\n## Produtos Disponíveis:\n\n"
        for product in products:
            context += f"### {product['name']}\n"
            context += f"- ID: {product['id']}\n"
            context += f"- Categoria: {categories.get(product['category'], product['category'])}\n"
            context += f"- Preço Base: R$ {product['base_price']:.2f}\n"
            context += f"- Descrição: {product['description']}\n"
            
            if product.get('specs'):
                context += "- Especificações:\n"
                for spec_key, spec_value in product['specs'].items():
                    # Formatar nome da especificação
                    spec_name = spec_key.replace('_', ' ').title()
                    context += f"  - {spec_name}: {spec_value}\n"
            
            context += "\n"
        
        return context
    
    def chat(self, user_message: str, products: List[Dict], 
             categories: Dict, conditions: Dict) -> str:
        """
        Processar mensagem do usuário e retornar resposta da IA
        
        Args:
            user_message: Mensagem do usuário
            products: Lista de produtos do catálogo
            categories: Dicionário de categorias
            conditions: Dicionário de condições
            
        Returns:
            Resposta do assistente de IA
        """
        
        if not self.model:
            return "Desculpe, o assistente de IA não está configurado. Por favor, configure a chave da API Gemini."
        
        try:
            # Formatar contexto do catálogo
            catalog_context = self._format_catalog_context(products, categories, conditions)
            
            # Criar prompt do sistema
            system_prompt = f"""Você é um assistente de atendimento ao cliente para uma loja de informática 
especializada em peças usadas e recondicionadas. Você deve ajudar clientes a encontrar peças, 
entender especificações técnicas e informar sobre preços.

{catalog_context}

Instruções:
1. Responda em português brasileiro
2. Seja amigável e prestativo
3. Forneça informações precisas sobre as peças disponíveis
4. Quando perguntado sobre preços, lembre que o preço varia conforme a condição da peça
5. Se o cliente perguntar sobre uma peça que não existe, sugira alternativas similares
6. Sempre que possível, forneça especificações técnicas relevantes
7. Mantenha respostas concisas mas informativas (máximo 3-4 parágrafos)
"""
            
            # Gerar resposta
            response = self.model.generate_content(
                f"{system_prompt}\n\nCliente: {user_message}"
            )
            
            return response.text
            
        except Exception as e:
            return f"Desculpe, ocorreu um erro ao processar sua mensagem: {str(e)}"
    
    def search_products(self, query: str, products: List[Dict]) -> List[Dict]:
        """
        Buscar produtos usando IA para entender a intenção do usuário
        
        Args:
            query: Consulta do usuário
            products: Lista de produtos
            
        Returns:
            Lista de produtos relevantes
        """
        
        if not self.model:
            # Fallback para busca simples se IA não está disponível
            query_lower = query.lower()
            return [p for p in products 
                   if query_lower in p['name'].lower() or 
                      query_lower in p['description'].lower()]
        
        try:
            # Usar IA para entender a busca
            search_prompt = f"""Dado o seguinte catálogo de produtos:
{json.dumps([{'id': p['id'], 'name': p['name'], 'category': p['category']} for p in products], ensure_ascii=False)}

Qual(is) produto(s) seria(m) mais relevante(s) para a seguinte consulta: "{query}"?

Responda apenas com uma lista de IDs de produtos, separados por vírgula. Se nenhum for relevante, responda "nenhum".
"""
            
            response = self.model.generate_content(search_prompt)
            
            # Parsear resposta
            product_ids = [id.strip() for id in response.text.split(',') if id.strip()]
            
            return [p for p in products if p['id'] in product_ids]
            
        except Exception as e:
            print(f"Erro na busca com IA: {str(e)}")
            # Fallback para busca simples
            query_lower = query.lower()
            return [p for p in products 
                   if query_lower in p['name'].lower() or 
                      query_lower in p['description'].lower()]
