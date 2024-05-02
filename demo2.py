import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    img = np.zeros((200, 200, 3), np.uint8)
    # img = cv2.imread("assets/img2.jpg", cv2.IMREAD_UNCHANGED)

    # 获取像素坐标颜色
    px = img[100, 100]
    # 获取blue通道值
    blue = img[100, 100, 0]
    # 设置坐标颜色
    img[100, 100] = (255, 255, 255)
    img[101, 100] = (255, 255, 255)
    img[100, 101] = (255, 255, 255)
    img[101, 101] = (255, 255, 255)

    cv2.imshow("图像窗口", img)
    cv2.waitKey(0)

    pass