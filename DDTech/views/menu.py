import reflex as rx
from DDTech.views.sidebar import sidebar
from DDTech.views.main_content import main_content
from DDTech.styles.styles import MAX_WIDTH



def menu() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                sidebar(),
                rx.spacer(),
                rx.vstack(
                    main_content(),
                    width="75%",
                ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                main_content(),
                width="100%",
            ),
        ),
        max_width = MAX_WIDTH,
        width="100%",
    )
