import requests
from datetime import datetime
import telebot
from token_file import TOKEN

def get_price(crypto='btc'):
    req = requests.get(f'https://yobit.net/api/3/ticker/{crypto}_usd')
    response = req.json()
    crypto_price = round(response[f'{crypto}_usd']['avg'], 2)
    now = datetime.now()
    price = f'{now.strftime("%Y-%m-%d %H:%M")}\nAverage {crypto.upper()} price: {crypto_price}$'
    return price

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, 'Hello, Friend! Write the tiker: \n(Example: "BTC", "btc")')


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        try:
            price = get_price(message.text.lower())
            bot.send_message(
                    message.chat.id,
                    price
                )
        except Exception as e:
            print(e)
            bot.send_message(
                message.chat.id,
                 f'Send only tiker. \nExample("btc", "LTC", "Xrp").'
            )


    bot.polling()


if __name__ == '__main__':

    telegram_bot(TOKEN)
