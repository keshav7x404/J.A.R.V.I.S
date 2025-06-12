import webbrowser
import pyautogui as ui
import time


def play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(5)
    ui.hotkey("ctrl","k")
    time.sleep(2)
    ui.write(song_name)
    time.sleep(1)
    ui.press("enter")
    time.sleep(4)
    ui.leftClick(540,550)
   
