import reflex as rx
from DDTech.components.botttom_footer import bottom_footer
from DDTech.components.upper_footer import upper_footer

def footer()->rx.Component:
    return rx.vstack(
        upper_footer(),
        bottom_footer(),
        width="100%",
    )