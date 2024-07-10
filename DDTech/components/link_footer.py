import reflex as rx

STYLE_HSTACK = {
    "transition" : "color 0.5s ease",
    "cursor" : "pointer",
}

class link_footer(rx.ComponentState):
    text_link:str
    color_hover:str = "#666"

    def on_box(self) -> None:
        self.color_hover="#3498db"

    def off_box(self) -> None:
        self.color_hover="#666"

    @classmethod
    def get_component(cls,**props) -> rx.Component:
        text_link = props.pop("text_link",cls.text_link)

        return rx.vstack(
            rx.link(
                rx.hstack(
                    rx.icon(tag="circle",
                            size=10,
                            color=cls.color_hover,
                            style=STYLE_HSTACK,
                            width="10%",
                    ),
                    rx.text(
                        text_link,
                        color=cls.color_hover,
                        style=STYLE_HSTACK,
                        size="1",
                        width="90%",
                    ),
                    align="center",
                ),
            ),
            rx.separator(size="4",
                         color_scheme="yellow"),
            width="100%",
            on_mouse_over=cls.on_box,
            on_mouse_leave=cls.off_box,
        )


def box_link_footer(text_link:str)->rx.Component:
    Link_Footer = link_footer.create
    return rx.box(
        Link_Footer(
            text_link = text_link,
        ),
        width="40%",
    )