import reflex as rx
from DDTech.styles.styles import Sizes
from DDTech.constants import CART_ICON, SQUARE_PLUS
from DDTech.styles.colors import ItemButtons as color

def item_buttons(cls) -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.icon(tag=CART_ICON,
                    background_color=color.CART_OFF,
                    color="white",
                    size=30,
                    padding_y=Sizes.SMALL.value,
                    padding_x=Sizes.EXTRA_SMALL.value,
                    cursor="pointer",
                    style={
                        "border_radius" : f"{Sizes.SMALL.value} 0 0 {Sizes.SMALL.value}",
                        "transition" : "background-color 0.5s ease",
                        "_hover" : {
                            "background_color" : color.CART_ON
                        }
                    },
                ),
            rx.text("Agregar",
                    size="1",
                    color="white",
                    background_color=color.ADD_OFF,
                    cursor="pointer",
                    user_select="none",
                    padding="0.59em",
                    style={
                        "border_radius" : f"0 {Sizes.SMALL.value} {Sizes.SMALL.value} 0",
                        "transition" : "background-color 0.5s ease",
                        "_hover" : {
                            "background_color" : color.ADD_ON
                        }
                    },
                ),
            spacing="0",
            align="center",
        ),
        rx.link(
            rx.hstack(
                rx.icon(
                    tag=SQUARE_PLUS,
                    size=20,
                ),
                rx.text(
                    "Ver más",
                    user_select="none",
                ),
                spacing="0",
                align="center",
                style={
                    "transition" : "color 0.3s ease",
                    "color" : color.CART_OFF,
                    "_hover" : {
                        "color" : color.CART_ON,
                    }
                }
            ),
            margin_top=Sizes.EXTRA_SMALL.value,
            margin_left=Sizes.MEDIUM.value,
            cursor="pointer",
        ),
        direction="row",
        width="100%",
        wrap="wrap",
        opacity = cls.button_opacity,
        transition = "opacity 0.3s ease",
    ),