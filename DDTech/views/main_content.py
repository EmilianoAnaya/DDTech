import reflex as rx
from DDTech.components.image_slider import image_slider
from DDTech.components.heading_main import heading_main
from DDTech.components.desktop_item_slot import desktop_item_slot
from DDTech.constants import MAIN_ITEMS

def main_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            image_slider(),
            rx.heading("Productos Destacados", color="white",size="4"),
            rx.separator(size="4",orientation="horizontal",color_scheme="yellow"),
            rx.desktop_only(
                rx.flex(
                    *[desktop_item_slot(item_info, i) for i,item_info in enumerate(MAIN_ITEMS)],
                    width="100%",
                    flex_wrap="wrap",
                    direction="row",
                    justify="between"
                ),
                width="100%",
            ),
            heading_main("Últimos Productos"),
            heading_main("Las Mejores Marcas"),
            visibility="visible",
        ),
        width="100%",
    )