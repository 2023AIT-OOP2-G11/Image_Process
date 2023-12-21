import cv2
def Canny(img):
    # ガウシアンフィルターを適用してノイズを削除
    kernel_size = 5                                                         # カーネルサイズの設定
    sigma = 0                                                               # sigmaの設定
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)    # ガウシアンフィルターの適用
    # Cannyエッジ検出を適用
    canny = cv2.Canny(blurred, threshold1=30, threshold2=100)
    
    return canny