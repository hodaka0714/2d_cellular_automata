import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from field import Field

SIZE = 50
STEPS = 200


def main():

    # 注意: なぜかこの一文はこの位置に書かないと正常に動かない
    fig = plt.figure()

    field = Field(SIZE)
    # はじめのフィールドがみたかったら↓のコメントを外す
    # field.get_current_field_image()

    ims = []
    for i in range(STEPS):
        im = plt.imshow(field.field*256, animated=True)
        ims.append([im])
        field.proceed_one_step()

    ani = animation.ArtistAnimation(fig, ims, interval=100)
    plt.show()


if __name__ == '__main__':
    main()
