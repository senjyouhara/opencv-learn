import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    img = cv2.imread("assets/img2.jpg", cv2.IMREAD_UNCHANGED)

    # m 2*3矩阵， dsize 输出宽高
    # [1  0  tx]
    # [0  1  ty]
    # dsize 输出图像大小
    img = cv2.warpAffine(img, np.float32([
        [1, 0, 100],
        [0, 1, 100],
    ]), (img.shape[1] + 100, img.shape[0] + 100))


    plt.imshow(img[:,:,::-1], cmap='gray')
    plt.title("匹配结果")
# 去掉x轴水瓶刻度
#     plt.xticks([])
# 去掉y轴水瓶刻度
#     plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    pass