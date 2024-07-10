import reflex as rx
from DDTech import constants as const
from DDTech.styles.colors import HoverColors
from DDTech.styles.styles import Margins, MAX_WIDTH
from DDTech.constants import DDTECH_FOOTER_LOGO, DDTECH_INFO
from DDTech.components.store_info_footer import store_info_footer
from DDTech.components.icon_link import icon_link
from DDTech.components.link_footer import box_link_footer

def upper_footer() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.flex(
                box_link_footer("Pride"),
                box_link_footer("Pride"),
                box_link_footer("Configurar"),
                box_link_footer("Preguntas Frecuentes"),
                box_link_footer("Nosotros"),
                box_link_footer("Aviso Legal"),
                box_link_footer("Blog"),
                box_link_footer("Terminos y condiciones"),
                box_link_footer("Contacto"),
                wrap='wrap',
                width="33.33%",
                spacing="7",
            ),
            rx.vstack(
                rx.image(
                    src=DDTECH_FOOTER_LOGO,
                    margin="0 auto",
                ),
                rx.text(
                    "Componentes y Tecnología de México DDTECH © 2024",
                    margin="0 auto",
                    size="2",
                    color="#cecece",
                ),
                width="33.33%",
            ),
            rx.vstack(
                *[store_info_footer(details) for details in DDTECH_INFO],
                wrap='wrap',
                width="22.22%",
            ),
            rx.flex(
                icon_link(const.FACEBOOK_LINK, const.FACEBOOK_ICON, HoverColors.FACEBOOK.value,"#666",30),
                icon_link(const.YOUTUBE_LINK, const.YOUTUBE_ICON, HoverColors.YOUTUBE.value,"#666",30),
                icon_link(const.TWITTER_LINK, const.TWITTER_ICON, HoverColors.TWITTER.value,"#666",30),
                icon_link(const.INSTAGRAM_LINK, const.INSTAGRAM_ICON, HoverColors.INSTAGRAM.value,"#666",30),
                icon_link(const.GMAIL_LINK, const.GMAIL_ICON, HoverColors.GMAIL.value,"#666",30),
                wrap='wrap',
                width="11.11%",
                spacing="2",
                padding_left=Margins.SMALL.value,
            ),
            justify='center',
            width=MAX_WIDTH,
        ),
        padding_y=Margins.SMALL.value,
        width="100%",
        background_color="#202020",
    )