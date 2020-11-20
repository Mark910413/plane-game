
from game.war import PlaneWar


def main():
    """  初始化游戏入口 """

    # 初始化
    war = PlaneWar()
    war.add_small_enemies(15)
    war.run_game()


if __name__ == '__main__':
    main()
