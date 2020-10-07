import speech_recognition as sr
import pyttsx3
import requests
from pygame import mixer
from yandex_music.client import Client


mixer.init()
mail, password = input().split()
client = Client.from_credentials(mail, password)
for i in range(len(list(client.users_likes_tracks()))):
    client.users_likes_tracks()[i].track.download(str(i) + '.mp3')
number = 0
music_flag = 0
music_pause_flag = 0
engine = pyttsx3.init()
voices = engine.getProperty('voices')
volume = 0.1
city_id = 0
appid = "86bb2596969f92098deda13aa115e059"


def weather(city):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'units': 'metric',
                                   'lang': 'ru', 'APPID': appid})
        data = res.json()
        return str(data['main']['temp']), data['weather'][0]['description']

    except Exception:
        print(1)
        return None


def command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=10)
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
    cmd = command().lower()
    print(cmd)
    if 'погода' in cmd:
        talk('Уточн ите город, который вас интересует')
        cmd = command().lower()
        wth = weather(cmd)
        if wth:
            talk('Сейчас в городе ' + cmd + wth[0] + 'градусов по цельсию,' + wth[1])
        else:
            talk('Я не расслышал название города')
            talk('Повторите пожалуйста')
    elif 'включи музыку' in cmd and music_flag == 0:
        mixer.music.load(str(number) + '.mp3')
        mixer.music.play()
        music_flag = 1
    elif 'прекрати играть' in cmd or 'пауз' in cmd and music_flag:
        mixer.music.pause()
        music_pause_flag = 1
    elif 'продолжи' in cmd and music_pause_flag == 1:
        mixer.music.unpause()
        music_pause_flag = 0
    elif 'далее' in cmd or 'дальше' in cmd or 'следующ' in cmd:
        number += 1
        mixer.music.load(str(number) + '.mp3')
        mixer.music.play()
    elif 'предыдущ' in cmd and number:
        number -= 1
        mixer.music.load(str(number) + '.mp3')
        mixer.music.play()
    elif cmd == 'пока':
        talk('Приятно было поболтать')
        exit()


