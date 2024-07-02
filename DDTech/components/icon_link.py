import reflex as rx

def icon_link(Url: str, icon: str, hovercolor:str) -> rx.Component:
    return rx.link(
            rx.icon(
                tag=icon,
                color="white",
                style={
                    "_hover": {"color": hovercolor}
                }
            ),
        href=Url,
        is_external=True,
        
    )