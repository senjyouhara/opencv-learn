import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    img = cv2.imread("assets/img2.jpg", cv2.IMREAD_UNCHANGED)
    height, width = img.shape[:2]
    # pts1 = np.float32([[50,50], [600,50], [50,600]])
    # pts2 = np.float32([[100,100], [600,250], [50,600]])

    pts1 = np.float32([[50,50], [width,50], [50,height]])
    pts2 = np.float32([[100,100], [width,400], [-100,height]])
    # pts2 = np.float32([[100,100], [200,50], [100,250]])
    M = cv2.getAffineTransform(pts1, pts2)
    # 仿射变换
    dst = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    # 水平翻转
    # dst = cv2.warpAffine(img, np.float32([[-1,0,width], [0, 1,0]]), (img.shape[1], img.shape[0]))
    # 垂直翻转
    # dst = cv2.warpAffine(img, np.float32([[1,0,0], [0, -1, height]]), (img.shape[1], img.shape[0]))
    # 镜像变换
    # dst = cv2.warpAffine(img, np.float32([[-1,0,width], [0, -1, height]]), (img.shape[1], img.shape[0]))
    plt.imshow(dst[:,:,::-1])
    plt.title("title")
# 去掉x轴水瓶刻度
#     plt.xticks([])
# 去掉y轴水瓶刻度
#     plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    pass