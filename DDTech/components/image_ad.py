import reflex as rx
from DDTech.backend.state_image_slider import State_ImageSlider

def image_ad(src:str, index:int) -> rx.Component:
    return rx.image(
        src=src,
        width="100%",
        height="338px",
        position="absolute",
        z_index=State_ImageSlider.appearence[index],
        opacity=State_ImageSlider.appearence[index],
        transition="opacity 0.5s ease",
    )
