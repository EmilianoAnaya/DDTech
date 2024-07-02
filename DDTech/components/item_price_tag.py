import reflex as rx
from DDTech.styles.styles import Sizes
from DDTech.styles.colors import TextColors

def item_price_tag(price:str)->rx.Component:
    return rx.vstack(
        rx.text(price,color=TextColors.HOVER_CATEGORY_TEXT.value,weight="bold"),
        rx.hstack(
            rx.icon(tag="check",size=15,color="white"),
            rx.text("CON EXISTENCIA",font_size=Sizes.MEDIUM.value,color="white"),
            spacing="1",
            align="center",
            background_color="#1765be",
            border_radius=Sizes.EXTRA_SMALL.value,
            padding_x=Sizes.SMALL.value,
        ),
        spacing="0",
    ),