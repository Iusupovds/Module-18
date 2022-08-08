import telebot
import requests
import json


TOKEN = '5593276120:AAEFzAOyDKeCdanV2ukuZApIMmk7xj7rFqo'


bot = telebot.Telebot(TOKEN)


keys = {
    'доллар США': 'USD',
    'евро': 'EUR',
    'фунт стерлингов': 'GBR',
    'юань': 'CNY',
    'рубль': 'RUB',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следущем формате: \n<имя валюты> \ 
<в какую валюту перевести> \ 
<количество переводимой валюты>\nПолучить список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', 1])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    


bot.polling()
