import reflex as rx

def heading_main(title_heading:str) -> rx.Component:
    return rx.box(
        rx.heading(title_heading, color="white",size="4"),
        rx.separator(size="4",orientation="horizontal",color_scheme="yellow"),
        width="100%"
    )