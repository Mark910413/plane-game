import os
import pygame

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 静态资源目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景音乐路径
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/bg.flac')
# 字体颜色
TEXT_SCORE_COLOR = pygame.Color(88, 46, 84)
# 开始界面图片资源路径
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
# 开始按钮图片
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 结束界面图片
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')

# 我方飞机的静态资源
OUR_PLAN_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero1.png'),
    os.path.join(ASSETS_DIR, 'images/hero2.png')
]
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png'),
]
OUR_DESTROY_SOUNDS = os.path.join(ASSETS_DIR, 'sounds/game_over.wav')
# 子弹
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')
# 发射的声音
BULLET_SHOOT_SOUNDS = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

# 敌方飞机
SMALL_ENEMY_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/enemy1.png')]
SMALL_ENEMY_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png')
]
SMALL_ENEMY_PLANE_DOWN_SOUNDS = os.path.join(ASSETS_DIR, 'sounds/enemy1_down.wav')

# 小型飞机分值
SCORE_SHOOT_SMALL = 10

# 游戏结果储存的文件地址
PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, 'store/rest.txt')
