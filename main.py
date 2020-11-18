import pygame, sys

import constants
from game.plane import OurPlane

def main():
    """  初始化游戏入口 """

    # 初始化
    pygame.init()
    width, height = 480, 852

    # 屏幕对象
    screen = pygame.display.set_mode((width, height))

    # 加载背景图片
    bg = pygame.image.load(constants.BG_IMG)

    # 加载开始标题图片
    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    img_game_title_rect = img_game_title.get_rect()
    # 标题的宽高
    t_width, t_height = img_game_title.get_size()
    # 设置标题的位置
    img_game_title_rect.topleft = (int((width - t_width) / 2), int((height - t_height) / 2))

    # 加载开始按钮
    img_game_start_btn = pygame.image.load(constants.IMG_GAME_START_BTN)
    img_game_start_btn_rect = img_game_start_btn.get_rect()
    btn_width, btn_height = img_game_start_btn.get_size()
    # 设置按钮开始按钮位置
    img_game_start_btn_rect.topleft = (int((width - btn_width) / 2), int((height - btn_height) / 2) + 100)

    # 加载背景音乐
    pygame.mixer.music.load(constants.BG_MUSIC)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    # 设置窗口标题
    pygame.display.set_caption('飞机乱炸')

    # 游戏状态 0 准备中 1 游戏中 2 结束
    status = 0

    # 装载我方飞机
    our_plan = OurPlane(screen)
    # 帧数计数器
    frame = 0
    clock = pygame.time.Clock()

    while True:
        # 设置帧数率
        clock.tick(60)
        frame += 1;
        if frame >= 60:
            frame = 0

        # 监听退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == 0:
                    status = 1
            elif event.type == pygame.KEYDOWN:
                if status == 1:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        our_plan.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        our_plan.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        our_plan.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        our_plan.move_right()

        # 各个状态下
        if status == 0:
            # 游戏准备中
            # 绘制背景图
            # 绘制开始按钮
            screen.blit(bg, bg.get_rect())
            screen.blit(img_game_title, img_game_title_rect)
            screen.blit(img_game_start_btn, img_game_start_btn_rect)
        elif status == 1:
            # 绘制游戏中的画面
            screen.blit(bg, bg.get_rect())
            our_plan.update(frame)
        pygame.display.flip()


if __name__ == '__main__':
    main()
