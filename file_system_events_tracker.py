import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Event Hander Class
class FileEventHandler(FileSystemEventHandler) :

   def on_created(self, event) :
    print(f"Hey, {event. src_path} has been created!")
   def on_deleted(self, event) :
    print(f"oops! Someone deleted {event. src_path}!")
   def on_modified(self, event) :
    print(f"hi, {event. src_path} has modified!")
    def on_moved(self, event) :
        print(f"hlo! the file {event. src_path} was moved!")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stop")
    observer.stop()
