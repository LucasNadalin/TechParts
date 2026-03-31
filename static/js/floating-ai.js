// ========================================
// ASSISTENTE DE IA FLUTUANTE - VERSÃO SIMPLES
// ========================================

// Criar modal dinamicamente
function createAIChatModal() {
    const modal = document.createElement('div');
    modal.id = 'aiChatModal';
    modal.className = 'ai-chat-modal';
    modal.innerHTML = `
        <div class="ai-chat-header">
            <h3>Assistente de IA</h3>
            <button id="closeAiChat" class="close-ai-chat">&times;</button>
        </div>
        <div id="aiChatMessages" class="ai-chat-messages">
            <div class="message bot-message">
                <p>Olá! 👋 Sou seu assistente de IA. Posso ajudá-lo com informações sobre nossas peças, especificações técnicas e preços. O que você gostaria de saber?</p>
            </div>
        </div>
        <div class="ai-chat-input-container">
            <input 
                type="text" 
                id="aiChatInput" 
                placeholder="Digite sua pergunta..." 
                class="ai-chat-input"
            >
            <button id="aiSendBtn" class="btn btn-primary btn-small">Enviar</button>
        </div>
    `;
    document.body.appendChild(modal);
    return modal;
}

// Criar botão flutuante dinamicamente
function createFloatingButton() {
    const btn = document.createElement('button');
    btn.id = 'aiFloatingBtn';
    btn.className = 'ai-floating-btn';
    btn.title = 'Abrir Assistente de IA';
    btn.innerHTML = '<span class="ai-icon">🤖</span>';
    document.body.appendChild(btn);
    return btn;
}

// Inicializar quando a página carregar
window.addEventListener('load', function() {
    console.log('Inicializando chat flutuante...');
    
    // Criar elementos
    const floatingBtn = createFloatingButton();
    const chatModal = createAIChatModal();
    
    console.log('Elementos criados:', { floatingBtn, chatModal });
    
    // Elementos do modal
    const closeBtn = document.getElementById('closeAiChat');
    const sendBtn = document.getElementById('aiSendBtn');
    const input = document.getElementById('aiChatInput');
    const messagesDiv = document.getElementById('aiChatMessages');
    
    // Clique no botão flutuante
    floatingBtn.addEventListener('click', function() {
        console.log('Botão clicado');
        chatModal.classList.toggle('show');
        if (chatModal.classList.contains('show')) {
            input.focus();
        }
    });
    
    // Fechar modal
    closeBtn.addEventListener('click', function() {
        console.log('Fechando modal');
        chatModal.classList.remove('show');
    });
    
    // Enviar mensagem
    sendBtn.addEventListener('click', enviarMensagem);
    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            enviarMensagem();
        }
    });
    
    // Função para enviar mensagem
    function enviarMensagem() {
        const mensagem = input.value.trim();
        if (!mensagem) return;
        
        console.log('Enviando:', mensagem);
        
        // Adicionar mensagem do usuário
        const userMsg = document.createElement('div');
        userMsg.className = 'message user-message';
        userMsg.innerHTML = `<p>${escapeHtml(mensagem)}</p>`;
        messagesDiv.appendChild(userMsg);
        
        input.value = '';
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        
        // Mostrar digitando
        const typing = document.createElement('div');
        typing.className = 'message bot-message';
        typing.innerHTML = '<p>Digitando...</p>';
        typing.id = 'typing-msg';
        messagesDiv.appendChild(typing);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        
        // Enviar para API
        fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: mensagem })
        })
        .then(r => r.json())
        .then(data => {
            console.log('Resposta:', data);
            
            // Remover digitando
            const typing = document.getElementById('typing-msg');
            if (typing) typing.remove();
            
            if (data.success) {
                // Adicionar resposta
                const botMsg = document.createElement('div');
                botMsg.className = 'message bot-message';
                botMsg.innerHTML = `<p>${escapeHtml(data.response)}</p>`;
                messagesDiv.appendChild(botMsg);
                
                // Ler resposta em voz alta
                lerEmVozAlta(data.response);
            } else {
                const errorMsg = document.createElement('div');
                errorMsg.className = 'message bot-message';
                errorMsg.innerHTML = '<p>Erro ao processar mensagem</p>';
                messagesDiv.appendChild(errorMsg);
            }
            
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        })
        .catch(err => {
            console.error('Erro:', err);
            const typing = document.getElementById('typing-msg');
            if (typing) typing.remove();
            
            const errorMsg = document.createElement('div');
            errorMsg.className = 'message bot-message';
            errorMsg.innerHTML = '<p>Erro ao conectar</p>';
            messagesDiv.appendChild(errorMsg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        });
    }
    
    console.log('Chat flutuante inicializado com sucesso!');
});

// Função para ler texto em voz alta
function lerEmVozAlta(texto) {
    // Verificar se o navegador suporta
    if (!('speechSynthesis' in window)) {
        console.log('Navegador não suporta síntese de fala');
        return;
    }
    
    // Cancelar fala anterior se houver
    speechSynthesis.cancel();
    
    // Criar utterance
    const utterance = new SpeechSynthesisUtterance(texto);
    utterance.lang = 'pt-BR';
    utterance.rate = 1;
    utterance.pitch = 1;
    utterance.volume = 1;
    
    // Falar
    speechSynthesis.speak(utterance);
}

// Função para escapar HTML
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}
