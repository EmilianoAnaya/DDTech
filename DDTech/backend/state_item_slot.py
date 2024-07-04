import reflex as rx
from DDTech.components.item_labels import item_labels
from DDTech.components.item_price_tag import item_price_tag
from DDTech.components.item_buttons import item_buttons
from DDTech.styles.styles import Sizes

class Item_Slot(rx.ComponentState):
    img_src:str
    item_des:str
    item_price:str
    button_opacity:str = "0"

    def show_buttons(self)->None:
        self.button_opacity = "1"

    def hide_buttons(self)->None:
        self.button_opacity = "0"

    @classmethod
    def get_component(cls,**props) -> rx.Component:
        img_src = props.pop("img_src",cls.img_src)
        item_des = props.pop("item_des",cls.item_des)
        item_price = props.pop("item_price",cls.item_price)

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
            item_buttons(cls),
            width="100%",
            margin_bottom = Sizes.SMALL.value,
            on_mouse_enter=cls.show_buttons,
            on_mouse_leave=cls.hide_buttons,
        )
