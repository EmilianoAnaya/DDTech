from enum import Enum

class CategoriesColors(Enum):
    HEADER = "#333333"
    BUTTONS = "#212121"
    HOVER_BUTTON = "black"
    CATGORY_MEGA_MENU = "#191a1a"

class BackgroundColors(Enum):
    HEADER_TOP = "#1d1d1d"
    HEADER_BOTTOM = "#1765be"
    BODY = "#121212"

class TextColors(Enum):
    HEADER = "#fff"
    HOVER_CATEGORY_TEXT = "#3498db"

class HoverColors(Enum):
    FACEBOOK = "#3b5998"
    YOUTUBE = "#c4302b"
    INSTAGRAM = "#E1306C"
    TWITTER = "#1DA1F2"
    GMAIL = "#f2a60c"
    QUESTIONS = "#94E0E2"

class ItemButtons(Enum):
    CART_OFF = "#575757"
    CART_ON = "#1d6ca1"
    ADD_OFF = "#a8a8a8"
    ADD_ON = "#3498db"