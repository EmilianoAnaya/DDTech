import reflex as rx
from DDTech.constants import MAIN_ITEMS, BRANDS_IMAGES


class Item_Slider(rx.State):
    margin_left:list[int] = [0,0]
    slides_counter: list[int] = [0,0]
    items_limit:list[int] = [len(MAIN_ITEMS)-4,len(BRANDS_IMAGES)-4]

    def slide_box(self,index:int,value:int) -> None:
        tmp_margin_left = self.margin_left[index] + value
        if tmp_margin_left > 0:
            self.margin_left[index] = self.items_limit[index]*-212
        elif tmp_margin_left < self.items_limit[index]*-212:
            self.margin_left[index] = 0
        else:
            self.margin_left[index] = self.margin_left[index] + value