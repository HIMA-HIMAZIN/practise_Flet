import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.start_app()

    def start_app(self):
        if self.process:
            self.process.terminate()  # 既存のプロセスを終了
        print("Starting app...")
        self.process = subprocess.Popen(["python", self.script_name])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"File {event.src_path} changed, restarting app...")
            self.start_app()

if __name__ == "__main__":
    script_name = "main.py"  # 実行するFletアプリのファイル名
    event_handler = ReloadHandler(script_name)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()
    print(f"Watching for changes in {script_name}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
