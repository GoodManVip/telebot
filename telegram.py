import telebot
from telebot import apihelper
import requests # Модуль для обработки URL
import time # Модуль для остановки программы
from telebot import types
import time

from pycbrf.toolbox import ExchangeRates
a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
cur_time=a.split('-')[0]+'-'+a.split('-')[1]+'-'+a.split('-')[2]
print(cur_time)

class users():
    def new(id_user):
        a=open('users.db')
        dump=a.read()
        a.close()
        a=open('users.db','w')
        a.write(dump+'\n')
        a.write(str(id_user))
        print('New user succeful added to db')
    
    
# Запрашиваем данные на 26-е июня.
rates = ExchangeRates(cur_time)

rates.date_requested  # 2016-06-26 00:00:00
rates.date_received  # 2016-06-25 00:00:00
# 26-е был выходной, а курс на выходные установлен 25-го
rates.dates_match  # False

bot = telebot.TeleBot('917894932:AAEiMHPRsBB5SquDTQlW77yG2GyghtQ-3EA');

apihelper.proxy = {
    'http': 'http://177.87.39.104:3128',
    'https': 'https://177.87.39.104:3128',
    # Замените на данные своего proxy
}
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Я бот Тихона показывающий курсы валют!\nТипы валют которые я могу отобразить:\n1. Доллар (Чтобы узнать напиши: /dol)\n2. Евро (Чтобы узнать напиши: /eu\n3. Юань (Чтобы узнать напиши: /cny))\n1. Турецкая лира (Чтобы узнать напиши: /try)\n Также просьба зарегистрировать аккаунт: /reg")
    elif message.text == '/america' or message.text == '/dol' or message.text == '/usd':
        course1=float(rates['USD'].value)
        course=('{0:.1f}'.format(course1))
        print('Кто-то восрользовался рограммой с id:'+str(message.from_user.id))
        print(course)
        bot.send_message(message.from_user.id, "На данный момент придятся отдать за 1 доллар: "+str(course)+' рублей!')
    elif message.text == '/eu' or message.text == '/eur' or message.text == '/euro':
        course1=float(rates['EUR'].value)
        course=('{0:.1f}'.format(course1))
        print('Кто-то восрользовался рограммой с id:'+str(message.from_user.id))
        print(course)
        bot.send_message(message.from_user.id, "На данный момент придятся отдать за 1 евро: "+str(course)+' рублей!' )
    elif message.text == '/cny' or message.text == '/china' or message.text == '/uyan':
        course1=float(rates['CNY'].value)
        course=('{0:.1f}'.format(course1))
        print('Кто-то восрользовался рограммой с id:'+str(message.from_user.id))
        print(course)
        bot.send_message(message.from_user.id, "На данный момент придятся отдать за 1 юань: "+str(course)+' рублей!')
    elif message.text == '/try' or message.text == '/turk' or message.text == '/turkey':
        course1=float(rates['TRY'].value)
        course=('{0:.1f}'.format(course1))
        print('Кто-то восрользовался рограммой с id:'+str(message.from_user.id))
        print(course)
        bot.send_message(message.from_user.id, "На данный момент придятся отдать за 1 турецкую лиру: "+str(course)+' рублей!')
    elif message.text == '/reg':
        users.new(str(message.from_user.id))
        bot.send_message(message.from_user.id, "Вы успешно были добавленны в базу данных!")
    else:
        bot.send_message(message.from_user.id, "Неизвестная команда. Напиши /start.")

bot.polling(none_stop=True, interval=0)

