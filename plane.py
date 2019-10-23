# Author:Liu
from PublicBullet import *
import random
from PIL import Image
import Planes

class EnemyPlane(Planes.Plane):
    def __init__(self,screen,name):
        self.x = 0
        self.y = 0

        self.imag_name = "./feiji/airplane.png"
        super().__init__(screen, name)
        self.direction ="right"

    def launch_bullet(self):
        number = random.randint(1, 100)
        if number == 88 or number == 66:
            super().launch_bullet()

    # 飞机移动
    def move(self):
        if self.direction=="right":
            self.x+=2
        elif self.direction=="left":
            self.x-=2
        if self.x>350:
            self.direction="left"
        elif self.x<0:
            self.direction="right"




