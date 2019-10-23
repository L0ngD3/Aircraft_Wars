# Author:Liu

import pygame
from PublicBullet import *
class Plane(object):
    def __init__(self, screen,name):
        # 设置英雄飞机的起始位置
        # self.x = 30
        # self.y = 600
        # 设置窗口要显示的内容
        self.screen = screen
        self.name=name

        self.image = pygame.image.load(self.imag_name).convert()
        # 储存英雄飞机的子弹
        self.bullet_list = []
    def display(self):
        # 更新飞机位置
        self.screen.blit(self.image,(self.x,self.y))
        # 存放要删除的子弹
        need_del_list = []
        for item in self.bullet_list:
            if item.judgu():
                need_del_list.append(item)
        # 删除保存的子弹
        for del_item in need_del_list:
            self.bullet_list.remove(del_item)
        # 更新子弹位置
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    def launch_bullet(self):

        new_bullet=PublicBullet(self.x,self.y,self.screen,self.name)
        # new_bullet=PublicBullet.__init__(self.x,self.y,self.screen,self.neme)
        self.bullet_list.append(new_bullet)