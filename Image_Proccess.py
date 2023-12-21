import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from modules.image_canny import Canny
from modules.mosaic_to_faces import apply_mosaic_to_faces
from modules.sekimoto_gray import grayscale_and_threshold
from modules.usida_face_judge import Face_judge

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # ファイルが変更された場合の処理
        if event.is_directory:
            return
        file_path = os.path.relpath(event.src_path)
        print(f"File {file_path} has been modified.")
        process_file(file_path)

    def on_created(self, event):
        # ファイルが作成された場合の処理
        if event.is_directory:
            return
        file_path = os.path.relpath(event.src_path)
        print(f"File {file_path} has been created.")
        process_file(file_path)

def process_file(file_path):
    Canny_img = Canny()
    mosaic_img = apply_mosaic_to_faces()
    grayscale_img = grayscale_and_threshold()
    judge_img = Face_judge()
    
    
if __name__ == "__main__":
    # ディレクトリの監視を開始
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='input_files', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # プログラムがキーボード入力で停止された場合、監視を停止
        observer.stop()
    observer.join()