import os
import telebot

channel = '-XXXXXXXXX'
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bot = telebot.TeleBot(token)
ip = ["10.5.110.55", "10.5.109.151", "10.5.110.56"]
#ip = ['google.com', 'yandex.ru', 'facebook.com']

for val in ip:
    response = os.system('ping -c 1 ' + val)
    if response == 0:
        print(val + ' is up!')
        bot.send_message(channel, val + ' is up')
    else:
        print(val + ' is down!')
        bot.send_message(channel, val + ' is down!')
