import reflex as rx
from DDTech.styles.styles import Sizes
from DDTech import constants as const
from DDTech.components.btn_selector import btn_selector
from DDTech.backend.state_image_slider import State_ImageSlider


def selector_ad() -> rx.Component:
    return rx.box(
        rx.flex(
            *[btn_selector(index) for index in range(1, len(const.BANNER)+1)],
            justify="center",
            flex_wrap="wrap",
            direction="row",
            spacing="2",
            width="100%",
        ),
        width="auto",
        padding=Sizes.SMALL.value,
        border_radius=Sizes.EXTRA_SMALL.value,  
        background_color = "white",
        position="relative",
        top=State_ImageSlider.top_selector,
        opacity=State_ImageSlider.img_opacity,
        margin="0 auto",
        z_index=3,
        style={
            "transition" : "top 0.2s ease, opacity 0.2s ease"
        }
    ),