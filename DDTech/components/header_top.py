import reflex as rx
from DDTech.components.icon_link import icon_link
from DDTech.styles.styles import Sizes, HEADER_TOP_STYLE
from DDTech.styles.colors import HoverColors
from DDTech.components.separator import separator
import DDTech.constants as const


def header_top() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.text("Nosotros"),
                    separator("2"),
                    rx.text("Blog"),
                    separator("2"),
                    rx.text("Contacto"),
                    align="center",
                ),
                rx.hstack(
                    icon_link(const.FACEBOOK_LINK, const.FACEBOOK_ICON, HoverColors.FACEBOOK.value),
                    icon_link(const.YOUTUBE_LINK, const.YOUTUBE_ICON, HoverColors.YOUTUBE.value),
                    icon_link(const.TWITTER_LINK, const.TWITTER_ICON, HoverColors.TWITTER.value),
                    icon_link(const.INSTAGRAM_LINK, const.INSTAGRAM_ICON, HoverColors.INSTAGRAM.value),
                    icon_link(const.GMAIL_LINK, const.GMAIL_ICON, HoverColors.GMAIL.value),
                    separator("2"),
                    rx.icon(tag=const.PHONE_ICON),
                    rx.text("(33) 28 77 04 35"),
                    separator("2"),
                    icon_link("https://ddtech.mx/preguntas_frecuentes", const.HELP_ICON, HoverColors.QUESTIONS.value),
                    margin_x=Sizes.BIG.value,
                    align="center"
                ),
                rx.hstack(
                    rx.text("Iniciar Sesión"),
                    separator("2"),
                    rx.text("Registrarme"),
                    align="center"
                ),
                spacing="9",
                justify="center",
                # style=HEADER_TOP_STYLE,
            ),
        ),
        style=HEADER_TOP_STYLE,
        width="100%",
    )
    