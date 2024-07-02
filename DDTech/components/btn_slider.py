import reflex as rx
from DDTech.styles.styles import BTN_SLIDER_STYLE
from DDTech.backend.state_image_slider import State_ImageSlider

def btn_slider_left(icon: str)->rx.Component:
    return rx.button(
        rx.icon(
            tag=icon,
            size=15,
        ),
        left=State_ImageSlider.position,
        opacity=State_ImageSlider.btn_opacity,
        style=BTN_SLIDER_STYLE,
        on_click=State_ImageSlider.plus_slide(-1)
    )

def btn_slider_right(icon: str)->rx.Component:
    return rx.button(
        rx.icon(
            tag=icon,
            size=15,
        ),
        right=State_ImageSlider.position,
        opacity=State_ImageSlider.btn_opacity,
        style=BTN_SLIDER_STYLE,
        on_click=State_ImageSlider.plus_slide(1)
        
    )