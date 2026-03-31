// ========================================
// CONFIGURAÇÃO E ESTADO GLOBAL
// ========================================

const API_BASE = '/api';
let currentProducts = [];
let currentFilters = {
    category: 'todos',
    condition: '',
    search: ''
};

// Ícones para categorias
const categoryIcons = {
    'placa-mae': '🖥️',
    'memoria-ram': '💾',
    'cpu': '⚙️',
    'gpu': '🎮',
    'ssd': '📦',
    'hd': '💿',
    'fonte': '🔌',
    'cooler': '❄️',
    'case': '📦',
    'monitor': '📺'
};

// ========================================
// INICIALIZAÇÃO
// ========================================

document.addEventListener('DOMContentLoaded', () => {
    initializeEventListeners();
    loadProducts();
});

// ========================================
// EVENT LISTENERS
// ========================================

function initializeEventListeners() {
    // Filtros
    document.getElementById('categoryFilter').addEventListener('change', (e) => {
        currentFilters.category = e.target.value;
        loadProducts();
    });

    document.getElementById('conditionFilter').addEventListener('change', (e) => {
        currentFilters.condition = e.target.value;
        loadProducts();
    });

    document.getElementById('searchInput').addEventListener('input', (e) => {
        currentFilters.search = e.target.value;
        loadProducts();
    });

    document.getElementById('resetFilters').addEventListener('click', () => {
        currentFilters = {
            category: 'todos',
            condition: '',
            search: ''
        };
        document.getElementById('categoryFilter').value = 'todos';
        document.getElementById('conditionFilter').value = '';
        document.getElementById('searchInput').value = '';
        loadProducts();
    });

    // Modal
    document.querySelector('.close-modal').addEventListener('click', closeModal);
    document.getElementById('productModal').addEventListener('click', (e) => {
        if (e.target.id === 'productModal') {
            closeModal();
        }
    });

    // Menu mobile
    const navbarToggle = document.getElementById('navbarToggle');
if (navbarToggle) {
    navbarToggle.addEventListener('click', toggleMobileMenu);
}
}

// ========================================
// CARREGAMENTO DE PRODUTOS
// ========================================

async function loadProducts() {
    const productsGrid = document.getElementById('productsGrid');
    productsGrid.innerHTML = '<div class="loading">Carregando produtos...</div>';

    try {
        const params = new URLSearchParams();
        
        if (currentFilters.category !== 'todos') {
            params.append('category', currentFilters.category);
        }
        
        if (currentFilters.condition) {
            params.append('condition', currentFilters.condition);
        }
        
        if (currentFilters.search) {
            params.append('search', currentFilters.search);
        }

        const response = await fetch(`${API_BASE}/products?${params}`);
        const data = await response.json();

        if (data.success) {
            currentProducts = data.products;
            renderProducts(currentProducts);
        } else {
            productsGrid.innerHTML = '<div class="no-products">Erro ao carregar produtos</div>';
        }
    } catch (error) {
        console.error('Erro ao carregar produtos:', error);
        productsGrid.innerHTML = '<div class="no-products">Erro ao carregar produtos</div>';
    }
}

// ========================================
// RENDERIZAÇÃO DE PRODUTOS
// ========================================

function renderProducts(products) {
    const productsGrid = document.getElementById('productsGrid');

    if (products.length === 0) {
        productsGrid.innerHTML = '<div class="no-products">Nenhum produto encontrado</div>';
        return;
    }

    productsGrid.innerHTML = products.map(product => `
        <div class="product-card" onclick="openProductModal('${product.id}')">
            <div class="product-header">
                ${product.image ? 
                    `<img src="/static/images/${product.image}" alt="${product.name}" style="width: 100%; height: 300px; object-fit: cover; border-radius: 8px;">` 
                    : `<span class="product-icon">${categoryIcons[product.category] || '📦'}</span>`
                }
            </div>
            <div class="product-body">
                <div class="product-category">${product.category}</div>
                <h3 class="product-name">${product.name}</h3>
                <p class="product-description">${product.description}</p>
            </div>
            <div class="product-footer">
                <div class="product-price">R$ ${product.price.toFixed(2)}</div>
                <div class="product-condition">${getConditionLabel(product.condition)}</div>
            </div>
        </div>
    `).join('');
}

function getConditionLabel(condition) {
    const labels = {
        'nova': 'Nova',
        'quase-nova': 'Quase Nova',
        'usada': 'Usada',
        'recondicionada': 'Recondicionada'
    };
    return labels[condition] || condition;
}

// ========================================
// MODAL DE DETALHES DO PRODUTO
// ========================================

async function openProductModal(productId) {
    const modal = document.getElementById('productModal');
    const modalBody = document.getElementById('modalBody');

    try {
        const condition = document.getElementById('conditionFilter').value || 'nova';
        const response = await fetch(`${API_BASE}/product/${productId}?condition=${condition}`);
        const data = await response.json();

        if (data.success) {
            const product = data.product;
            modalBody.innerHTML = `
                <div class="product-detail">
                    ${product.image ? 
                        `<img src="/static/images/${product.image}" alt="${product.name}" style="width: 100%; height: 300px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;">` 
                        : ''
                    }
                    <h2>${product.name}</h2>
                    <p><strong>Categoria:</strong> ${product.category}</p>
                    <p><strong>Descrição:</strong> ${product.description}</p>
                    
                    <div style="display: flex; gap: 1rem; align-items: center;">
                        <div>
                            <h3 style="color: var(--primary-color); margin: 0;">R$ ${product.price.toFixed(2)}</h3>
                            <p style="margin: 0.5rem 0 0 0; color: var(--text-light);">Condição: ${getConditionLabel(product.condition)}</p>
                        </div>
                    </div>
                    
                    ${product.specs ? `
                        <div>
                            <h3 style="margin-top: 1.5rem;">Especificacoes</h3>
                            <div class="specs-grid">
                                ${Object.entries(product.specs).map(([key, value]) => `
                                    <div class="spec-item">
                                        <div class="spec-label">${formatSpecLabel(key)}</div>
                                        <div class="spec-value">${value}</div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    ` : ''}
                    
                    <button class="btn btn-primary" style="width: 100%; margin-top: 1.5rem;" onclick="addToCart('${product.id}', '${product.name}', ${product.price}, '${product.condition}')">
                        Adicionar ao Carrinho
                    </button>
                </div>
            `;
            modal.classList.add('show');
        }
    } catch (error) {
        console.error('Erro ao carregar detalhes do produto:', error);
        modalBody.innerHTML = '<p>Erro ao carregar detalhes do produto</p>';
        modal.classList.add('show');
    }
}

function closeModal() {
    document.getElementById('productModal').classList.remove('show');
}

function formatSpecLabel(label) {
    return label
        .replace(/_/g, ' ')
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

// ========================================
// MENU MOBILE
// ========================================

function toggleMobileMenu() {
    const navbarMenu = document.getElementById('navbarMenu');
    navbarMenu.classList.toggle('active');
}

// Fechar menu ao clicar em um link
document.addEventListener('click', (e) => {
    if (e.target.tagName === 'A' && e.target.parentElement.id === 'navbarMenu') {
        document.getElementById('navbarMenu').classList.remove('active');
    }
});
