import reflex as rx

def store_info_footer(details:list[str,str])->rx.Component:
    return rx.hstack(
        rx.icon(
            tag=details[0],
            width="25%",
            color="#666"
        ),
        rx.text(
            details[1],
            width="75%",
            color="#666",
        ),
        spacing="0",
        width="100%",
    )