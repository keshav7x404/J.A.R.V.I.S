import requests
from win10toast import ToastNotifier
from TextToSpeech.Fast_DF_TTS import speak
import time
import threading

import random


def alert(text):
    toaster = ToastNotifier()
    toaster.show_toast(
        "JARVIS",
        text,
        duration=1,  
        icon_path=None,
        threaded=True
    )
    while toaster.notification_active():
        time.sleep(0.1)

def is_Online(url = "https://www.google.com",timeout=5):
    try:
        response =requests.get(url,timeout=timeout)
        return response.status_code >= 200 and response.status_code<300
    except requests.ConnectionError:
        return False
    
# def internet_status():
#     if is_Online():
#         t1=threading.Thread(target=speak,args=(ran_online_dlg,))
#         t2=threading.Thread(target=alert,args=(ran_online_dlg,))
#         t1.start()
#         t2.start()
#         t1.join()
#         t2.join()
#         return(ran_online_dlg)
#     else:
#         alert(ran_offine_dlg)
#         return(ran_offine_dlg)
