import reflex as rx

def icon_link(Url: str, icon: str, hovercolor:str,color_default="white",Size=25) -> rx.Component:
    return rx.link(
            rx.icon(
                tag=icon,
                size=Size,
                color=color_default,
                style={
                    "_hover": {"color": hovercolor}
                }
            ),
        href=Url,
        is_external=True,
        
    )