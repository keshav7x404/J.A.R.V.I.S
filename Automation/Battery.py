import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import psutil
# import time
# from plyer import notification

# def alert100():
#     notification.notify(
#         title="Battery Alert 🔋",
#         message="Battery is 100% charged. Please unplug the charger.",
#         timeout=5
#     )

# def battery_alert():
#     while True:
#         battery = psutil.sensors_battery()
#         percentage = int(battery.percent)

#         if percentage == 100:
#             alert100()
#             break  # Remove this if you want it to alert repeatedly

#         time.sleep(60)  # Check every 60 seconds

# if __name__ == "__main__":
#     notification.notify(
#         title="Jarvis🔋",
#         message="You will be notified when the battery is fully charged.",
#         timeout=3
#     )
#     battery_alert()
import time
from win10toast import ToastNotifier
import psutil
from TextToSpeech.Fast_DF_TTS import speak
import threading
def alert100():
    toaster = ToastNotifier()
    toaster.show_toast(
        "JARVIS",
        "100% charged. Please unplug it",
        duration=1,  
        icon_path=None,
        threaded=True
    )
    while toaster.notification_active():
        time.sleep(0.1)

def battery_Alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)
        if percentage == 100:
            t1=threading.Thread(target=alert100)
            t2=threading.Thread(target=speak,args=("100% charged. Please unplug it.",))
            
            t1.start()
            t2.start()
            t1.join()
            t2.join()

            break  # Optional: prevents repeated alerts

battery_Alert()
