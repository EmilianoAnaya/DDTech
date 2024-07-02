import reflex as rx
from DDTech.components.item_slot import item_slot

def desktop_item_slot(item_info:list, index:int) -> rx.Component:
    return rx.box(
        item_slot(
            item_info[0],
            item_info[1],
            item_info[2],
            index
        ),
        width="22%"
    )