import reflex as rx
from DDTech.constants import CategoriesIcons
from DDTech.constants import CategoriesItems
from DDTech.styles.colors import CategoriesColors
from DDTech.styles.styles import Sizes
from DDTech.components.btn_category import btn_category
from DDTech.constants import CATEGORIES

class Sidebar(rx.State):
    display:str = "block"
    
    def show_options(self):
       self.display = "block" if not self.display == "block" else "none"

def categories() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.button(
                    rx.hstack(
                        rx.icon(
                            tag=CategoriesIcons.MENU_ICON.value,
                            size=20,
                        ),
                        rx.text(
                            "CATEGORÍAS",
                            weight="bold",
                            font_family="Times New Roman",
                        ),
                        width="100%",
                        padding_x=Sizes.SMALL.value,
                    ),
                width="100%",
                background_color=CategoriesColors.HEADER.value,
                padding_y=Sizes.BIG.value,
                border_radius="0px",
                on_click=Sidebar.show_options
                ),
                rx.vstack(
                    *[btn_category(category, i) for i, category in enumerate(CATEGORIES)],
                    width="100%",
                    spacing="0",
                    display=Sidebar.display,
                ),
            spacing="0",
            ),
        ),
        width="100%"
    )


