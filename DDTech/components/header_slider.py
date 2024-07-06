import reflex as rx
from DDTech.constants import ARROW_LEFT,ARROW_RIGHT
from DDTech.styles.styles import Sizes, BTN_SLIDER_HEADER

def header_slider(title_heading:str,index:int) -> rx.Component:
    from DDTech.backend.state_item_slider import Item_Slider
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
                on_click=Item_Slider.slide_box(index,212),
                style=BTN_SLIDER_HEADER,
            ),
            rx.button(
                rx.icon(
                    tag=ARROW_RIGHT,
                    size=12,
                ),
                size="1",
                on_click=Item_Slider.slide_box(index,-212),
                style=BTN_SLIDER_HEADER,
            ),
            margin_bottom=Sizes.SMALL.value,
            width="100%",
        ),
        rx.separator(size="4",orientation="horizontal",color_scheme="yellow"),
        width="100%"
    )