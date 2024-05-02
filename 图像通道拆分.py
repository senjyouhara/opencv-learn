import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    img = cv2.imread("assets/img2.jpg", cv2.IMREAD_UNCHANGED)
    # 拆分通道
    b,g,r = cv2.split(img)

    for bx in b:
        for x in range(0,6):
            bx[x] = 255

    # 合并通道
    img = cv2.merge((b,g,r))

    # 色彩空间转换
    # bgr转灰度图
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # bgr转HSV
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow("图像窗口", img)
    cv2.waitKey(0)

    pass