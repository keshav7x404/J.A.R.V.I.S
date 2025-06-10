# Required Libraries
# pip install SpeechRecognition mtranslate colorama pyaudio

import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init
import os

# Auto-reset colors
init(autoreset=True)

def Translate_hindi_to_english(text):
    try:
        english_text = translate(text, "en")
        return english_text
    except Exception as e:
        return f"Translation Error: {e}"

def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    
    # Tweaked recognizer settings
    recognizer.pause_threshold = 0.5
    recognizer.non_speaking_duration = 0.3

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.GREEN + "Listening...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                print(Fore.YELLOW + "Processing...")

                # Recognize and lower the input
                recognizer_text = recognizer.recognize_google(audio, language='hi-IN').lower()

                if recognizer_text:
                    translated_text = Translate_hindi_to_english(recognizer_text)
                    print(Fore.BLUE + f"\nKeshav (translated): {translated_text}\n")
                else:
                    print(Fore.RED + "Didn't catch that.")
            except sr.UnknownValueError:
                print(Fore.RED + "Could not understand audio.")
            except sr.RequestError as e:
                print(Fore.RED + f"Could not request results; {e}")
            except KeyboardInterrupt:
                print(Fore.LIGHTRED_EX + "\nExiting...")
                break

if __name__ == "__main__":
    Speech_To_Text_Python()
 