import pygame
import constants

class Bullet(pygame.sprite.Sprite):
    """ 子弹类 """
    # 子弹的状态
    active = True

    def __init__(self, screen, plane, speed = 10):
        super().__init__()
        self.screen = screen
        # 速度
        self.speed = speed
        self.plane = plane

        # 加载子弹的图片
        self.image = pygame.image.load(constants.BULLET_IMG)

        # 子弹的初始位置
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        # 发射的生意效果
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUNDS)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, *agrs):
        """更新子弹的位置"""
        self.rect.top -= self.speed
        # 超出屏幕的范围
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        # 绘制子弹
        self.screen.blit(self.image, self.rect)
