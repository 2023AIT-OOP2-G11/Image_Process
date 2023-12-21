import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from modules.image_canny import Canny
from modules.mosaic_to_faces import apply_mosaic_to_faces
from modules.usida_face_judge import Face_judge

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        file_path = os.path.relpath(event.src_path)
        print(f"File {file_path} has been modified.")
        process_file(file_path)

    def on_created(self, event):
        if event.is_directory:
            return
        file_path = os.path.relpath(event.src_path)
        print(f"File {file_path} has been created.")
        process_file(file_path)

def process_file(file_path):
    # ここにファイルの処理を書く
    # 例: ファイルを別のディレクトリに保存
    save_path = os.path.join('processed_files', os.path.basename(file_path))
    os.rename(file_path, save_path)
    print(f"File {file_path} has been processed and saved to {save_path}")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='input_files', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
