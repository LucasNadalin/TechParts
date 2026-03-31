# TechParts - Loja de Informática com Peças Usadas e Recondicionadas

Uma aplicação web moderna construída com **Python Flask** para uma loja de informática especializada em peças usadas e recondicionadas. A aplicação inclui um **assistente de IA integrado com a API do Gemini** para responder perguntas sobre especificações técnicas e preços.

## 🎯 Funcionalidades

- **Catálogo Completo**: Mais de 30 peças de informática em 10 categorias diferentes
- **Filtros Avançados**: Filtrar por categoria, condição da peça (nova, quase nova, usada, recondicionada) e busca por nome
- **Cálculo de Preços Dinâmico**: Preços ajustados automaticamente conforme a condição da peça
- **Assistente de IA**: Chat integrado com Google Gemini para responder perguntas sobre peças, especificações e preços
- **Design Responsivo**: Interface moderna e otimizada para desktop, tablet e mobile
- **API RESTful**: Endpoints bem documentados para integração com outras aplicações

## 📋 Categorias de Peças

- Placa-Mãe
- Memória RAM
- Processador (CPU)
- Placa de Vídeo (GPU)
- SSD
- HD (Disco Rígido)
- Fonte de Alimentação
- Cooler
- Gabinete
- Monitor

## 🔧 Condições de Peças

| Condição | Preço | Descrição |
|----------|-------|-----------|
| Nova | 100% | Peça nova, nunca usada |
| Quase Nova | 85% | Peça em excelente estado |
| Usada | 70% | Peça em bom estado de funcionamento |
| Recondicionada | 75% | Peça restaurada e testada |

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Chave da API do Google Gemini (opcional, para usar o assistente de IA)

### Passos de Instalação

1. **Clone ou navegue até o diretório do projeto**:
   ```bash
   cd /home/ubuntu/techparts-store
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente** (opcional):
   
   Crie um arquivo `.env` na raiz do projeto:
   ```
   FLASK_ENV=development
   FLASK_DEBUG=True
   SECRET_KEY=sua-chave-secreta-aqui
   GEMINI_API_KEY=sua-chave-da-api-gemini-aqui
   ```

4. **Inicie a aplicação**:
   ```bash
   python app.py
   ```

5. **Acesse a aplicação**:
   
   Abra seu navegador e acesse: `http://localhost:5000`

## 🤖 Configurando o Assistente de IA (Gemini)

Para ativar o assistente de IA com a API do Google Gemini:

1. **Obtenha sua chave da API**:
   - Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Crie uma nova chave de API

2. **Configure a chave**:
   - Defina a variável de ambiente `GEMINI_API_KEY` com sua chave
   - Ou edite o arquivo `.env` e adicione: `GEMINI_API_KEY=sua-chave-aqui`

3. **Reinicie a aplicação**:
   ```bash
   python app.py
   ```

## 📁 Estrutura do Projeto

```
techparts-store/
├── app.py                    # Aplicação principal Flask
├── catalog.py               # Catálogo de produtos e configurações
├── ai_assistant.py          # Módulo do assistente de IA
├── config.py                # Configurações da aplicação
├── requirements.txt         # Dependências Python
├── templates/
│   ├── index.html          # Página principal
│   ├── 404.html            # Página de erro 404
│   └── 500.html            # Página de erro 500
└── static/
    ├── css/
    │   └── style.css       # Estilos CSS
    └── js/
        └── main.js         # JavaScript frontend
```

## 🔌 API Endpoints

### Produtos

- **GET** `/api/products` - Obter lista de produtos com filtros
  - Query Parameters:
    - `category`: ID da categoria (ex: `placa-mae`)
    - `condition`: Condição da peça (ex: `usada`)
    - `search`: Termo de busca

- **GET** `/api/product/<product_id>` - Obter detalhes de um produto específico
  - Query Parameters:
    - `condition`: Condição da peça para calcular preço

### Categorias e Condições

- **GET** `/api/categories` - Obter todas as categorias disponíveis
- **GET** `/api/conditions` - Obter todas as condições disponíveis

### Chat com IA

- **POST** `/api/chat` - Enviar mensagem para o assistente de IA
  - Body (JSON):
    ```json
    {
      "message": "Qual é a melhor placa-mãe para Ryzen 5000?"
    }
    ```

## 💻 Exemplos de Uso

### Buscar produtos por categoria

```bash
curl "http://localhost:5000/api/products?category=gpu"
```

### Buscar produtos em condição específica

```bash
curl "http://localhost:5000/api/products?condition=recondicionada"
```

### Buscar produtos por nome

```bash
curl "http://localhost:5000/api/products?search=RTX"
```

### Conversar com o assistente de IA

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Qual é a diferença entre DDR4 e DDR5?"}'
```

## 🎨 Design

A aplicação utiliza um **design minimalista moderno** com:

- Paleta de cores profissional (azul escuro, branco, cinza)
- Tipografia clara e hierárquica (Poppins para títulos, Roboto para corpo)
- Layout responsivo que se adapta a qualquer tamanho de tela
- Transições suaves e animações discretas
- Foco em usabilidade e clareza de informação

## 🔒 Segurança

- Proteção contra CSRF
- Validação de entrada em todos os endpoints
- Sanitização de HTML para prevenir XSS
- CORS configurado para aceitar requisições do frontend

## 📝 Dados de Exemplo

A aplicação vem com um catálogo pré-populado com mais de 30 peças reais, incluindo:

- Placas-mãe: ASUS ROG STRIX, MSI MPG, Gigabyte
- CPUs: AMD Ryzen, Intel Core
- GPUs: NVIDIA RTX, AMD Radeon
- Memória: Corsair, Kingston, Crucial
- Armazenamento: Samsung, WD, Kingston
- E muito mais!

## 🐛 Troubleshooting

### A aplicação não inicia

- Verifique se Python 3.8+ está instalado: `python --version`
- Instale as dependências novamente: `pip install -r requirements.txt`
- Verifique se a porta 5000 está disponível

### O assistente de IA não funciona

- Verifique se a chave da API Gemini está configurada corretamente
- Verifique a conexão com a internet
- Consulte os logs da aplicação para mensagens de erro

### Produtos não aparecem

- Verifique se o arquivo `catalog.py` está intacto
- Reinicie a aplicação
- Limpe o cache do navegador (Ctrl+Shift+Delete)

## 📞 Suporte

Para reportar bugs ou sugerir melhorias, entre em contato ou abra uma issue no repositório.

## 📄 Licença

Este projeto é fornecido como está, sem garantias. Use livremente para fins pessoais ou comerciais.

## 🙏 Agradecimentos

- Google Gemini API para o assistente de IA
- Flask framework para a aplicação web
- Google Fonts para as fontes tipográficas

---

**Desenvolvido com ❤️ para entusiastas de informática**
