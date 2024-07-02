import reflex as rx
from DDTech.components.icon_link import icon_link
from DDTech.styles.styles import Sizes, HEADER_BOTTOM_STYLE
from DDTech.components.separator import separator
from DDTech.components.search_bar import search_bar
from DDTech.components.cart_info import cart_info
import DDTech.constants as const

def header_bottom() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.image(
                    src=const.DDTECH_LOGO,
                    margin_x=Sizes.SMALL.value,
                ),
                rx.icon(const.HOME_ICON),
                separator("1"),
                rx.text("PRODUCTOS"),
                separator("1"),
                rx.text("TIENDAS"),
                separator("1"),
                rx.text("PRIDE"),
                separator("1"),
                rx.text("CONFIGURAR PC"),
                separator("1"),
                rx.text("ASUS PBA"),
                separator("1"),
                rx.text("AORUS PC"),
                search_bar(),
                cart_info(),
                separator("1"),
                rx.text("Comprar"),
                align="center",
                justify="center"
            ),
        ),
        style=HEADER_BOTTOM_STYLE,
        width="100%"
    )