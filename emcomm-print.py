#import dependencies
import time
import os
import shutil
import time
import configparser

config = configparser.ConfigParser()
config.read("config.txt")
incoming_dir = config.get("emcomm-print", "incoming_dir")
processed_dir = config.get("emcomm-print", "processed_dir")

while True:
    files = os.listdir(incoming_dir)
    for file in files:
        filepath = incoming_dir + file
        os.startfile(filepath,"print")
        time.sleep(7)

        destination_file = processed_dir + file
        shutil.move(filepath, destination_file)

    time.sleep(1)
