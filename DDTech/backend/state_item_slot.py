import reflex as rx
from DDTech.constants import MAIN_ITEMS

class State_ItemSlot(rx.State):
    button_opacity:list[str] = ["0"]*len(MAIN_ITEMS)

    def show_buttons(self,index) -> None:
        self.button_opacity[index] = "1"

    def hide_buttons(self,index) -> None:
        self.button_opacity[index] = "0"
