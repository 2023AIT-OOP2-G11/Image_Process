import cv2

# 画像を読み込む
image_path = '/Users/K22021kk/work/oop2/lecture12/gettyimages-1250238624-612x612.jpg'  

# Haarカスケード分類器をロードする
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 画像のファイルパスを指定してください
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not read the image.")
    # ここでプログラムを終了するか、エラー処理を行ってください

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 顔を検出する
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 検出された顔に枠を描画する
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    roi_gray = gray_image[y:y+h, x:x+w]
    edges = cv2.Canny(roi_gray, 100, 200)
    edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    image[y:y+h, x:x+w] = cv2.addWeighted(image[y:y+h, x:x+w], 1, edges_color, 1, 0)


# 結果を表示する
cv2.imshow('Detected Faces', image)

# キー入力を待つ
cv2.waitKey(0)
cv2.destroyAllWindows()