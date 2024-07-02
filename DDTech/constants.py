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