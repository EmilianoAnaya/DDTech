import reflex as rx
from DDTech.constants import CategoriesIcons as icons
from DDTech.components.link_mega_menu import link_mega_menu
from DDTech.styles.colors import CategoriesColors as Color
from DDTech.styles.styles import Sizes
from DDTech.styles.colors import TextColors

class Visibility(rx.State):
    display:list[str] = ["none"] * 15
    top:str = "90px"

    def hide_options(self):
        self.display = ["none"] * len(self.display)
    
    def show_options(self,index):
       self.display[index] = "block" if not self.display[index] == "block" else "none"
    

def btn_category(information: list[str, str, int, list[str]], index:int) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon(
                tag=information[0],
                size=15,
            ),
            rx.text(
                information[1],
            ),
            rx.spacer(),
            rx.icon(
                tag=icons.LEFT_ARROW.value,
                size=15,
            ),
            align_items="center",
        width="100%",
        padding_y=Sizes.DEFAULT.value,
        style={
            "color" : TextColors.HEADER.value,
            "transition" : "padding-left 0.3s ease",
            "_hover" : {
                "color" : TextColors.HOVER_CATEGORY_TEXT.value,
                "padding_left" : Sizes.SMALL.value,
            }
        }
        ),
        rx.box(
            rx.flex(
                rx.foreach(information[3], link_mega_menu),
                direction="column",
                wrap="wrap",
                height=f"{information[2]}px",
            ),
            border_color="white",
            border_style="solid",
            margin_top=f"{information[2]-20}px",
            background_color=Color.CATGORY_MEGA_MENU.value,
            position="absolute",
            padding_y=Sizes.MEDIUM.value,
            padding_x=Sizes.BIG.value,
            width="790px",
            display=Visibility.display[index],
            style={
                "@media (min-width: 1121px)" : {
                    "margin_left" : "1065px"
                },
                "@media (max-width: 1120px)" : {
                    "margin_left" : "1045px"
                },
            },
        ),
    z_index=2000,
    border_radius="0px",
    width="100%",
    position="relative",
    background_color=Color.BUTTONS.value,
    padding_y=Sizes.EXTRA.value,
    on_click=Visibility.show_options(index),
    on_blur=Visibility.hide_options,
    style={
        "_hover" : {
            "bg" : Color.HOVER_BUTTON.value
        }
    }
    )