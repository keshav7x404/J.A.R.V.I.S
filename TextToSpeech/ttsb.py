import requests
import playsound  # pip install playsound==1.2.2
import os
from typing import Union

def generate_audio(message: str, voice: str = "Brian"):
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        result = requests.get(url=url, headers=headers)
        if result.status_code == 200:
            return result.content
        else:
            print(f"Failed to fetch audio. Status code: {result.status_code}")
            return None
    except Exception as e:
        print("Error during API request:", e)
        return None

def speak(message: str, voice: str = "Brian", folder: str = "", extension: str = ".mp3") -> Union[None, str]:
    try:
        result_content = generate_audio(message, voice)
        if result_content is None:
            print("Audio generation failed.")
            return "Failed to generate audio."

        file_path = os.path.join(folder, f"{voice}{extension}")
        with open(file_path, "wb") as file:
            file.write(result_content)

        playsound.playsound(file_path)
        os.remove(file_path)
    except Exception as e:
        print("Error during speech playback:", e)

# Test
speak("hello sir, I am Jarvis")
speak("hey sir, I am Jarvis")
# import requests
# from playsound import playsound#pip install playsound==1.2.2
# import os
# from typing import Union

# def generate_audio(message:str,voice:str="Brian"):
#     url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"
#     headers = {'User-Agent':'Mozilla/5.0(Maciontosh;interl Mac OS X 10_15_7)AppleWebKit/537.36(KHTML,likeGecoko)Chrome/119.0.0.0 Safari.537.36'}

#     try:
#         result =requests.get(utl=url, headers=headers)
#         return result.content
#     except:
#         return None

# def speak(message : str, voice: str="Brian", folder:str="", extension:str =".mp3") -> Union[None,str]:
#     try:
#         result_content =generate_audio(message,voice)
#         file_path = os.path.join(folder,f"{voice}{extension}")
#         with open(file_path,"wb") as file:
#             file.write(result_content)
#         playsound(file_path)
#         os.remove(file_path)
#         return None
#     except Exception as e:
#         print(e)

# speak("hello sir,I m jarvis")