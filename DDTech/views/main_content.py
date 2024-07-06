import reflex as rx
from DDTech.components.image_slider import image_slider
from DDTech.components.header_slider import header_slider
from DDTech.components.box_item_slot import box_item_slot
from DDTech.components.box_brand_slot import box_brand_slot
from DDTech.backend.state_item_slider import Item_Slider
from DDTech.constants import MAIN_ITEMS,BRANDS_IMAGES

def main_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            image_slider(),
            rx.heading("Productos Destacados", color="white",size="4"),
            rx.separator(size="4",orientation="horizontal",color_scheme="yellow"),
            rx.desktop_only(
                rx.flex(
                    *[box_item_slot("22%",item_info) for item_info in MAIN_ITEMS],
                    width="100%",
                    flex_wrap="wrap",
                    direction="row",
                    justify="between"
                ),
                width="100%",
            ),
            header_slider("Últimos Productos",0),
            rx.desktop_only(
                rx.hstack(
                    *[box_item_slot("200px",item_info) for item_info in MAIN_ITEMS],
                    spacing="3",
                    margin_left=f"{Item_Slider.margin_left[0]}px",
                    transition = "margin-left 0.5s ease"
                ),
            ),
            header_slider("Las Mejores Marcas",1),
            rx.desktop_only(
                rx.hstack(
                    *[box_brand_slot("200px",item_info) for item_info in BRANDS_IMAGES],
                    spacing="3",
                    margin_left=f"{Item_Slider.margin_left[1]}px",
                    transition = "margin-left 0.5s ease"
                ),
            ),
            visibility="visible",
        ),
        width="100%",
        overflow="hidden",
    )