import reflex as rx
from DDTech.styles.styles import Sizes

def search_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            bg="#4990df",
            border_radius="0px",
            border_bottom_left_radius="10px",
            border_top_left_radius="10px",
            
        ),
        rx.button(
            "Buscar",
            bg="#4990df",
            border_radius="0px"
        ),
        spacing="0",
        margin_x=Sizes.DEFAULT.value
    )