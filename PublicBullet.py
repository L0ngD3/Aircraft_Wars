# Author:Liu
import pygame
class PublicBullet(object):
    def __init__(self,x,y,screen,plan_name):
        self.screen =screen
        self.plan_name=plan_name
        if plan_name=="hero":
            self.x=x+40
            self.y=y-20
            image_name="./feiji/bullie.png"
        elif plan_name=="enemy":
            self.x=x+40
            self.y=y+30
            image_name="./feiji/bullie.png"
        self.image=   pygame.image.load(image_name).convert()

    # 子弹移动
    def move(self):
        if self.plan_name == "hero":
            self.y -= 2
        elif self.plan_name == "enemy":
            self.y+=2

    def display(self):
        # 显示子弹
        self.screen.blit(self.image, (self.x, self.y))
    def judgu(self):
        if self.y < 0 or self.y>700:
            return True
        else:
            return False
