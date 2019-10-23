# Author:Liu
import Planes
from PIL import Image
class HeroPlane(Planes.Plane):
    def __init__(self, screen,name):
        self.x = 230
        self.y = 600

        im = Image.open("./feiji/hero.PNG")
        out = im.resize((50, 50), Image.ANTIALIAS)
        out.save("./feiji/hero2.PNG")
        self.imag_name = "./feiji/hero2.PNG"
        super().__init__(screen,name)

    def move_left(self):
        if self.x>0:
             self.x -=10

    def move_right(self):
        if self.x<350:
            self.x += 10



