import reflex as rx
import asyncio
from threading import Timer
from DDTech.styles.styles import Sizes
from DDTech.constants import BANNER

class State_ImageSlider(rx.State):
    img_selecter_top:str = "-30px"
    img_opacity:str = "0"
    position:str = Sizes.EXTRA_BIG.value
    btn_opacity = "0"
    on_image = False

    index_img: int = 1
    appearence: list[str] = ["1"] + ["0"] * (len(BANNER)-1)

    flag_auto_slide:bool = False
    timer_delay: int = 5

    top_selector:str = "350px"
    buttons_colors: list[str] = ["#3498db"] + ["#d3d3d3"] * (len(BANNER)-1)
    
    def show_items(self)->None:
        self.position = "0px"
        self.btn_opacity = "0.33"
        self.img_selecter_top = "-55px"
        self.top_selector = "325px"
        self.img_opacity = "1"
        self.on_image = True
    
    def hide_items(self)->None:
        self.position = Sizes.EXTRA_BIG.value
        self.btn_opacity = "0"
        self.img_selecter_top = "-30px"
        self.top_selector = "350px"
        self.img_opacity = "0"
        self.on_image = False
        
    def plus_slide(self, index_slide: int) -> None:
        return State_ImageSlider.show_slide(self.index_img + index_slide)

    def current_slide(self, index_slide: int) -> None:
        return State_ImageSlider.show_slide(index_slide)

    @rx.background
    async def show_slide(self, index_slide: int) -> None:
        async with self:
            slides: int = len(BANNER)
            if index_slide > slides:
                self.index_img = 1
            elif index_slide < 1:
                self.index_img = slides
            else:
                self.index_img = index_slide

            self.appearence = ["0"] * slides
            self.buttons_colors = ["#d3d3d3"] * slides
            self.appearence[self.index_img - 1] = "1"
            self.buttons_colors[self.index_img - 1] = "#3498db"

    @rx.background
    async def auto_slide(self):
        async with self:
            if self.flag_auto_slide:
                return
            self.flag_auto_slide = True

        while True:
            await asyncio.sleep(self.timer_delay)
            async with self:
                if not self.on_image:
                    yield self.plus_slide(1)