#1.0 версия

import datetime
import subprocess
import os
import asyncio
import string
import sys
import requests
import random
from typing import Any, Text
import vk_api
from random import choice
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token="youtokenhere")  # Токен твоего бота
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, clubid) # ID Сообщества
admins = [admin1, admin2] # Админ-лист


def send_msg(peer_id: int, message: str, attachment: str = ""):
    return vk.method("messages.send", {**locals(), "random_id": 0})


        
while True: # Чтоб бот не падал при пропадании тырнета
    try:        
        for event in longpoll.listen():
           if event.type == VkBotEventType.MESSAGE_NEW:
               if event.message.peer_id != event.message.from_id:
                   if event.message.text.startswith("/"): # С чего начинается команда
                        cmd = event.message.text[1:] # Сколько символов обрезать,у нас 1 здесь, если юзать /cmd то нужно 4, принцип как бы понятен
                        if event.message.from_id in admins: # Проверяет админа у пользователя
                            send_msg(event.message.peer_id,choice("Message1,Message2,Message3,Message4)".split(",")))  # Реплики бота при подключении к cmd
                            command=cmd+"> tmp.txt" # Кэш-файлы, вообще есть либа для перехвата того, что программа пукает, сами найдете
                            os.system(command)
                            file=open('tmp.txt','r+')
                            oppenedfile=file.read()
                            send_msg(event.message.peer_id, message=(f"{oppenedfile}"))
                            file.close()
                            os.system("rm tmp.txt")
                        else:
                            send_msg(event.message.peer_id, message=(f"Вас нет в админ-листе бота.")) # Сообщение если не нашло в списке админов
           
    except Exception as e:
        print(repr(e)) # Спаситель бота
