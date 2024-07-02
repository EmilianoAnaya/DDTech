import reflex as rx

def sidebar_image(src:str) -> rx.Component:
    return rx.image(
        src=src,
        width="100%",
        height="auto",
    )