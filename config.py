import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações padrão da aplicação"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('FLASK_DEBUG', False)
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    
    # Configurações de CORS
    CORS_HEADERS = 'Content-Type'
