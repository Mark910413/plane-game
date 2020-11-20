import pygame, sys

import constants
from game.plane import OurPlane, SmallEnemyPlane
from store.result import PlayRest


class PlaneWar(object):
    """飞机大战"""
    # 游戏状态 0 准备中 1 游戏中 2 结束
    READY = 0
    PLAYING = 1
    OVER = 2
    status = READY
    # 装载我方飞机
    our_plan = None
    # 帧数计数器
    frame = 0
    # 敌方飞机精灵组
    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    # 分数
    rest = PlayRest()

    def __init__(self):
        # 初始化游戏
        pygame.init()
        # 屏幕宽高
        self.width, self.height = 480, 852
        # 打开屏幕
        self.screen = pygame.display.set_mode((self.width, self.height))
        # 加载背景图片
        self.bg = pygame.image.load(constants.BG_IMG)
        # 加载结束图片
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)
        # 加载开始标题图片
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()
        # 标题的宽高
        t_width, t_height = self.img_game_title.get_size()
        # 设置标题的位置
        self.img_game_title_rect.topleft = (int((self.width - t_width) / 2), int((self.height - t_height) / 2))

        # 加载开始按钮
        self.img_game_start_btn = pygame.image.load(constants.IMG_GAME_START_BTN)
        self.img_game_start_btn_rect = self.img_game_start_btn.get_rect()
        btn_width, btn_height = self.img_game_start_btn.get_size()
        # 设置按钮开始按钮位置
        self.img_game_start_btn_rect.topleft = (int((self.width - btn_width) / 2), int((self.height - btn_height) / 2) + 100)

        # 游戏文字对象
        self.score_font = pygame.font.SysFont('fangsong', 32)
        # 加载背景音乐
        pygame.mixer.music.load(constants.BG_MUSIC)
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play(-1)

        # 装载我方飞机
        self.our_plan = OurPlane(self.screen, 8)

        self.clock = pygame.time.Clock()

    def bind_event(self):
        """ 绑定事件 """
        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.status == self.READY:
                    self.status = self.PLAYING

        # 被按下的键
        key_pressed = pygame.key.get_pressed()
        if self.status == self.PLAYING:
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                self.our_plan.move_up()
            if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                self.our_plan.move_down()
            if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                self.our_plan.move_left()
            if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                self.our_plan.move_right()
            if key_pressed[pygame.K_SPACE] and (self.frame % 5 == 0):
                self.our_plan.shoot(10)

    def add_small_enemies(self, num):
        # 装载敌方小飞机
        for i in range(num):
            plan = SmallEnemyPlane(self.screen, 4)
            plan.add(self.small_enemies, self.enemies)

    def run_game(self):
        """ 游戏的主循环 """
        while True:
            # 绑定事件
            self.bind_event()
            # 设置帧数率
            self.clock.tick(60)
            self.frame += 1
            if self.frame >= 60:
                self.frame = 0

            # 各个状态下
            if self.status == self.READY:
                # 游戏准备中
                # 绘制背景图
                # 绘制开始按钮
                self.screen.blit(self.bg, self.bg.get_rect())
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                self.screen.blit(self.img_game_start_btn, self.img_game_start_btn_rect)
            elif self.status == self.PLAYING:
                # 绘制游戏中的画面
                # 绘制背景图片
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制我方飞机
                self.our_plan.update(self.frame, self)
                # 绘制子弹
                self.our_plan.bullets.update(self)
                # 绘制敌方飞机
                # print(self.small_enemies)
                self.small_enemies.update()
                # 游戏分数
                score_text = self.score_font.render(
                    '得分:{0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                score_text_rect = score_text.get_rect()
                score_text_rect.topleft = (20, 50)
                self.screen.blit(score_text, score_text_rect)
            elif self.status == self.OVER:
                # 绘制游戏结束的画面
                # 绘制背景图
                self.screen.blit(self.bg_over, self.bg.get_rect())
                # 统计分数
                # 游戏分数
                score_text = self.score_font.render(
                    '{0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                score_text_rect = score_text.get_rect()
                score_text_rect.centerx = int(self.width / 2)
                score_text_rect.centery = int(self.height / 2)
                self.screen.blit(score_text, score_text_rect)
                # 历史最高分
                score_his = self.score_font.render(
                    '{0}'.format(self.rest.get_max_core()),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                score_his_rect = score_text.get_rect()
                score_his_rect.topleft = (150, 40)
                self.screen.blit(score_his, score_his_rect)
            pygame.display.flip()