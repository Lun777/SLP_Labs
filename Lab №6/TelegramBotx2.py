# -*- coding: utf-8 -*-

import telebot
import sqlite3
import sys
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

API = '6931360555:AAH07vHQ-Y-VIg829Zfdl3Ikon7WHyx5qgw'

bot = telebot.TeleBot(API)

global correct_answer

# 136 teams

def listToStr(line_up):
    squad = ""
    for team in line_up:
        for i in team:
            squad += i
            if i != line_up[len(line_up) - 1]:
                squad += '\n'
    return squad

def gen_markup(list):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(list[0], callback_data=list[0]),
                               InlineKeyboardButton(list[1], callback_data=list[1]),
               InlineKeyboardButton(list[2], callback_data=list[2]),
                               InlineKeyboardButton(list[3], callback_data=list[3]))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == correct_answer:
        bot.send_message(call.message.chat.id, "Ответ правильный. Ты молодец!")
    else:
        bot.send_message(call.message.chat.id, "Ответ неверный")

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет!\nДля получения состава одной из команд по Dota 2 введите её название.\nДля прохождения теста введите /play .')

@bot.message_handler(commands=['play'])
def get4AnswersAndOneOfThemIsCorrect(message):
    conn = sqlite3.connect('Dota2.sql')
    cur = conn.cursor()
    squad = cur.execute("SELECT Name, Player1, Player2, Player3, Player4, Player5 FROM teams WHERE Player5 IS NOT NULL ORDER BY RANDOM() LIMIT 1")
    squad = list(list(squad)[0])
    team = squad[0]
    text = squad[0]
    squad.remove(text)
    text += '\n'
    for i in range(4):
        random_element = random.choice(squad)
        text += ('\n' + random_element)
        squad.remove(random_element)
    global correct_answer
    correct_answer = squad[0]
    text += ('\n' + '\n' + "Какого игрока не хватает в этой команде?")
    squadx2 = cur.execute("SELECT Name, Player1, Player2, Player3, Player4, Player5 FROM teams WHERE Player5 IS NOT NULL AND Name != '%s' ORDER BY RANDOM() LIMIT 3" % team)
    squadx2 = list(squadx2)
    cur.close()
    conn.close()
    i = 0
    while i < 3:
        temp = list(list(squadx2)[i])
        temp.pop(0)
        random_element = random.choice(temp)
        squad.append(random_element)
        i += 1
    random.shuffle(squad)
    bot.send_message(message.chat.id, text, reply_markup=gen_markup(squad))

@bot.message_handler(content_types=['text'])
def DotaTeams(message):
    conn = sqlite3.connect('Dota2.sql')
    cur = conn.cursor()
    # line_up = list()
    try:
        line_up = cur.execute("SELECT Player1, Player2, Player3, Player4, Player5 FROM teams WHERE Name = '%s'" % (message.text))
        line_up = list(line_up)
        cur.close()
        conn.close()
        squad = listToStr(line_up)
        bot.send_message(message.chat.id, squad)
    except:
        bot.send_message(message.chat.id, "Такой команды не существует")

bot.polling()