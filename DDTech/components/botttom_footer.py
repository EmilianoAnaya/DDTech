import reflex as rx
from DDTech.constants import PAYMENTS_LOGOS
from DDTech.styles.styles import Sizes, MAX_WIDTH


def bottom_footer()->rx.Component:
    return rx.center(
        rx.box(
            rx.spacer(),
            rx.image(
               src=PAYMENTS_LOGOS,
               align="right",
            ),
            width=MAX_WIDTH,
        ),
        padding=Sizes.DEFAULT.value,
        background_color="#121212",
        width="100%",
    ),