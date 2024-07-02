import reflex as rx

def separator(size:str) -> rx.Component:
    return rx.separator(
        color_scheme="yellow",
        orientation="vertical",
        size=size
    )