import telebot
from config import TOKEN, keys
from Extensions import ConvertionException, CurrenciesConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = f'Привет {message.chat.username}! Я бот конвертатор валют. Чтобы начать работу введите команду в следущем ' \
        f'формате: \n<название исходной валюты> \
<в какую валюту перевести> \
<требуемое количество валюты>\nВвод осуществлять с маленькой буквы через пробел, название валюты нужно писать в единственном числе\n' \
           f'Например: рубль доллар 100\nПолучить список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', 1])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        base, quote, amount = values
        total_base = CurrenciesConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
