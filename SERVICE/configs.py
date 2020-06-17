#coding: utf-8
# -*- coding:utf-8 -*-

import sys
import requests
import slack
from datetime import datetime
import yagmail

#Colors
C = '\033[36m' # cyan
Y = '\033[1;33m' # yellow
W = '\033[0m'  # white


#SLACK
def send_slack():
    url = 'https://slack.com/api/chat.postMessage?&text='
    data = {
        'token': "xoxb-774183402898-786504017076-01010101010101010101", #Token Slack
        'channel': 'CNT010101',  # ID Channel Slack
        'as_user': True,
        'username': '@ToraBot',
        
    }
    requests.post(url + get_hora() +'\n' +'*`YOU HAVE NOT RECEIVED FILES FOR 2 HOURS ! `*  😟   '+'\n', data)


#EMAIL
def send_email():
    receiver_emails = ['sendemail@hotmail.com'] #Email-s From Send
    subject = get_hora()    
    yag=yagmail.SMTP("youemail@gmail.com","01010101") #You Login Gmail
    #Body Message
    contents = [
    '  <b> <font color="#FF1493" size="10">  YOU HAVE NOT RECEIVED FILES FOR 2 HOURS 	😟   </font>  </b>',
    ]
    yag.send(receiver_emails, subject, contents)


#DATA HOUR NOW
def get_hora():
    return datetime.now().strftime("%d-%m-%Y %H-%M-%S")  



#__________________________________________________________________________________________#