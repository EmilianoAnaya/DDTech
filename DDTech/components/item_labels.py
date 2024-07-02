import reflex as rx
from DDTech.styles.styles import Sizes

def item_labels()->rx.Component:
    return rx.hstack(
        rx.image(
            src="new_label.jpg",
            border_radius=Sizes.SMALL.value,
        ),
        width="100%",
    ),