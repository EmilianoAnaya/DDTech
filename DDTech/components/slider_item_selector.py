import reflex as rx
from DDTech.constants import ARROW_LEFT,ARROW_RIGHT
from DDTech.styles.styles import Sizes

def slider_item_selector(title_heading:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading(title_heading, color="white",size="4"),
            rx.spacer(),
            rx.button(
                rx.icon(
                    tag=ARROW_LEFT,
                    size=12,
                ),
                size="1",
            ),
            rx.button(
                rx.icon(
                    tag=ARROW_RIGHT,
                    size=12,
                ),
                size="1",
            ),
            margin_bottom=Sizes.SMALL.value,
        ),
        rx.separator(size="4",orientation="horizontal",color_scheme="yellow"),

        width="100%"
    )