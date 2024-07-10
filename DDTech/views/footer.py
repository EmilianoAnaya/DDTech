import reflex as rx
from DDTech.constants import PAYMENTS_LOGOS
from DDTech.styles.styles import Sizes

def footer()->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("Holaaaaaa"),
            background_color="#202020",
            justify='center',
            width="100%",
        ),
        rx.center(
            rx.box(
                rx.spacer(),
                rx.image(
                   src=PAYMENTS_LOGOS,
                ),
            ),
            padding=Sizes.DEFAULT.value,
            background_color="#121212",
            width="100%",
        ),
    )