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
        return render_template("top.html")

    # 画像を保存するディレクトリを指定
    upload_directory = 'static/'

    uploaded_filename = image.filename

    # 一意のファイル名を生成
    filename = upload_directory + uploaded_filename

    # 画像を保存
    image.save(filename)

    return render_template("top.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

