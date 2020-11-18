"""
飞机基类
我方飞机 敌方小飞机 敌方中型飞机 敌方大型飞机
"""

import pygame
import constants


class Plan(pygame.sprite.Sprite):
    """
    飞机的基类
    """
    # 飞机的图片
    plane_images = []

    # 摧毁的图片
    destroy_images = []
    # 坠毁的声音
    down_sound_src = None
    # 飞机的状态 True 活的； False side
    active = True
    #  飞机发射子弹的精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed = 10):
        super().__init__()
        self.screen = screen
        # 加载静态资源
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()

        # 游戏窗口宽高
        self.width, self.height = self.screen.get_size()

        # 飞机飞行的速度
        self.speed = speed

        # 获取飞机的位置
        self.rect = self.img_list[0].get_rect()

    def load_src(self):
        """ 加载静态资源 """
        # 飞机图片
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))
        # 飞机坠毁的图片
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))
        # 坠毁的音乐
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        # 飞机向上移动
        self.rect.top -= self.speed

    def move_down(self):
        # 飞机向下移动
        self.rect.top += self.speed

    def move_left(self):
        # 飞机向左移动
        self.rect.left -= self.speed

    def move_right(self):
        # 飞机向右移动
        self.rect.left += self.speed

    def broken_down(self):
        """ 飞机坠毁效果 """
        # 1. 播放坠毁yiny
        if self.down_sound:
            self.down_sound.play()
        # 2.飞机坠毁画面
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        # 3. 坠毁后
        self.active = False


class OurPlane(Plan):
    """ 我方的飞机 """
    # 飞机的图片
    plane_images = [constants.OUR_PLAN_IMG_1, constants.OUR_PLAN_IMG_2]
    # 飞机爆炸的图片
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    #  飞机坠毁的音乐
    down_sound_src = None

    def update(self, frame):
        """ 更新飞机的动画效果 """
        if frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)

    def move_up(self):
        super().move_up()
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        super().move_down()
        if self.rect.top > self.height:
            self.rect.top = self.height

    def move_left(self):
        super().move_left()
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left > self.width:
            self.rect.left = self.width