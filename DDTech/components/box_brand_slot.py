import reflex as rx
from DDTech.styles.styles import Sizes

def box_brand_slot(Width:str, img_src:str)->rx.Component:
    return rx.box(
        rx.image(
            src=img_src,
        ),
        width=Width,
        background_color="white",
        border_radius=Sizes.EXTRA.value,
    )