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

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

