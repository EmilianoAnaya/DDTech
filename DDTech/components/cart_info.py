import reflex as rx
import DDTech.constants as const
from DDTech.styles.colors import TextColors

def cart_info() -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(
                "0"
            ),
            rx.icon(
                tag=const.CART_ICON,
                size=20,
            ),
            spacing="0",
            color=TextColors.HEADER
        )
    )