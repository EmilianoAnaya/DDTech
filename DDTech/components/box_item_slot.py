import reflex as rx
from DDTech.backend.state_item_slot import Item_Slot

def box_item_slot(Width:str, item_info:list) -> rx.Component:
    item_slot = Item_Slot.create
    return rx.box(
        item_slot(
            img_src = item_info[0],
            item_des = item_info[1],
            item_price = item_info[2],
        ),
        width=Width
    )