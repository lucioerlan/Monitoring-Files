#coding: utf-8
# -*- coding:utf-8 -*-

import sys
import re
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import configs as conf


tempo = 0


#Colors
C = '\033[36m' # cyan
Y = '\033[1;33m' # yellow
W = '\033[0m'  # white
R = '\033[31m' # red




class EventHandler(FileSystemEventHandler):
    
    def catch_all_handler(self, event):
        self.tempo = tempo
        pass


    def on_moved(self, event):
        print("ARCHIVE MOVED " + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('C:/Users/Erlan/Desktop/LOGS/moved/ARCHIVE_MODIFIED.txt', 'a') #LOGS
        arquivo.write(str(conf.get_hora()) + '\n'  + 'ARCHIVE MOVED' + '\n' + str(event) + '\n'+'\n')
        arquivo.close() 


    def on_created(self, event):
        print("ARCHIVE CREATE " + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('C:/Users/Erlan/Desktop/LOGS/create/ARCHIVE_CREATE.txt', 'a') #LOGS
        arquivo.write(str(conf.get_hora()) + '\n'  + 'ARCHIVE CREATE' + '\n' + str(event) + '\n'+'\n')
        arquivo.close() 


    def on_deleted(self, event):
        print("ARCHIVE DELETED " + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('C:/Users/Erlan/Desktop/LOGS/delete/ARCHIVE_DELETE.txt', 'a') #LOGS
        arquivo.write(str(conf.get_hora()) + '\n'  + 'ARCHIVE DELETE' + '\n' + str(event) + '\n'+'\n')
        arquivo.close() 


    def on_modified(self, event): 
        print("ARCHIVE UPDATE " + str(event))
        self.catch_all_handler(event)
        self.tempo = 0
        arquivo = open('C:/Users/Erlan/Desktop/LOGS/update/ARCHIVE_UPDATE.txt', 'a') #LOGS
        arquivo.write(str(conf.get_hora()) + '\n'  + 'ARCHIVE UPDATE' + '\n' + str(event) + '\n'+'\n')
        arquivo.close() 


    def process(self,event):
        fileTocheck = "Version"
        with open(event.src_path+"\\"+fileTocheck) as version:
            chngstring = version.read()
            changeNumber = re.findall(r"\D(\d{5})\D",chngstring)
            if not changeNumber:
                return


events = EventHandler()
observador = Observer()
path = "C:/Users/Erlan/Desktop/VERIFY" #VERIFY FOLDER
observador.schedule(events,path, recursive=False)
observador.start() 
print('\n' + Y + '>> ' + C + 'Service started, reading folder '+path+'' + W)
events.tempo = 0



        # IF FOR 1 HOUR NOT RECEIVING FILES, A MESSAGE FOR SLACK!
try:
    while True:
        time.sleep(1)
        events.tempo = events.tempo + 1
        if events.tempo >= 10:
                print('\n' + R + " YOU HAVE NOT RECEIVED FILES FOR 2 HOURS ! " + W) 
                conf.send_email() #Call methodo send email
                conf.send_slack() #Call methodo send slack
                events.tempo = 0


except KeyboardInterrupt:
    print("")
    observador.stop()
    observador.join()


#__________________________________________________________________________________________#