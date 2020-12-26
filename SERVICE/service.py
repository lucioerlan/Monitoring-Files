#coding: utf-8
# -*- coding:utf-8 -*-

import os
import re
import time
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Extras.sendLogs import send_slack, send_email, get_hora
from Customs.style import style
load_dotenv()


class service(FileSystemEventHandler):
    
    def catch_all_handler(self, event):
        self.tempo = tempo
    pass
    
    def on_created(self,event):
        print("ARCHIVE CREATE" + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('Logs/create/ARCHIVE_CREATE.txt', 'a') #LOGS
        arquivo.write(str(get_hora()) + str(event) + '\n')
        arquivo.close()

    def on_moved(self,event):
        print("ARCHIVE MOVED" + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('Logs/ARCHIVE_MODIFIED.txt', 'a') #LOGS
        arquivo.write(str(get_hora()) + str(event) + '\n')
        arquivo.close()

    def on_modified(self,event):
        print("ARCHIVE UPDATE" + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('Logs/changed/ARCHIVE_UPDATE.txt', 'a') #LOGS
        arquivo.write(str(get_hora()) + str(event) + '\n')
        arquivo.close()

    def on_deleted(self,event):
        print("ARCHIVE DELETED" + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('Logs/delete/ARCHIVE_DELETE.txt', 'a') #LOGS
        arquivo.write(str(get_hora()) + str(event) + '\n')
        arquivo.close()

    def process(self,event):
        fileTocheck = "Version"
        with open(event.src_path+"\\"+fileTocheck) as version:
            chngstring = version.read()
            changeNumber = re.findall(r"\D(\d{5})\D", chngstring)
            if not changeNumber:
                return


path = os.getenv("PATH-MONITOR")  # PATH MONITOR FOLDER
events = service()
observador = Observer()
observador.schedule(events, path, recursive=False)
observador.start()
tempo = 0
events.tempo = 0
print(style.OKGREEN + 'Service started, Reading Folder '+path+'' + style.ENDC)



# If, every 10 Seconds the folder not receive Changes, a log is Sent!
try:
    while True:
        time.sleep(1)
        events.tempo = events.tempo + 1
        if events.tempo >= 10:
            print(style.FAIL + "YOU HAVE NOT RECEIVED FILES FOR 10 SECONDS!" + style.ENDC)
            send_email()  # Call send email
            send_slack()  # Call send slack
            events.tempo = 0

except KeyboardInterrupt:
    print(style.OKBLUE + 'Program Ended!' + style.ENDC)

