#coding: utf-8
# -*- coding:utf-8 -*-

import os
import sys
import time

#Colors
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
B = '\033[;1m' # black
M = '\033[1;35m' # Magento


class funcoes:

    def __init__(self):
        time.sleep(1)
    
        
    def banner(self):
        os.system('cls')
        version = '0.0.2'
        print ('\n' + M +
        r'''
        
    ___██__________██
    ___█▒█________█▒█
    __█▒███____███▒█
    __█▒████████▒▒█
    __█▒████▒▒█▒▒██
    __████▒▒▒▒▒████
    ___█▒▒▒▒▒▒▒████
    __█▒▒▒▒▒▒▒▒████______█
    _██▒█▒▒▒▒▒█▒▒████__█▒█                      _____ ___  _     ____  _____ ____  
    _█▒█●█▒▒▒█●█▒▒███_█▒▒█                      |  ___/ _ \| |   |  _ \| ____|  _ \ 
    _█▒▒█▒▒▒▒▒█▒▒▒██_█▒▒█                       | |_ | | | | |   | | | |  _| | |_) |
    __█▒▒▒=▲=▒▒▒▒███_██▒█                       |  _|| |_| | |___| |_| | |___|  _ <
    __██▒▒█♥█▒▒▒▒███__██▒█                      |_|   \___/|_____|____/|_____|_| \_\
    ____███▒▒▒▒████____█▒█            __  __  ___  _   _ ___ _____ ___  ____  ___ _   _  ____ 
    ______██████________███           |  \/  |/ _ \| \ | |_ _|_   _/ _ \|  _ \|_ _| \ | |/ ___|
    _______█▒▒████______██            | |\/| | | | |  \| || |  | || | | | |_) || ||  \| | |  _ 
    _______█▒▒▒▒▒████__██             | |  | | |_| | |\  || |  | || |_| |  _ < | || |\  | |_| |
    _______█▒██▒██████▒█              |_|  |_|\___/|_| \_|___| |_| \___/|_| \_\___|_| \_|\____|
    _______█▒███▒▒▒█████
    _____█▒████▒▒▒▒████
    ______█▒███▒██████__
        ''' + W)
        print('\n' + G + '[>]' + C + ' Created By : ' + W + 'Erlan Lucio')
        print(G + '[>]' + C + ' Version    : ' + W + version + '\n')
        
        
    def chooseDep(self):   

        condition = True
        while (condition is True): 
            install = input( B +'Install Dependencies? [Y/n]: ' + W)
            if (install == 'Y'):
                os.system('pip install -r requirements.txt')
                print(C + 'Libraries installed successfully!' + W)
                time.sleep(3)
                condition = False
            elif(install == 'n'):
                condition = False



    def displaysMenu(self):            
        os.system('cls')
        print('\n' + G + 'Start Monitoring:' + W + '\n' +
        '''
        [1]:Monitoring Folder Test 
        [0]:End
        ''')



    def chooseOption(self): 
     try:        
        while True:
            choice = input(R + '[X]' + W + ' Select> ')
            if choice == '1':
                os.system('python ./SERVICE/monitoring_folder.py')
            if choice == '0':
                print('\n' +  R + 'Successfully logged out!!'+ W)
                exit(0)
  
                
     except KeyboardInterrupt:
                print('\n\n\n\n'  +  R + 'Monitoring Aborted!'+ W)

# _______________________________________________________________________________________#





