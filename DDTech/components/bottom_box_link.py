import reflex as rx

def bottom_box_link(img_src:str, Width:str)->rx.Component:
    return rx.box(
        background=f"center/cover url('/{img_src}')",
        width=Width,
        height="350px",
    )