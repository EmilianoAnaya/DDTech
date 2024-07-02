import reflex as rx
from DDTech.components.btn_slider import btn_slider_left, btn_slider_right
from DDTech.components.image_ad import image_ad
from DDTech.components.selector_ad import selector_ad
from DDTech.backend.state_image_slider import State_ImageSlider
from DDTech import constants as const

def image_slider() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            const.BANNER,
            lambda src, index: image_ad(src,index)
        ),
        btn_slider_left(const.ARROW_LEFT),
        btn_slider_right(const.ARROW_RIGHT),

        selector_ad(),

        height="338px",
        width="100%",
        position="relative",
        on_mouse_enter=State_ImageSlider.show_items,
        on_mouse_leave=State_ImageSlider.hide_items,
        on_mount=State_ImageSlider.auto_slide,
    )