from PIL import Image
import time
from pygame.locals import *
from HeroPlane import *
from plane import *



def start():
    # 设置窗体大小
    scree=pygame.display.set_mode((400,700),0,32)
    im = Image.open("./feiji/background.png")
    out = im.resize((400,700), Image.ANTIALIAS)
    out.save("./feiji/background2.png")
    # //设置图片背景图片
    image_file_path='./feiji/background2.png'
    background = pygame.image.load(image_file_path)
    hero_plan=HeroPlane(scree,"hero")
    enemy_plan=EnemyPlane(scree,"enemy")

# 实时更新图片
    while True:
        # 背景图片的位置
        scree.blit(background,(0,0))
        hero_plan.display()
        enemy_plan.display()
        enemy_plan.move()
        enemy_plan.launch_bullet()


        # 键盘监听
        PD(hero_plan)
        time.sleep(0.01)
        pygame.display.update()


def PD(hero_plan):
    for event in pygame.event.get():
        # 鼠标点击叉号退出
        if event.type == QUIT:
            print("exit")
            exit()
            # 键盘按下事件
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero_plan.move_left()
                print("left")
            elif event.key == K_d or event.key == K_RIGHT:
                hero_plan.move_right()
                print("right")
            elif event.key == K_SPACE:
                hero_plan.launch_bullet()
                print("space")

if __name__=='__main__':
    start()