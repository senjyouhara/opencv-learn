import math

import cv2
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
# 读取图像
# IMREAD_COLOR 彩色模式加载，透明通道将忽略，默认
# IMREAD_UNCHANGED 包括alpha通道加载模式
# IMREAD_GRAYSCALE 灰度模式加载
    img = cv2.imread("assets/img1.png", cv2.IMREAD_UNCHANGED)
    centerpointX,centerpointY = math.ceil(img.shape[1]/2), math.ceil(img.shape[0]/2)
# 绘制直线
    cv2.line(img, (centerpointX - 100,centerpointY - 100), (centerpointX + 100,centerpointY - 100), (0,0,255), 2)
    cv2.line(img, (centerpointX - 100,centerpointY - 100), (centerpointX - 100,centerpointY + 100), (0,0,255), 2)
    cv2.line(img, (centerpointX - 100,centerpointY + 100), (centerpointX + 100,centerpointY + 100), (0,0,255), 2)
    cv2.line(img, (centerpointX + 100,centerpointY + 100), (centerpointX + 100,centerpointY - 100), (0,0,255), 2)

    # 绘制圆形  当thickness为-1时填充内部颜色
    cv2.circle(img, (centerpointX, centerpointY), 30, (0,0,255), 3)

    cv2.imshow("图像窗口", img)
    cv2.waitKey(0)



#    在matplotlib中展示图片,需要对图像进行翻转,从bgr转成rgb
#     plt.imshow(img[:,:,::-1], cmap='gray')
#     plt.title("匹配结果")
# # 去掉x轴水瓶刻度
#     plt.xticks([])
# # 去掉y轴水瓶刻度
#     plt.yticks([])
#     plt.show()
#     cv2.waitKey(0)
# 保存图片
#    cv.imwrite("./png.png", img)
    
    pass


