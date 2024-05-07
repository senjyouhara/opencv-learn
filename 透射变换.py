import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    img = cv2.imread("assets/img2.jpg", cv2.IMREAD_UNCHANGED)
    height, width = img.shape[:2]
    # 需围绕逆时针设置点
    pts1 = np.float32([[0,0], [width,0], [0,height],  [width,height]])
    pts2 = np.float32([[150,150], [600,50], [150,height-100], [width,height]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    plt.imshow(dst[:,:,::-1])
    plt.title("title")
# 去掉x轴水瓶刻度
#     plt.xticks([])
# 去掉y轴水瓶刻度
#     plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    pass