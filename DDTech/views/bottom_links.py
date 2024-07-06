import reflex as rx
from DDTech.components.bottom_box_link import bottom_box_link
from DDTech.constants import BOTTOM_LINKS_IMAGES


def bottom_link()->rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                bottom_box_link(BOTTOM_LINKS_IMAGES.REPAIR.value, "33.33%"),
                bottom_box_link(BOTTOM_LINKS_IMAGES.PRIDE.value, "33.33%"),
                bottom_box_link(BOTTOM_LINKS_IMAGES.TWITCH.value, "33.33%"),
                spacing="0",
                width="100%",
            )
        ),
        width="100%",
    )