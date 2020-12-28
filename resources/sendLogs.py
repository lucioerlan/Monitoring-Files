#coding: utf-8
# -*- coding:utf-8 -*-

from datetime import datetime
from dotenv import load_dotenv
import requests
import yagmail
import os
load_dotenv()


class sendLogs:pass

def send_slack():
    url = 'https://slack.com/api/chat.postMessage?&text='
    data = {
        'token': os.getenv("TOKEN-SLACK"),  # Token Slack
        'channel': os.getenv("CHANNEL-SLACK"),  # ID Channel Slack
        'as_user': True,
    }
    requests.post(url + get_hora() + '\n' + '*`YOU HAVE NOT RECEIVED FILES FOR 10 SECONDS ! `*  😟 '+'\n', data)


def send_email():
    receiver_emails = [os.getenv("SEND-EMAIL")]  # Email Send
    subject = get_hora()
    yag = yagmail.SMTP(os.getenv("EMAIL-GMAIL"),  os.getenv("PASSWORD-GMAIL"))  # You Login Gmail
    
    # Body Message
    contents = [
        '  <b> <font color="#FF1493" size="10">  YOU HAVE NOT RECEIVED FILES FOR 10 SECONDS 😟 </font>  </b>',
    ]
    yag.send(receiver_emails, subject, contents)


def get_hora():
    return datetime.now().strftime("%d-%m-%Y %H-%M-%S")
