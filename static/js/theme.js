// ========================================
// GERENCIADOR DE TEMA (CLARO/ESCURO)
// ========================================

// Inicializar tema quando a página carregar
document.addEventListener('DOMContentLoaded', initTheme);

function initTheme() {
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.querySelector('.theme-icon');
    
    if (!themeToggle) {
        console.warn('Botão de tema não encontrado');
        return;
    }
    
    // Carregar tema salvo no localStorage
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);
    
    // Adicionar evento ao botão
    themeToggle.addEventListener('click', toggleTheme);
}

function toggleTheme() {
    const currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    applyTheme(newTheme);
    localStorage.setItem('theme', newTheme);
}

function applyTheme(theme) {
    const themeIcon = document.querySelector('.theme-icon');
    
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
        if (themeIcon) themeIcon.textContent = '☀️';
    } else {
        document.body.classList.remove('dark-mode');
        if (themeIcon) themeIcon.textContent = '🌙';
    }
}
