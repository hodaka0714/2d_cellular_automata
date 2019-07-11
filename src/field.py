import numpy as np
import matplotlib.pyplot as plt


class Field():
    """二次元セルオートマトンのセルの情報をまとめたクラス。
    """
    def __init__(self, size):
        self.size = size
        self.field = self.init_field(size)

    def init_field(self, size):
        """
        ■■□
        □■■
        □■□
        の要素をはじめに↑をフィールドの中心に追加

        Args:
            size(int): フィールドの縦横サイズ

        Returns:
            はじめのフィールドの値（行列）
        """
        field = np.zeros((size, size))
        field[size//2, size//2] = 1
        field[(size//2)-1, (size//2)-1] = 1
        field[(size//2)-1, (size//2)] = 1
        field[(size//2), (size//2)+1] = 1
        field[(size//2)+1, size//2] = 1
        return field

    def proceed_one_step(self):
        """現在からひとステップ進んだフィールドを返す。

        そのとき用いるルールは
        https://ja.wikipedia.org/wiki/ライフゲーム#ライフゲームのルール
        を用いる。
        """
        f = self.field
        s = self.size
        next_step = np.zeros((s, s))
        for i in range(s):
            for j in range(s):
                # 周りのセルの情報を変数に入れる
                u_l, u_c, u_r =\
                    f[(i-1)%s][(j-1)%s], f[(i-1)%s][j%s], f[(i-1)%s][(j+1)%s]
                c_l, c_c, c_r =\
                    f[i%s][(j-1)%s], f[i%s][j%s], f[i%s][(j+1)%s]
                l_l, l_c, l_r =\
                    f[(i+1)%s][(j-1)%s], f[(i+1)%s][j%s], f[(i+1)%s][(j+1)%s]
                neighbors = np.array([u_l, u_c, u_r, c_l, c_r, l_l, l_c, l_r])
                myself = c_c

                # ここからはライフゲームのルール
                neighbor_sum = neighbors.sum()
                if c_c == 0:
                    if neighbor_sum == 3:
                        next_step[i][j] = 1
                elif c_c == 1:
                    if neighbor_sum == 2 or neighbor_sum == 3:
                        next_step[i][j] = 1
                    elif neighbor_sum <= 1:
                        next_step[i][j] = 0
                    elif neighbor_sum >= 4:
                        next_step[i][j] = 0

        self.field = next_step
        return None

    def get_current_field_image(self):
        """フィールドを画像にして表示する
        """
        im = plt.imshow(self.field*256)
        plt.show()
