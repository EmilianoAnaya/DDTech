import reflex as rx
from DDTech.components.header_top import header_top
from DDTech.components.header_bottom import header_bottom

def header() -> rx.Component:
    return rx.vstack(
        header_top(),
        header_bottom(),
        spacing="0",
    ),
        
