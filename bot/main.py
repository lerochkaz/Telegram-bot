import telebot
from config import TOKEN
import random
import workFile
bot = telebot.TeleBot(TOKEN)


# Домашнее задание


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рассказать анекдот')
    item2 = telebot.types.KeyboardButton('Сделать комплимент')
    item3 = telebot.types.KeyboardButton('Знаки зодиака')
    item4 = telebot.types.KeyboardButton('Угадайка')

    markup.add(item1, item2, item3, item4)

    bot.send_message(
        message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)


@bot.message_handler(commands=['text'])
def zodiacButtons(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    item_1 = telebot.types.InlineKeyboardButton(
        'Овен', callback_data='Овен')
    item_2 = telebot.types.InlineKeyboardButton(
        'Телец', callback_data='Телец')
    item_3 = telebot.types.InlineKeyboardButton(
        'Близнецы', callback_data='Близнецы')
    item_4 = telebot.types.InlineKeyboardButton(
        'Рак', callback_data='Рак')
    item_5 = telebot.types.InlineKeyboardButton(
        'Лев', callback_data='Лев')
    item_6 = telebot.types.InlineKeyboardButton(
        'Дева', callback_data='Дева')
    item_7 = telebot.types.InlineKeyboardButton(
        'Весы', callback_data='Весы')
    item_8 = telebot.types.InlineKeyboardButton(
        'Скорпион', callback_data='Скорпион')
    item_9 = telebot.types.InlineKeyboardButton(
        'Стрелец', callback_data='Стрелец')
    item_10 = telebot.types.InlineKeyboardButton(
        'Козерог', callback_data='Козерог')
    item_11 = telebot.types.InlineKeyboardButton(
        'Водолей', callback_data='Водолей')
    item_12 = telebot.types.InlineKeyboardButton(
        'Рыбы', callback_data='Рыбы')
    markup.add(item_1, item_2, item_3, item_4, item_5, item_6,
               item_7, item_8, item_9, item_10, item_11, item_12)
    bot.send_message(
        message.chat.id, 'Выбрать знак зодиака', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inLine(call):
    signInDictionary = workFile.printSignZodiac()
    if call.data == 'Овен':
        bot.send_message(call.message.chat.id, signInDictionary['Овен'])
    elif call.data == 'Телец':
        bot.send_message(call.message.chat.id, signInDictionary['Телец'])
    elif call.data == 'Близнецы':
        bot.send_message(call.message.chat.id, signInDictionary['Близнецы'])
    elif call.data == 'Рак':
        bot.send_message(call.message.chat.id, signInDictionary['Рак'])
    elif call.data == 'Лев':
        bot.send_message(call.message.chat.id, signInDictionary['Лев'])
    elif call.data == 'Дева':
        bot.send_message(call.message.chat.id, signInDictionary['Дева'])
    elif call.data == 'Весы':
        bot.send_message(call.message.chat.id, signInDictionary['Весы'])
    elif call.data == 'Скорпион':
        bot.send_message(call.message.chat.id, signInDictionary['Скорпион'])
    elif call.data == 'Стрелец':
        bot.send_message(call.message.chat.id, signInDictionary['Стрелец'])
    elif call.data == 'Козерог':
        bot.send_message(call.message.chat.id, signInDictionary['Козерог'])
    elif call.data == 'Водолей':
        bot.send_message(call.message.chat.id, signInDictionary['Водолей'])
    else:
        bot.send_message(call.message.chat.id, signInDictionary['Телец'])


def numberGeneration(mess):
    number = random.randint(1, 5)
    print(number)
    if mess.text == str(number):
        bot.send_message(
            mess.chat.id, f'Число отгадано верно "{number}", молодец!')
    else:
        bot.send_message(mess.chat.id, 'Не отгадал!')


@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text == 'привет':
        bot.send_message(
            message.chat.id, 'Привет, как дела?')
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAEHJuZjuJviFGZqPA6429xeLO_UjVNEjQACWgUAAj-VzAobFrmFvSDDnS0E')
    elif message.text == 'Рассказать анекдот':
        bot.send_message(
            message.chat.id, str(workFile.printAnecdote()))
    elif message.text == 'Сделать комплимент':
        bot.send_message(
            message.chat.id, str(workFile.printCompliments()))
    elif message.text == 'Знаки зодиака':
        zodiacButtons(message)
    elif message.text == 'Угадайка':
        mess = bot.send_message(
            message.chat.id, 'Я загадал число от 1 до 5, попробуй отгадать')
        bot.register_next_step_handler(mess, numberGeneration)
    else:
        bot.send_message(
            message.chat.id, 'Данный функционал находится в разработке')


bot.polling(none_stop=True)
