from enum import Enum
from typing import List, Tuple
# LINKS
YOUTUBE_LINK = "https://www.youtube.com"
FACEBOOK_LINK = "https://www.facebook.com"
TWITTER_LINK = "https://x.com/home"
INSTAGRAM_LINK = "https://www.instagram.com"
GMAIL_LINK = "https://mail.google.com"

# ICONS
YOUTUBE_ICON = "youtube"
FACEBOOK_ICON = "facebook"
TWITTER_ICON = "twitter"
INSTAGRAM_ICON = "instagram"
GMAIL_ICON = "mail"
PHONE_ICON = "phone"
HELP_ICON = "circle-help"
HOME_ICON = "home"
CART_ICON = "shopping-cart"
SQUARE_PLUS = "square-plus"

# MENU_SLIDER_ICONS
ARROW_LEFT = "arrow-left"
ARROW_RIGHT = "arrow-right"

# FOOTER
PAYMENTS_LOGOS = "logos-pagos.png"

# APP_LOGO
DDTECH_LOGO = "ddtech.png"

# CATEGORIES_RESOURCES
class CategoriesIcons(Enum):    
    MENU_ICON = "menu"
    ACCESSORIES_ICON = "mouse"
    SPEAKER_ICON = "speaker"
    COMPUTER_ICON = "computer"
    COMPONENTS_ICON = "cpu"
    CONSUMABLES_ICON = "droplets"
    STORAGE_ICON = "hard-drive"
    ELECTRONICS_ICON = "battery"
    PRINTER_ICON = "printer"
    MONITOR_ICON = "monitor"
    SOFTWARE_ICON = "binary"
    SMARPHONE_ICON = "smartphone"
    NETWORK_ICON = "network"
    APPLE_ICON = "apple"
    ENERGY_ICON = "zap"
    MERCHANDISE_ICON = "shirt"
    LEFT_ARROW = "circle-arrow-right"

