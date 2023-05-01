import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(massage: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<колличество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(massage, text)

@bot.message_handler(commands=['values'])
def values(massage: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(massage, text)

@bot.message_handler(content_types=['text', ])
def convert(massage: telebot.types.Message):
    try:
        values = massage.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много или слишком мало параметров')

        guote, base, amount = values
        total_base = CryptoConverter.convert(guote, base, amount)
    except ConvertionException as e:
        bot.reply_to(massage, f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(massage, f'Не удалось обработать команду\n {e}')
    else:
        text = f'Цена {amount} {guote} в {base} - {total_base}'
        bot.send_message(massage.chat.id, text)




bot.polling()




