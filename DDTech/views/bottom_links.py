import reflex as rx
from DDTech.components.bottom_box_link import bottom_box_link
from DDTech.constants import ITEMS_BOTTOM_LINKS


def bottom_links()->rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                *[bottom_box_link(Box_details, "33.33%") for Box_details in ITEMS_BOTTOM_LINKS],
                spacing="0",
                width="100%",
            )
        ),
        width="100%",
    )