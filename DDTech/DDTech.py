import reflex as rx
from DDTech.views.header import header
from DDTech.views.menu import menu
from DDTech.styles.styles import BASE_STYLE
from DDTech.styles.styles import Sizes
from DDTech.backend.state_image_slider import State_ImageSlider


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
    )


app = rx.App(
    style=BASE_STYLE,
    stylesheets=["https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap"]
)
app.add_page(index,title="DD Tech")
app._compile()