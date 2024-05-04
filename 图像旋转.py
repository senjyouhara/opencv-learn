import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    img = cv2.imread("assets/img2.jpg", cv2.IMREAD_UNCHANGED)

    marix = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), 45, 0.7)
    img = cv2.warpAffine(img, marix, (img.shape[1], img.shape[0]))

    plt.imshow(img[:,:,::-1], cmap='gray')
    plt.title("title")
# 去掉x轴水瓶刻度
#     plt.xticks([])
# 去掉y轴水瓶刻度
#     plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    pass