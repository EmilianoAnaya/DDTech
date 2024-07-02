import reflex as rx
from DDTech.styles.styles import Sizes
from DDTech.styles.colors import TextColors

def link_mega_menu(title: str) -> rx.Component:
    return rx.box(
        rx.link(
            rx.text(title,width="100%",
                    align="left",
                    style={
                        "color" : TextColors.HEADER.value,
                        "transition" : "padding-left 0.3s ease",
                        "_hover" : {
                            "color" : TextColors.HOVER_CATEGORY_TEXT.value,
                            "padding_left" : Sizes.SMALL.value
                        }
                    }
                    ),
            rx.separator(color_scheme="yellow",size="4",orientation="horizontal",width="95%"),

        ),
        width="25%",
        spacing="0",
        padding_y=Sizes.EXTRA_SMALL.value,
        margin_x=Sizes.EXTRA_SMALL.value,
    )