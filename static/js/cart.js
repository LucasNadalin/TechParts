// ========================================
// GERENCIAMENTO DO CARRINHO DE COMPRAS
// ========================================

let cart = [];

// Carregar carrinho do localStorage
function loadCart() {
    const savedCart = localStorage.getItem('techparts-cart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
        updateCartUI();
    }
}

// Salvar carrinho no localStorage
function saveCart() {
    localStorage.setItem('techparts-cart', JSON.stringify(cart));
    updateCartUI();
}

// Adicionar item ao carrinho
function addToCart(productId, productName, price, condition) {
    const existingItem = cart.find(item => item.id === productId && item.condition === condition);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            id: productId,
            name: productName,
            price: price,
            condition: condition,
            quantity: 1
        });
    }
    
    saveCart();
    showCartNotification();
}

// Remover item do carrinho
function removeFromCart(productId, condition) {
    cart = cart.filter(item => !(item.id === productId && item.condition === condition));
    saveCart();
}

// Atualizar quantidade
function updateQuantity(productId, condition, quantity) {
    const item = cart.find(item => item.id === productId && item.condition === condition);
    if (item) {
        item.quantity = Math.max(1, quantity);
        saveCart();
    }
}

// Atualizar UI do carrinho
function updateCartUI() {
    const cartCount = document.getElementById('cartCount');
    const cartItems = document.getElementById('cartItems');
    const cartSummary = document.getElementById('cartSummary');
    
    // Atualizar contador
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    cartCount.textContent = totalItems;
    
    if (cart.length === 0) {
        cartItems.innerHTML = '<p class="empty-cart">Seu carrinho está vazio</p>';
        cartSummary.style.display = 'none';
    } else {
        // Renderizar itens
        cartItems.innerHTML = cart.map((item, index) => `
            <div class="cart-item">
                <div class="cart-item-info">
                    <div class="cart-item-name">${item.name}</div>
                    <div class="cart-item-condition">Condição: ${getConditionLabel(item.condition)}</div>
                    <div class="cart-item-price">R$ ${item.price.toFixed(2)}</div>
                </div>
                <div class="cart-item-quantity">
                    <button onclick="updateQuantity('${item.id}', '${item.condition}', ${item.quantity - 1})">-</button>
                    <span>${item.quantity}</span>
                    <button onclick="updateQuantity('${item.id}', '${item.condition}', ${item.quantity + 1})">+</button>
                </div>
                <button class="cart-item-remove" onclick="removeFromCart('${item.id}', '${item.condition}')">
                    Remover
                </button>
            </div>
        `).join('');
        
        // Calcular total
        const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        document.getElementById('cartTotal').textContent = `R$ ${total.toFixed(2)}`;
        cartSummary.style.display = 'block';
    }
}

// Mostrar notificação de item adicionado
function showCartNotification() {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 30px;
        background-color: var(--success-color);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 1000;
        animation: slideInUp 0.3s ease-in-out;
    `;
    notification.textContent = '✓ Adicionado ao carrinho!';
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutDown 0.3s ease-in-out';
        setTimeout(() => notification.remove(), 300);
    }, 2000);
}

// Abrir modal do carrinho
function openCartModal() {
    document.getElementById('cartModal').classList.add('show');
}

// Fechar modal do carrinho
function closeCartModal() {
    document.getElementById('cartModal').classList.remove('show');
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    loadCart();
    
    // Clique no ícone do carrinho
    document.getElementById('cartIcon').addEventListener('click', openCartModal);
    
    // Fechar modal ao clicar fora
    document.getElementById('cartModal').addEventListener('click', (e) => {
        if (e.target.id === 'cartModal') {
            closeCartModal();
        }
    });
});
