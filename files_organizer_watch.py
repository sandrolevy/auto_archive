from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime
import folders_tree
import files_organizer

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
       files_organizer.scan_folders()
        

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
