import cv2
import numpy as np

# Haar Cascadeファイルを読み込む
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def apply_mosaic_to_faces(image_path, mosaic_size=15):
    # 画像を読み込む
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔検出
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 各顔にモザイクを適用
    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        # モザイク処理
        face = cv2.resize(face, (w // mosaic_size, h // mosaic_size))
        face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)
        img[y:y+h, x:x+w] = face

    return img

# 画像パス（ここに処理したい画像のパスを指定）デバック用
image_path = '/Users/k22012kk/Downloads/Oop2_11.jpeg'

# モザイク処理を実行

mosaic_img = apply_mosaic_to_faces(image_path)

# 結果を表示
cv2.imshow('Mosaic', mosaic_img)
cv2.waitKey(0)
cv2.destroyAllWindows()