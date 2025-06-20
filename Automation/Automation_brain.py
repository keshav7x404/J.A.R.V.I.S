import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Automation.open_App import open_App
from Automation.Web_Open import openweb
import pyautogui as gui
from Automation.Play_Music_YT import play_music_on_youtube
from Automation.Play_Music_Sfy import play_music_on_spotify
from TextToSpeech import Fast_DF_TTS


def close():
    gui.hotkey('alt','f4')

def Open_Brain(text):
    if "website" in text or "open website named" in text:
        text = text.replace("open", "").strip()
        text = text.replace("website", "").strip()
        text = text.replace("open website named", "").strip()
        openweb(text)
    else:
        text = text.replace("open", "").strip()
        text = text.replace("app", "").strip()
        open_App(text)





def Auto_main_brain(text):
    try:
        if text.startswith("open"):
            Open_Brain(text)
        
        elif "close" in text:
            close()
        
        elif "play album" in text or "play music on youtube" in text:
            Fast_DF_TTS.speak("Which album do you want to play, sir?")
            x = input()
            play_music_on_youtube(x)
        
        elif "play some music" in text or "play music on spotify" in text:
            Fast_DF_TTS.speak("Which song do you want to play, sir?")
            x = input()
            play_music_on_spotify(x)
        
        else:
            pass

    except Exception as e:
        print(f"Error: {e}")

#to check if its running , uncomment these lines
# while True:
#     x=input("x :")
#     Auto_main_brain(x)
      
    
    
        


