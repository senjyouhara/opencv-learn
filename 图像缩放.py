import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    img = cv2.imread("assets/img2.jpg", cv2.IMREAD_UNCHANGED)

    # dsize绝对尺寸， fx,fy缩放因子,根据图像xy乘以该系数,需要把dsize设为None
    # cv2.INTER_LINEAR 双线性插值法
    # cv2.INTER_NEAREST 最近邻差值
    # cv2.INTER_AREA 像素区域重采样 默认
    # cv2.INTER_CUBIC 双三次插值
    # img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_LINEAR)
    img = cv2.resize(img, None, fx=0.5, fy=0.5,  interpolation= cv2.INTER_NEAREST)
    cv2.imshow("图像窗口", img)
    cv2.waitKey(0)
    pass