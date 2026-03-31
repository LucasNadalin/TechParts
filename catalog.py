"""Catálogo de peças de informática usadas e recondicionadas"""

CATEGORIES = {
    'placa-mae': 'Placa-Mãe',
    'memoria-ram': 'Memória RAM',
    'cpu': 'Processador (CPU)',
    'gpu': 'Placa de Vídeo (GPU)',
    'ssd': 'SSD',
    'hd': 'HD (Disco Rígido)',
    'fonte': 'Fonte de Alimentação',
    'cooler': 'Cooler',
    'case': 'Gabinete',
    'monitor': 'Monitor'
}

CONDITIONS = {
    'nova': {'label': 'Nova', 'price_multiplier': 1.0},
    'quase-nova': {'label': 'Quase Nova', 'price_multiplier': 0.85},
    'usada': {'label': 'Usada', 'price_multiplier': 0.70},
    'recondicionada': {'label': 'Recondicionada', 'price_multiplier': 0.75}
}

PRODUCTS = [
    # Placas-Mãe
    {
        'id': 'pm-001',
        'name': 'ASUS ROG STRIX B550-F',
        'category': 'placa-mae',
        'base_price': 850.00,
        'image': 'b550.png',
        'specs': {
            'socket': 'AM4',
            'chipset': 'B550',
            'memoria_max': '128GB',
            'slots_ram': '4',
            'slots_m2': '2',
            'features': 'WiFi 6, Bluetooth 5.2, RGB Aura Sync'
        },
        'description': 'Placa-mãe para processadores Ryzen série 3000 e 5000'
    },
    {
        'id': 'pm-002',
        'name': 'MSI MPG Z790 EDGE WIFI',
        'category': 'placa-mae',
        'base_price': 1200.00,
        'image': 'b550.png',
        'specs': {
            'socket': 'LGA1700',
            'chipset': 'Z790',
            'memoria_max': '192GB',
            'slots_ram': '4',
            'slots_m2': '4',
            'features': 'WiFi 6E, Thunderbolt 4, DDR5'
        },
        'description': 'Placa-mãe para processadores Intel série 12ª e 13ª geração'
    },
    {
        'id': 'pm-003',
        'name': 'Gigabyte B450M DS3H',
        'category': 'placa-mae',
        'base_price': 450.00,
        'image': 'b550.png',
        'specs': {
            'socket': 'AM4',
            'chipset': 'B450',
            'memoria_max': '64GB',
            'slots_ram': '2',
            'slots_m2': '1',
            'features': 'Micro ATX, Suporte Ryzen 5000'
        },
        'description': 'Placa-mãe compacta e econômica para Ryzen'
    },
    
    # Memória RAM
    {
        'id': 'ram-001',
        'name': 'Corsair Vengeance RGB Pro 16GB (2x8GB) DDR4 3200MHz',
        'category': 'memoria-ram',
        'base_price': 350.00,
        'image': 'ram.jpg',
        'specs': {
            'capacidade': '16GB',
            'tipo': 'DDR4',
            'velocidade': '3200MHz',
            'latencia': 'CAS 16',
            'modulos': '2x8GB',
            'features': 'RGB Sync, XMP Profile'
        },
        'description': 'Memória RAM de alto desempenho com iluminação RGB'
    },
    {
        'id': 'ram-002',
        'name': 'Kingston Fury Beast 32GB (2x16GB) DDR4 3200MHz',
        'category': 'memoria-ram',
        'base_price': 550.00,
        'image': 'ram.jpg',
        'specs': {
            'capacidade': '32GB',
            'tipo': 'DDR4',
            'velocidade': '3200MHz',
            'latencia': 'CAS 16',
            'modulos': '2x16GB',
            'features': 'HyperX Fury, Dissipador de calor'
        },
        'description': 'Memória RAM de alto desempenho para workstations'
    },
    {
        'id': 'ram-003',
        'name': 'Crucial Ballistix 8GB DDR4 2666MHz',
        'category': 'memoria-ram',
        'base_price': 180.00,
        'image': 'ram.jpg',
        'specs': {
            'capacidade': '8GB',
            'tipo': 'DDR4',
            'velocidade': '2666MHz',
            'latencia': 'CAS 16',
            'modulos': '1x8GB',
            'features': 'Compatível com maioria das placas'
        },
        'description': 'Memória RAM de entrada com bom custo-benefício'
    },
    
    # Processadores
    {
        'id': 'cpu-001',
        'name': 'AMD Ryzen 5 5600X',
        'category': 'cpu',
        'base_price': 1100.00,
        'image': 'processador.jpg',
        'specs': {
            'nucleos': '6',
            'threads': '12',
            'frequencia_base': '3.7 GHz',
            'frequencia_turbo': '4.6 GHz',
            'tdp': '65W',
            'cache': '32MB',
            'socket': 'AM4'
        },
        'description': 'Processador de alto desempenho para gaming e produção'
    },
    {
        'id': 'cpu-002',
        'name': 'Intel Core i7-12700K',
        'category': 'cpu',
        'base_price': 1800.00,
        'image': 'processador.jpg',
        'specs': {
            'nucleos': '12 (8P+4E)',
            'threads': '20',
            'frequencia_base': '3.6 GHz',
            'frequencia_turbo': '5.0 GHz',
            'tdp': '125W',
            'cache': '25MB',
            'socket': 'LGA1700'
        },
        'description': 'Processador topo de linha para gaming e workstations'
    },
    {
        'id': 'cpu-003',
        'name': 'AMD Ryzen 3 3100',
        'category': 'cpu',
        'base_price': 400.00,
        'image': 'processador.jpg',
        'specs': {
            'nucleos': '4',
            'threads': '8',
            'frequencia_base': '3.6 GHz',
            'frequencia_turbo': '3.9 GHz',
            'tdp': '65W',
            'cache': '16MB',
            'socket': 'AM4'
        },
        'description': 'Processador de entrada com bom desempenho'
    },
    
    # Placas de Vídeo
    {
        'id': 'gpu-001',
        'name': 'NVIDIA RTX 3080',
        'category': 'gpu',
        'base_price': 3500.00,
        'image': 'gpu.jpg',
        'specs': {
            'memoria': '10GB GDDR6X',
            'cuda_cores': '8704',
            'frequencia': '1.44 GHz',
            'power': '320W',
            'interface': 'PCI-E 4.0',
            'saidas': 'HDMI 2.1, 3x DisplayPort 1.4a'
        },
        'description': 'Placa de vídeo topo de linha para gaming 4K e IA'
    },
    {
        'id': 'gpu-002',
        'name': 'NVIDIA RTX 2060',
        'category': 'gpu',
        'base_price': 1200.00,
        'image': 'gpu.jpg',
        'specs': {
            'memoria': '6GB GDDR6',
            'cuda_cores': '1920',
            'frequencia': '1.365 GHz',
            'power': '160W',
            'interface': 'PCI-E 3.0',
            'saidas': 'HDMI 2.0b, 3x DisplayPort 1.4'
        },
        'description': 'Placa de vídeo de entrada para gaming 1080p/1440p'
    },
    {
        'id': 'gpu-003',
        'name': 'AMD Radeon RX 6700 XT',
        'category': 'gpu',
        'base_price': 1800.00,
        'image': 'gpu.jpg',
        'specs': {
            'memoria': '12GB GDDR6',
            'stream_processors': '2560',
            'frequencia': '2.105 GHz',
            'power': '230W',
            'interface': 'PCI-E 4.0',
            'saidas': 'HDMI 2.1, 2x DisplayPort 1.4'
        },
        'description': 'Placa de vídeo AMD para gaming 1440p/4K'
    },
    
    # SSDs
    {
        'id': 'ssd-001',
        'name': 'Samsung 970 EVO Plus 1TB',
        'category': 'ssd',
        'base_price': 450.00,
        'image': 'ssd.jpg',
        'specs': {
            'capacidade': '1TB',
            'tipo': 'NVMe M.2',
            'velocidade_leitura': '4200 MB/s',
            'velocidade_escrita': '3600 MB/s',
            'interface': 'PCIe 3.0',
            'factor_forma': 'M.2 2280'
        },
        'description': 'SSD NVMe de alto desempenho com ótima confiabilidade'
    },
    {
        'id': 'ssd-002',
        'name': 'WD Blue SN570 500GB',
        'category': 'ssd',
        'base_price': 250.00,
        'image': 'ssd.jpg',
        'specs': {
            'capacidade': '500GB',
            'tipo': 'NVMe M.2',
            'velocidade_leitura': '3500 MB/s',
            'velocidade_escrita': '3000 MB/s',
            'interface': 'PCIe 3.0',
            'factor_forma': 'M.2 2280'
        },
        'description': 'SSD NVMe de entrada com bom custo-benefício'
    },
    {
        'id': 'ssd-003',
        'name': 'Kingston A400 240GB',
        'category': 'ssd',
        'base_price': 150.00,
        'image': 'ssd.jpg',
        'specs': {
            'capacidade': '240GB',
            'tipo': 'SATA 2.5"',
            'velocidade_leitura': '500 MB/s',
            'velocidade_escrita': '350 MB/s',
            'interface': 'SATA III',
            'factor_forma': '2.5 polegadas'
        },
        'description': 'SSD SATA compacto e econômico'
    },
    
    # HDs
    {
        'id': 'hd-001',
        'name': 'Seagate Barracuda 2TB',
        'category': 'hd',
        'base_price': 350.00,
        'image': 'hd.jpg',
        'specs': {
            'capacidade': '2TB',
            'velocidade': '7200 RPM',
            'cache': '256MB',
            'interface': 'SATA III',
            'factor_forma': '3.5 polegadas',
            'mtbf': '2 milhões de horas'
        },
        'description': 'HD de armazenamento confiável para desktops'
    },
    {
        'id': 'hd-002',
        'name': 'WD Blue 1TB',
        'category': 'hd',
        'base_price': 250.00,
        'image': 'hd.jpg',
        'specs': {
            'capacidade': '1TB',
            'velocidade': '7200 RPM',
            'cache': '64MB',
            'interface': 'SATA III',
            'factor_forma': '3.5 polegadas',
            'mtbf': '2 milhões de horas'
        },
        'description': 'HD de armazenamento de entrada'
    },
    
    # Fontes
    {
        'id': 'fonte-001',
        'name': 'Corsair RM850x 850W',
        'category': 'fonte',
        'base_price': 600.00,
        'image': 'fonte.jpg',
        'specs': {
            'potencia': '850W',
            'certificacao': '80+ Gold',
            'conectores': '1x 20+4pin, 2x 4+4pin, 8x 6+2pin',
            'ventilador': '135mm',
            'modular': 'Totalmente modular',
            'garantia': '10 anos'
        },
        'description': 'Fonte modular de alta qualidade com certificação Gold'
    },
    {
        'id': 'fonte-002',
        'name': 'EVGA 650W 80+ Bronze',
        'category': 'fonte',
        'base_price': 350.00,
        'image': 'fonte.jpg',
        'specs': {
            'potencia': '650W',
            'certificacao': '80+ Bronze',
            'conectores': '1x 20+4pin, 1x 4+4pin, 6x 6+2pin',
            'ventilador': '120mm',
            'modular': 'Semi-modular',
            'garantia': '3 anos'
        },
        'description': 'Fonte confiável com bom custo-benefício'
    },
    
    # Coolers
    {
        'id': 'cooler-001',
        'name': 'Noctua NH-D15',
        'category': 'cooler',
        'base_price': 450.00,
        'image': 'water.jpg',
        'specs': {
            'tipo': 'Air',
            'ventiladores': '2x 140mm',
            'tdp': '250W',
            'altura': '165mm',
            'compatibilidade': 'Intel LGA1700, AMD AM4/AM5',
            'ruido': '19.2 dB'
        },
        'description': 'Cooler ar de alto desempenho e silencioso'
    },
    {
        'id': 'cooler-002',
        'name': 'Corsair Liquid H100i RGB',
        'category': 'cooler',
        'base_price': 700.00,
        'image': 'water.jpg',
        'specs': {
            'tipo': 'Líquido AIO',
            'ventiladores': '2x 120mm',
            'tdp': '300W',
            'radiador': '240mm',
            'compatibilidade': 'Intel LGA1700, AMD AM4/AM5',
            'ruido': '25 dB'
        },
        'description': 'Cooler líquido all-in-one com RGB'
    },
    
    # Gabinetes
    {
        'id': 'case-001',
        'name': 'NZXT H510 Flow',
        'category': 'case',
        'base_price': 550.00,
        'image': 'gabinete.jpg',
        'specs': {
            'tipo': 'Mid Tower',
            'material': 'Aço e vidro temperado',
            'slots_ventiladores': '6',
            'slots_radiador': 'Até 280mm',
            'slots_hd': '2x 3.5" / 2x 2.5"',
            'slots_ssd': '2x M.2',
            'painel_vidro': 'Sim'
        },
        'description': 'Gabinete moderno com bom fluxo de ar'
    },
    {
        'id': 'case-002',
        'name': 'Corsair Carbide Series 275R',
        'category': 'case',
        'base_price': 400.00,
        'image': 'gabinete.jpg',
        'specs': {
            'tipo': 'Mid Tower',
            'material': 'Aço',
            'slots_ventiladores': '4',
            'slots_radiador': 'Até 240mm',
            'slots_hd': '2x 3.5" / 2x 2.5"',
            'slots_ssd': '2x M.2',
            'painel_vidro': 'Não'
        },
        'description': 'Gabinete clássico e robusto'
    },
    
    # Monitores
    {
        'id': 'monitor-002',
        'name': 'ASUS VP28UQG 28" 4K',
        'category': 'monitor',
        'base_price': 1200.00,
        'image': 'monitor.jpg',
        'specs': {
            'tamanho': '28 polegadas',
            'resolucao': '3840x2160 (4K)',
            'painel': 'TN',
            'frequencia': '60Hz',
            'tempo_resposta': '1ms',
            'conectores': 'HDMI 2.0, DisplayPort 1.2'
        },
        'description': 'Monitor 4K para gaming e edição'
    }
]
