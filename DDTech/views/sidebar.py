import reflex as rx
from DDTech.components.categories import categories


def sidebar() -> rx.Component:
    return rx.vstack(
        categories(),
        rx.spacer(),
        rx.image(src="Meses_sin_intereses.jpg"),
        rx.image(src="Gratis.png"),
        rx.image(src="Dudas.jpg"),
        rx.image(src="Ayuda.jpg"),
        rx.image(src="GeForce.png"),
        width="25%"
    )