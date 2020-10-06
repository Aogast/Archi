import os
import time
import speech_recognition as sr
import pyttsx3
import requests
import datetime


engine = pyttsx3.init()
voices = engine.getProperty('voices')
city_id = 0
appid = "86bb2596969f92098deda13aa115e059"


def weather(city):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        return str(data['main']['temp']), data['weather'][0]['description']

    except Exception as e:
        print(1)
        return None


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        talk('Я вас не понял, пожалуйста, повторите')
        query = command()
    return query


def talk(string):
    engine.say(string)
    engine.runAndWait()


while True:
    cmd = command()
    talk(cmd)
    if 'погода' in cmd:
        talk('Уточните город, который вас интересует')
        cmd = command()
        wth = weather(cmd)
        if wth:
            talk('Сейчас в городе ' + cmd + wth[0] + 'градусов по цельсию,' + wth[1])
        else:
            talk('Я не расслышал название города')
            talk('Повторите пожалуйста')
    elif cmd == 'пока':
        talk('Приятно было поболтать')
        exit()
