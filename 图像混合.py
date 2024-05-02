import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    img = cv2.imread("assets/img3.png", cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread("assets/img4.png", cv2.IMREAD_UNCHANGED)

    img3 = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
    cv2.imshow("图像窗口", img3)
    cv2.waitKey(0)
    pass