import reflex as rx
from DDTech.styles.styles import Sizes
from DDTech.backend.state_image_slider import State_ImageSlider

def btn_selector(index:int) -> rx.Component:
    return rx.button(
        width="0.5%",
        height="10px",
        size="1",
        border_radius=Sizes.EXTRA_BIG.value,
        style={
            "_hover" : {
                "background_color" : "#3498db" ,
            },
        },
        cursor="pointer",
        background_color = State_ImageSlider.buttons_colors[index-1],
        on_click=State_ImageSlider.current_slide(index),
    )