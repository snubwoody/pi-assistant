import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

#uses google text to speech to write and play an audio file then deletes it

def speak(input:str):
    language = 'en'

    speech = gTTS(text=input,lang=language,slow=False,)
    os.system('rm ./AudioFiles/*')
    speech.save('./AudioFiles/speech.mp3')

    playsound('./AudioFiles/speech.mp3')

    os.system('rm ./AudioFiles/*')

activation_word:str = "computer"

def listen():
    listener = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print('Adjusting for ambient noise')
        listener.adjust_for_ambient_noise(source,2)
        print("Listening")
        speech= listener.listen(source)
        listener.pause_threshold = 1
        print("Audio collected ... \nProccessing speech....")
        try:
            query = listener.recognize_google(speech,language='en_gb')
            print(f'the input speech was:{query}')
            print(type(query))
            return query
        except:
            return None

speak('hi')       


