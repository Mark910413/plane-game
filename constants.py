import os

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 静态资源目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景音乐路径
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/bg.flac')

# 图片资源路径
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
# 开始按钮图片
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')


# 我方飞机的静态资源
OUR_PLAN_IMG_1 = os.path.join(ASSETS_DIR, 'images/hero1.png')
OUR_PLAN_IMG_2= os.path.join(ASSETS_DIR, 'images/hero2.png')
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png'),
]

# 子弹
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')
# 发射的声音
BULLET_SHOOT_SOUNDS = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

