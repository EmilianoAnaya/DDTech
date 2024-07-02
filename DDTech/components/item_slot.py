import reflex as rx
from DDTech.styles.styles import Sizes
from DDTech.components.item_labels import item_labels
from DDTech.components.item_buttons import item_buttons
from DDTech.components.item_price_tag import item_price_tag
from DDTech.backend.state_item_slot import State_ItemSlot as State

def item_slot() -> rx.Component:
    return rx.vstack(
        item_labels(),
        rx.image(
            src="item_example1.png",
            cursor="pointer",
            width="80%",
            margin="0 auto 1em",
            border_radius=Sizes.DEFAULT.value,
        ),
        rx.link(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis, augue ut mattis pretium, erat tellus suscipit lorem, quis elementum libero mauris vel sapien.",
            color="white",
            cursor="pointer",
        ),
        item_price_tag(),
        item_buttons(),
        width="100%",
        on_mouse_enter=State.show_buttons,
        on_mouse_leave=State.hide_buttons,
    )