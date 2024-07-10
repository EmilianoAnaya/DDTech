import reflex as rx
from DDTech.styles.styles import Sizes,Margins

def bottom_box_link(Box_details:list[str,str,str,str], Width:str)->rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                Box_details[1],
                weight="bold",
                size="5",
                font_family="Roboto",
                color="white",
                text_shadow= "1px 1px 2px black",
                margin_bottom=Margins.EXTRA_SMALL.value,
                cursor=Box_details[4]
            ),
            rx.text(
                Box_details[2],
                size="2",
                font_family="Sans-serif",
                color="white",
                text_shadow= "1px 1px 2px black",
                height=Margins.DEFAULT.value,
            ),
            rx.separator(
                size="4",
                orientation="horizontal",
                color_scheme="yellow",
            ),
            rx.text(
                Box_details[3],
                size="1",
                font_family="Sans-serif",
                color="white",
                text_shadow= "1px 1px 2px black",
                cursor="pointer",
            ),
            padding_x=Sizes.DEFAULT.value,
            position="absolute",
            bottom="0",
            width="100%",
            # background_color="lightblue",
        ),
        position="relative",
        background=f"center/cover url('/{Box_details[0]}')",
        width=Width,
        height="350px",
    )