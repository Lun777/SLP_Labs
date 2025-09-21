# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import telebot
import sqlite3
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

API = '6931360555:AAH07vHQ-Y-VIg829Zfdl3Ikon7WHyx5qgw'
def getTeams():
    URL = "https://liquipedia.net/dota2/Portal:Teams"
    rq = requests.get(URL)
    soup = bs(rq.content, "html.parser")
    teams = soup.find_all('span', class_='team-template-text')
    teams = [team.get_text().strip() for team in teams]
    return teams

teams = getTeams()

# conn = sqlite3.connect('Dota2.sql')
# cur = conn.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS teams (id int auto_increment primary key, Name varchar(50), Player1 varchar(50), Player2 varchar(50), Player3 varchar(50), Player4 varchar(50), Player5 varchar(50))')
# conn.commit()
# cur.close()
# conn.close()

conn = sqlite3.connect('Dota2.sql')
cursor = conn.cursor()
cursor.execute("SELECT * FROM teams")
tables = cursor.fetchall()
print(tables)
for table in tables:
    for i in table:
        print(i, end=' ')
    print('\n')

for team in teams:
    URL = "https://liquipedia.net/dota2/" + '_'.join(team.split())
    rq = requests.get(URL)
    soup = bs(rq.content, "html.parser")
    try:
        line_up = soup.find_all('table', class_='wikitable wikitable-striped roster-card')[0].find_all('span', class_='inline-player')
        line_up = [player.get_text().strip() for player in line_up]
        conn = sqlite3.connect('Dota2.sql')
        cur = conn.cursor()
        if len(line_up) == 5:
            cur.execute(
                "INSERT INTO teams (Name, Player1, Player2, Player3, Player4, Player5) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
                team, line_up[0], line_up[1], line_up[2], line_up[3], line_up[4]))
        elif len(line_up) == 4:
            cur.execute(
                "INSERT INTO teams (Name, Player1, Player2, Player3, Player4) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
                team, line_up[0], line_up[1], line_up[2], line_up[3]))
        elif len(line_up) == 3:
            cur.execute("INSERT INTO teams (Name, Player1, Player2, Player3) VALUES ('%s', '%s', '%s', '%s')" % (
            team, line_up[0], line_up[1], line_up[2]))
        elif len(line_up) == 2:
            cur.execute(
                "INSERT INTO teams (Name, Player1, Player2) VALUES ('%s', '%s', '%s')" % (team, line_up[0], line_up[1]))
        elif len(line_up) == 1:
            cur.execute("INSERT INTO teams (Name, Player1) VALUES ('%s', '%s')" % (team, line_up[0]))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("blablabla")




# def printPlayers(organisation, teams):
#     for team in teams:
#         if team == organisation:
#             URL = "https://liquipedia.net/dota2/" + '_'.join(team.split())
#             rq = requests.get(URL)
#             soup = bs(rq.content, "html.parser")
#             line_up = soup.find_all('table', class_='wikitable wikitable-striped roster-card')[0].find_all('span', class_='inline-player')
#             line_up = [player.get_text().strip() for player in line_up]
#             squad = ""
#             for team in line_up:
#                 squad += team
#                 if team != line_up[len(line_up) - 1]:
#                     squad += '\n'
#             # for player in line_up:
#             #     print(player)
#             return squad
#     return "Такой команды не существует!"
#
# teams = getTeams()

# bot = telebot.TeleBot(API)
# @bot.message_handler(commands=['start'])
# def hello(message):
#     conn = sqlite3.connect('Dota2.sql')
#     cur = conn
#     cur.execute('CREATE TABLE IF NOT EXISTS teams (ID int auto_increment primary key, Name varchar(50), Player1 varchar(50), Player2 varchar(50), Player3 varchar(50), Player4 varchar(50), Player5 varchar(50))')
#     bot.send_message(message.chat.id, 'Привет, для получения состава одной из команд по Dota 2 введите её название')
#
# @bot.message_handler(content_types=['text'])
# def DotaTeams(message):
#     line_up = printPlayers(message.text, teams)
#     bot.send_message(message.chat.id, line_up)
#
# bot.polling()
#
# URL = "https://liquipedia.net/counterstrike/Portal:Teams"
# rq = requests.get(URL)
# soup = bs(rq.content, "html.parser")
# teams = soup.find_all('span', class_='team-template-text')
# teams = [team.get_text().strip() for team in teams]
# for team in teams:
#     print(team)