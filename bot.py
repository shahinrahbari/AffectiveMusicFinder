import json 
import requests

import time
from six.moves import urllib

from database import DBHelper

from emoji import emojize

from random import randint

import songsWords


def pick_random_song(list_of_songs):
    random_number = randint(0,2)
    return list_of_songs[random_number][1]
    


TOKEN = "302407166:AAEPZDxQDrQ-HMy15-8wJBKh7iWEOdNjZig"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    update_id = updates["result"][last_update]["update_id"]
    return (text, chat_id,update_id)



def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

   


def send_audio(chat_id,file_id):
    url = URL + "sendaudio?chat_id={}&audio={}".format(chat_id,file_id)
    get_url(url)


def get_song_info(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    song_id = updates["result"][last_update]["message"]["file_id"]
    song_title = updates["result"][last_update]["message"]["title"]
    song_performer = updates["result"][last_update]["message"]["performer"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (song_id,song_title,song_performer,chat_id)


def main():
    last_update_id = None
    
    foundSong = False    
    while True:

        text, chat, update_id = get_last_chat_id_and_text(get_updates())
        if update_id != last_update_id:
            for c in songsWords.list_of_sad_words:
                if (c in text):
                    send_message("Don't feel sad buddy",chat)
                    send_audio(chat,pick_random_song(songsWords.list_of_sad_songs))
                    foundSong = True
            
            for c in songsWords.list_of_happy_words:
                if (c in text):
                    send_message("Let's listen to some happy music",chat)
                    send_audio(chat,pick_random_song(songsWords.list_of_happy_songs))
                    foundSong = True
            for c in songsWords.list_of_angry_words:
                if (c in text):
                    send_message("Some metals just in time \0/",chat)
                    send_audio(chat,pick_random_song(songsWords.list_of_angry_songs))
                    foundSong = True
            for c in songsWords.list_of_romantic_words:
                if (c in text):
                    send_message("How about some romantic songs",chat)
                    send_audio(chat,pick_random_song(songsWords.list_of_romantic_songs))
                    foundSong = True
            for c in songsWords.list_of_calm_words:
                if (c in text):
                    send_message("Let's chill down",chat)
                    send_audio(chat,pick_random_song(songsWords.list_of_calm_songs))
                    foundSong = True

            if(not foundSong):    
                send_message("Sorry no song found :(", chat)
            last_update_id = update_id
        time.sleep(0.5)


if __name__ == '__main__':
    main()


    

    











    