#food.py
import colors as Colors
from object import Object


class Food(Object):
    def __init__(self, orientacao=0, position=[1, 1], color=Colors.green, size=30 ):
        super().__init__(orientacao, position, color, size)


