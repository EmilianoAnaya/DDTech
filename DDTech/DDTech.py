import reflex as rx
from DDTech.views.bottom_links import bottom_link
from DDTech.views.header import header
from DDTech.views.menu import menu
from DDTech.styles.styles import BASE_STYLE
from DDTech.styles.styles import Sizes


class Status(rx.State):
    pass    

def index() -> rx.Component:
    return rx.box(
        header(),
        rx.center(
            menu(),
            width="100%",
            margin_top=Sizes.BIG.value
        ),
        bottom_link(),
    )


app = rx.App(
    style=BASE_STYLE,
    stylesheets=["https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap"]
)
app.add_page(index,title="DD Tech")
app._compile()