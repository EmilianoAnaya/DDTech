import reflex as rx
from DDTech.styles.styles import Sizes
from DDTech.components.item_labels import item_labels
from DDTech.components.item_buttons import item_buttons
from DDTech.components.item_price_tag import item_price_tag
from DDTech.backend.state_item_slot import State_ItemSlot as State

def item_slot(img_src:str, item_des:str, item_price:str, index:str) -> rx.Component:
    return rx.vstack(
        item_labels(),
        rx.image(
            src=img_src,
            cursor="pointer",
            width="80%",
            margin="0 auto 1em",
            border_radius=Sizes.DEFAULT.value,
        ),
        rx.link(
            rx.text(
                item_des,
                size="1",
                font_family="Oswald",
                weight="bold",
                style={
                    "color" : "#8c8c8c",
                    "transition" : "color 0.5s ease",
                    "_hover" : {
                        "color" : "#1765be"
                    }
                }
            ),
            color="white",
            cursor="pointer",
        ),
        item_price_tag(item_price),
        item_buttons(index),
        width="100%",
        margin_bottom = Sizes.SMALL.value,
        on_mouse_enter=State.show_buttons(index),
        on_mouse_leave=State.hide_buttons(index),
    )