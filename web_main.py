from flask import Flask, request, render_template

app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
def top():
    return render_template("top.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return '画像がありません'

    image = request.files['image']

    if image.filename == '':
        return 'ファイルが選択されていません'

    # 画像を保存するディレクトリを指定
    upload_directory = 'uploads/'

    # 一意のファイル名を生成
    filename = upload_directory + 'uploaded_image.png'

    # 画像を保存
    image.save(filename)

    return '画像がアップロードされました: ' + filename

# アップロードリスト画像表示
@app.route('/upload_list')
def upload_list():

    # 画像監視プログラムから受け取ったファイル名配列
    # imgs = ['1.png','2.png','3.png']

    return render_template('upload_list.html',imgs=imgs)

# Cannyフィルタによる輪郭抽出画像表示
@app.route('/canny')
def canny():

    # imgs = ['1.png','2.png','3.png']
    
    return render_template('canny.html',imgs=imgs)

# グレースケール画像表示
@app.route('/gray_scale')
def gray_scale():

    # imgs = ['1.png','2.png','3.png']
    
    return render_template('gray_scale.html',imgs=imgs)

# モザイク画像表示
@app.route('/mosaic')
def mosaic():

    # imgs = ['1.png','2.png','3.png']
    
    return render_template('mosaic.html',imgs=imgs)

# 顔検出して枠で囲む画像表示
@app.route('/rectangle')
def rectangle():

    # imgs = ['1.png','2.png','3.png']
    
    return render_template('rectangle.html',imgs=imgs)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

