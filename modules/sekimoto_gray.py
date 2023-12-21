import cv2

def grayscale_and_threshold(input_image_path):
    # 画像を読み込む
    image = cv2.imread(input_image_path)

    # グレースケールに変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale image',gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return gray_image, image
if __name__ =="__main__":
    input_image_path = '/Users/k22076kk/oop2/lecture12/freephoto.jpg'
    grayscale_and_threshold(input_image_path)

    