# CATEGORIES_ITEMS
class CategoriesItems(Enum):
    ACCESSORIES = [
        "Ver todo",
        "Docking Station",
        "Tapete para sillas",
        "Kits de Accesorios",
        "Herramienta",
        "Accesorios para streaming",
        "Gabinete Ext. para GPU",
        "Reposamuñecas",
        "Decodificador",
        "Simuladores",
        "Escritorios Gamer",
        "Lentes VR",
        "Limpiadores",
        "Sillas",
        "Aire Comprimido",
        "Otros Accesorios",
        "Drones",
        "Game Pads",
        "Cajones de Dinero",
        "Lectores de Código",
        "Mouse Pad",
        "Cargadores",
        "Baterías / Power Banks",
        "Fundas",
        "Transmisores",
        "Presentadores",
        "Mochilas",
        "Lectores de Memoria",
        "Hubs USB",
        "Cámaras Web",
        "Bases / Soportes",
        "Cables / Adaptadores",
        "Teclado",
        "Mouse",
    ]

    AUDIO = [
        "Ver todo",
        "Accesorios para Headset",
        "Accesorios para Microfono",
        "Amplificador de Diadema",
        "Bases para auriculares",
        "Adaptadores",
        "Mini Componente",
        "Manos libres",
        "Microfonos",
        "Reproductores",
        "Bocinas",
        "Diademas",
        "Audífonos",
    ]

    COMPUTERS = [
        "Ver todo",
        "Tableta digitalizadora",
        "Portátiles",
        "Servidor",
        "Tablets",
        "Escritorio",
    ]

    COMPONENTS = [
        "Ver todo",
        "Cable ó base GPU vertical",
        "Pastas termicas",
        "Enf. líquidos (Custom)",
        "Enf. líquidos (AIO)",
        "Disipador CPU (Aire)",
        "Unidades Optane",
        "Accesorios",
        "Iluminación",
        "Kits de Actualizacion",
        "Tarjetas de TV / Capturadoras",
        "Fuente de Alimentación",
        "Ventilación",
        "Gabinetes",
        "Tarjetas de sonido",
        "Unidades Ópticas",
        "Tarjetas de video",
        "Tarjetas madre",
        "Procesadores",
        "Memoria RAM",
        "Unidades SSD",
        "Discos Duros Internos",
    ]

    CONSUMABLES = [
        "Ver todo",
        "Cintas",
        "Papel",
        "Toners",
        "Tinta",
        "Ópticos",
    ]

    STORAGE = [
        "Ver todo",
        "Enclosure",
        "NAS/RED",
        "Tarjetas de Memoria",
        "Memorias USB",
        "Discos Duros Externos",
        "Dock HDD",
    ]

    ELECTRONICS = [
        "Ver todo",
        "Scooters",
        "Asistentes de Voz",
        "Proyector Holografico",
        "Smart Devices",
        "TV BOX",
        "Pantallas",
        "HTPC",
        "Consolas",
        "Cámaras Digitales",
        "Iluminación",
    ]

    PRINTER = [
        "Ver todo",
        "Ticket",
        "Multifuncionales",
        "Impresoras",
    ]

    MONITOR = [
        "Ver todo",
        "Stand",
        "Proyectores",
        "Monitores",
    ]

    SOFTWARE = [
        "Ver todo",
        "Antivirus",
        "Ofimatica",
        "Sistemas Operativos",
    ]

    SMARTPHONE = [
        "Ver todo",
        "Feature phone",
        "Smartwatch",
        "Windows",
        "iOS",
        "Android",
    ]

    NETWORK = [
        "Ver todo",
        "Conectores de Red",
        "Videovigilancia",
        "Enchufe Inteligente",
        "PowerLine",
        "Switch KVM",
        "Router",
        "Tarjetas de Red",
        "Switch",
        "Expansores",
        "Cables",
        "Antenas",
        "Adaptadores",
        "Access Point",
    ]

    APPLE = [
        "Ver todo",
        "Pencil",
        "iPad",
        "Almacenamiento",
        "Memorias de expansión",
        "Cables y Adaptadores",
    ]

    ENERGY = [
        "Ver todo",
        "No Breaks",
        "Reguladores",
    ]

    MERCHANDISE = [
        "Ver todo",
        "Suéteres",
        "Boxers",
        "Servicios",
        "Termos",
        "Playeras",
    ]

# CATEGORIES
CATEGORIES: list[list[str, str, int, list[str]]] = [
    [CategoriesIcons.ACCESSORIES_ICON.value, "Accesorios", 280, CategoriesItems.ACCESSORIES.value],
    [CategoriesIcons.SPEAKER_ICON.value, "Audio", 150, CategoriesItems.AUDIO.value],
    [CategoriesIcons.COMPUTER_ICON.value, "Computadoras", 150, CategoriesItems.COMPUTERS.value],
    [CategoriesIcons.COMPONENTS_ICON.value, "Componentes", 190, CategoriesItems.COMPONENTS.value],
    [CategoriesIcons.CONSUMABLES_ICON.value, "Consumibles", 150, CategoriesItems.CONSUMABLES.value],
    [CategoriesIcons.STORAGE_ICON.value, "Almacenamiento", 150, CategoriesItems.STORAGE.value],
    [CategoriesIcons.ELECTRONICS_ICON.value, "Electrónica de Consumo", 150, CategoriesItems.ELECTRONICS.value],
    [CategoriesIcons.PRINTER_ICON.value, "Impresión", 150, CategoriesItems.PRINTER.value],
    [CategoriesIcons.SOFTWARE_ICON.value, "Software", 150, CategoriesItems.SOFTWARE.value],
    [CategoriesIcons.MONITOR_ICON.value, "Monitores", 150, CategoriesItems.MONITOR.value],
    [CategoriesIcons.SMARPHONE_ICON.value, "Celulares", 150, CategoriesItems.SMARTPHONE.value],
    [CategoriesIcons.NETWORK_ICON.value, "Redes", 150, CategoriesItems.NETWORK.value],
    [CategoriesIcons.APPLE_ICON.value, "Apple", 150, CategoriesItems.APPLE.value],
    [CategoriesIcons.ENERGY_ICON.value, "Energia", 150, CategoriesItems.ENERGY.value],
    [CategoriesIcons.MERCHANDISE_ICON.value, "Merchandise", 150, CategoriesItems.MERCHANDISE.value],
]


