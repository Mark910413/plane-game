import constants


class PlayRest(object):
    # 总分
    __score = 0
    # 生命数量
    __life = 3
    # 生命值
    __blood = 1000

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        """ 设置游戏成绩 """
        print(value)
        if value < 0:
            return 0
        self.__score = value

    def set_history(self):
        """ 记录最高分 """
        if int(self.get_max_core()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w') as f:
                f.write('{0}'.format(self.score))

    def get_max_core(self):
        """ 读取历史最高分 """
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE, 'r') as f:
            r = f.read()
            if r:
                rest = r
            return rest
