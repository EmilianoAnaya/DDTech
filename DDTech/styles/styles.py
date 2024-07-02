from enum import Enum
from .colors import TextColors, BackgroundColors

# Constants
MAX_WIDTH = "70em"

class Margins(Enum):
    ZERO = "0px"
    EXTRA_SMALL = "25px"
    SMALL = "50px"
    MEDIUM = "75px"
    DEFAULT = "100px"
    EXTRA = "150px"
    BIG = "200px"
    EXTRA_BIG = "300px"

class Sizes(Enum):
    EXTRA_SMALL = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    EXTRA = "1.5em"
    BIG = "2em"
    EXTRA_BIG = "4em"


HEADER_TOP_STYLE = dict(
    bg=BackgroundColors.HEADER_TOP.value,
    padding_y=Sizes.EXTRA_SMALL.value,
    color=TextColors.HEADER.value
)

HEADER_BOTTOM_STYLE = dict(
    bg=BackgroundColors.HEADER_BOTTOM.value,
    color=TextColors.HEADER.value,
    font_size=Sizes.MEDIUM.value,
    padding_y=Sizes.EXTRA.value,
)

BASE_STYLE = {
    "background_color" : BackgroundColors.BODY.value
}

BTN_SLIDER_STYLE= {
    "width" : "auto",
    "cursor" : "pointer",
    "padding_y" : Sizes.BIG.value,
    "top" : Margins.EXTRA.value,
    "position" :"absolute",
    "z_index" : "3",
    "background_color" : "#fff",
    "transition" : "right 0.2s ease, left 0.2s ease, opacity 0.5s ease",
    "_hover" : {
        "background_color" : "#1368f1",
        "opacity" : "1"
    },
}

TRANSITION_ADD_CART= {
    "transition" : "background-color 0.5s ease",
}
