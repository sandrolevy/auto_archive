from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime
from Modules import folders_tree

class MyHandler(FileSystemEventHandler):
    def move_file(self):
        folder_to_track = folders_tree.folder_to_track()
        extensions_folders = folders_tree.folders()
        os.chdir(folder_to_track)
        for filename in os.listdir(folder_to_track):
            try:
                extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                path = extensions_folders[extension]
                if not os.path.exists(path):
                    os.makedirs(path)
                shutil.move(filename, path + '/' + filename)
            except Exception:
                extension = 'noname'
    def on_modified(self, event):
        self.move_file()

extensions_folders = folders_tree.folders()
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folders_tree.folder_to_track(), recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
