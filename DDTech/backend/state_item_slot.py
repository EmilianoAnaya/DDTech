import reflex as rx

class State_ItemSlot(rx.State):
    button_opacity:str = "0",

    def show_buttons(self) -> None:
        self.button_opacity = "1"

    def hide_buttons(self) -> None:
        self.button_opacity = "0"