# IMAGE_ADS
BANNER: list[str] = [
    "DDTech_image_ad.png",
    "DDTech_image_ad2.png",
    "DDTech_image_ad3.png",
    "DDTech_image_ad4.png",
    "DDTech_image_ad5.png",
]


# MAIN CONTENT ITEMS
MAIN_ITEMS: list[list[str, str]] = [
    ["item_example1.png", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis, augue ut mattis pretium, erat tellus suscipit lorem, quis elementum libero mauris vel sapien.","$14,999.00",],
    ["item_example2.png","Computadora PRIDE MSI MAESTRO / NVIDIA GeForce RTX 4090 / INTEL CORE I9-14900K / 64GB RAM / 2TB SSD / 1000W 80+ GOLD / INCLUYE WIFI / Gorra de Regalo!","$79,999.00"],
    ["item_example3.png","Tarjeta de Video Asus Dual Radeon RX 6600 V2 / AMD Radeon RX6600 / PCIe 4.0 / 1 HDMI 2.1 / 3 Puertos DisplayPort 1.4a / DUAL-RX6600-8G-V2","$4,299.00"],
    ["item_example4.png","Monitor Curvo LG 39GS95QE Ultragear OLED / 39 pulgadas / WQHD / 800R / 240Hz / 0.03ms / DisplayHDR / True Black 400 / AMD FreeSync Premium Pro / NVIDIA G-Sync / HDMI 2.1 / DisplayPort / 39GS95QE-B","$14,999.00"],
    ["item_example5.png","Fuente NZXT C750 Bronze / 750W / 80+ Bronze / PFC Ativo / Black / PA-7B2BB-US/","$999.00"],
    ["item_example6.png","Computadora PRIDE GAMING PBA WHITE WOLF LUFT / NVIDIA GeForce RTX 4060 / AMD Ryzen 5 5500 / 32GB RAM / 1TB SSD / 650W 80+ BRONZE / INCLUYE WIFI","$14,999.00"],
    ["item_example7.png","Monitor Gamer MSI G274F LED 27 / Full HD / G-Sync / 180Hz / Rapid IPS / HDMI / Negro / G274F","$2,999.00"],
    ["item_example8.png","Sistema de Enfriamiento Liquido HYTE THICC Q60 / 240mm / 0-3000RPM / FAN-HYTE-Q60-BW/","$4,899.00"]
]

# BRAND IMAGES
BRANDS_IMAGES: list[str] = [
    "Intel.png",
    "Munfrost.png",
    "XPG.png",
    "ASUS.png",
    "Fury.png",
    "Aorus.png",
    "AMD.png" 
]

# BOTTOM_LINKS_IMAGES
class BOTTOM_LINKS_IMAGES(Enum):
    REPAIR = "Motherboard_Repair.jpg"
    PRIDE = "Pride_DDTech.jpeg"
    TWITCH = "Twitch_DDTech.png"


ITEMS_BOTTOM_LINKS: list[str,str,str,str,str] = [
    [BOTTOM_LINKS_IMAGES.REPAIR.value,"Configurador","¿Buscas la computadora ideal para ti?, Encuentra tu computadora perfecta respondiendo estas simples preguntas. Tendrás lo que necesitas al instante.","IR AL SITIO","auto"],
    [BOTTOM_LINKS_IMAGES.PRIDE.value,"Pride","Todo lo que necesitas para llevar tus partidas al siguiente nivel con Pride. Siente el orgullo Gamer y llena tus partidas de poder con el equipo de Pride.","IR AL SITIO","auto"],
    [BOTTOM_LINKS_IMAGES.TWITCH.value,"Gracias por seguirnos en Twitch","Son una comunidad increible","VER NOTICIA","pointer"]
]