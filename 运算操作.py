import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    #opencv加法和numpy加法存在差异，opencv是饱和度操作，而numpy是模运算
    x = np.uint8([250])
    y = np.uint8([10])

    # 250+10=260 => 255
    print(cv2.add(x,y))
    # 250+10 = 260 %256 = 4
    print(x + y)

    img = cv2.imread("assets/img3.png", cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread("assets/img4.png", cv2.IMREAD_UNCHANGED)


    # cv2.imshow("图像窗口", cv2.add(img,img2))
    # cv2.imshow("图像窗口", img + img2)
    cv2.imshow("图像窗口", cv2.subtract(img,img2))
    # cv2.imshow("图像窗口", img - img2)
    cv2.waitKey(0)

    pass