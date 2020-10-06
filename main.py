import os
import time
import speech_recognition as sr
import pyttsx3
import datetime


engine = pyttsx3.init()
engine.say('Привет, я рад снова тебя видеть')
engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
        print('Вы сказали ' + query)
    except sr.UnknownValueError:
        print('Я вас не понял')
        query = command()
    return query


engine.say(command())
engine.runAndWait()
