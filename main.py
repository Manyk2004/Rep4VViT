import telebot
from telebot import types
from datetime import date
import psycopg2

token = "6212441460:AAGRSm2tcmW48SCgrCoV31lv-IkPa9lkM90"
bot = telebot.TeleBot(token)

conn = psycopg2.connect(database="timetable",
                        user="postgres",
                        password="FirEfirE",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

today = date.today()
num = int(today.isocalendar().week)
if (num % 2) == 0:
    this_week = "timetable_lower"
else:
    this_week = "timetable_upper"


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/mtuci", "/help", "/timetable", "/week")
    bot.send_message(message.chat.id, 'Здравствуйте! Что вы хотите узнать?\n Команда /help для справки',
                     reply_markup=keyboard)


@bot.message_handler(commands=['timetable'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница")
    keyboard.row("Расписание на текущую неделю", "Расписание на следующую неделю")
    keyboard.row("/start")
    bot.send_message(message.chat.id, 'Информация о расписании', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я - бот расписания\n'
                                      'Я умею выводить расписание на определённый день недели или же на целую '
                                      'интересующую вас неделю (команда /timetable)\n'
                                      'Также я могу поделиться свежей информацией о МТУСИ (команда /mtuci)\n'
                                      'И могу рассказать, верхняя или нижняя сейчас неделя (команда /week)')


@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'Свежая информация о МТУСИ - https://mtuci.ru/')


@bot.message_handler(commands=['week'])
def start_message(message):
    if this_week == 'timetable_upper':
        bot.send_message(message.chat.id, 'Эта неделя верхняя.')
    else:
        bot.send_message(message.chat.id, 'Эта неделя нижняя.')


def mess1(monday_upper):
    a = []
    cursor.execute(
        "SELECT timetable_upper.subject, room_numb, start_time, full_name FROM timetable_upper INNER JOIN "
        "subject ON timetable_upper.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Понедельник' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Понедельник \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11])
    bot.send_message(monday_upper.chat.id, word)


def mess2(tuesday_upper):
    a = []
    cursor.execute(
        "SELECT timetable_upper.subject, room_numb, start_time, full_name FROM timetable_upper INNER JOIN "
        "subject ON timetable_upper.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Вторник' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Вторник \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
    bot.send_message(tuesday_upper.chat.id, word)


def mess3(wednesday_upper):
    a = []
    cursor.execute(
        "SELECT timetable_upper.subject, room_numb, start_time, full_name FROM timetable_upper INNER JOIN "
        "subject ON timetable_upper.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Среда' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Среда \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11])
    bot.send_message(wednesday_upper.chat.id, word)


def mess4(thursday_upper):
    a = []
    cursor.execute(
        "SELECT timetable_upper.subject, room_numb, start_time, full_name FROM timetable_upper INNER JOIN "
        "subject ON timetable_upper.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Четверг' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Четверг \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11])
    bot.send_message(thursday_upper.chat.id, word)


def mess5(friday_upper):
    a = []
    cursor.execute(
        "SELECT timetable_upper.subject, room_numb, start_time, full_name FROM timetable_upper INNER JOIN "
        "subject ON timetable_upper.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Пятница' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Пятница \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14],
                a[15])
    bot.send_message(friday_upper.chat.id, word)


def mess6(monday_lower):
    a = []
    cursor.execute(
        "SELECT timetable_lower.subject, room_numb, start_time, full_name FROM timetable_lower INNER JOIN "
        "subject ON timetable_lower.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Понедельник' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Понедельник \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n{}, {}, {}, {}' \
           '\n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14],
                a[15], a[16], a[17], a[18], a[19])
    bot.send_message(monday_lower.chat.id, word)


def mess7(tuesday_lower):
    a = []
    cursor.execute(
        "SELECT timetable_lower.subject, room_numb, start_time, full_name FROM timetable_lower INNER JOIN "
        "subject ON timetable_lower.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Вторник' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Вторник \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11])
    bot.send_message(tuesday_lower.chat.id, word)


def mess8(wednesday_lower):
    a = []
    cursor.execute(
        "SELECT timetable_lower.subject, room_numb, start_time, full_name FROM timetable_lower INNER JOIN "
        "subject ON timetable_lower.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Среда' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Среда \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
    bot.send_message(wednesday_lower.chat.id, word)


def mess9(thursday_lower):
    a = []
    cursor.execute(
        "SELECT timetable_lower.subject, room_numb, start_time, full_name FROM timetable_lower INNER JOIN "
        "subject ON timetable_lower.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Четверг' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Четверг \n------------\n------------'
    bot.send_message(thursday_lower.chat.id, word)


def mess10(friday_lower):
    a = []
    cursor.execute(
        "SELECT timetable_lower.subject, room_numb, start_time, full_name FROM timetable_lower INNER JOIN "
        "subject ON timetable_lower.subject=subject.name INNER JOIN teacher ON subject.name=teacher.subject "
        "WHERE day='Пятница' ORDER BY start_time")
    records = cursor.fetchall()
    for row in records:
        a += row
    word = 'Пятница \n------------ \n{}, {}, {}, {}\n{}, {}, {}, {}\n------------' \
        .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
    bot.send_message(friday_lower.chat.id, word)


@bot.message_handler(content_types=['text'])
def answer(message):
    if (message.text.lower() == "расписание на текущую неделю" and this_week == 'timetable_upper') or (message.text.lower() == "расписание на слудующую неделю" and this_week == 'timetable_lower'):
        mess1(message), mess2(message), mess3(message), mess4(message), mess5(message)
    elif (message.text.lower() == "расписание на следующую неделю" and this_week == 'timetable_upper') or (message.text.lower() == "расписание на текущую неделю" and this_week == 'timetable_lower'):
        mess6(message), mess7(message), mess8(message), mess9(message), mess10(message)
    elif this_week == 'timetable_upper':
        if message.text.lower() == "понедельник":
            mess1(message)
        elif message.text.lower() == "вторник":
            mess2(message)
        elif message.text.lower() == "среда":
            mess3(message)
        elif message.text.lower() == "четверг":
            mess4(message)
        elif message.text.lower() == "пятница":
            mess5(message)
        elif message.text.lower() != '':
            bot.send_message(message.chat.id, 'Извините, я Вас не понял.')
    elif this_week == 'timetable_lower':
        if message.text.lower() == "понедельник":
            mess6(message)
        elif message.text.lower() == "вторник":
            mess7(message)
        elif message.text.lower() == "среда":
            mess8(message)
        elif message.text.lower() == "четверг":
            mess9(message)
        elif message.text.lower() == "пятница":
            mess10(message)
        elif message.text.lower() != '':
            bot.send_message(message.chat.id, 'Извините, я Вас не понял.')


bot.polling()
