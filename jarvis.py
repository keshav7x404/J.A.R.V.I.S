import threading
from internet_check import is_Online,alert
from Data.DLG_data import offline_dlg,online_dlg
import random
from co_brain import Jarvis
from TextToSpeech.Fast_DF_TTS import speak

ran_online_dlg = random.choice(online_dlg)
ran_offine_dlg = random.choice(offline_dlg)

def main():
    if is_Online():
        t1=threading.Thread(target=speak,args=(ran_online_dlg,))
        t2=threading.Thread(target=alert,args=(ran_online_dlg,))
        t2=threading.Thread(target=alert,args=(ran_online_dlg,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        Jarvis()
    else:
        alert(ran_offine_dlg)

main()
