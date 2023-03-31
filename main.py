import telebot
from telebot import types


bot = telebot.TeleBot("5978946896:AAHSLcAj3vNuI5F9Mm_-41ulkavN9mp8EDY")
API_TOKEN = '5978946896:AAHSLcAj3vNuI5F9Mm_-41ulkavN9mp8EDY'




@bot.message_handler(commands=["start"])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item3 = types.KeyboardButton("Приложения 🌏")
    item2 = types.KeyboardButton("Мероприятия 🍔")
    item1 = types.KeyboardButton('О нас 🎯')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n\nЯ - <b>{1.first_name}</b>, бот unitED, "
                     "создан для того, "
                     "чтобы помочь Вам изучить project management,"
                     "просто узнать что-то о нас или же просто пообщаться и весело провести время.\n\n"
                     "<i>Have a nice time</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['stop'])
def bye(message):
    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "До свидания, {0.first_name}!\nМы, команда <b>{1.first_name}</b>, надеемся, что ты хорошо "
                     "провел(а) время 🌈✨\n\n "
                     .format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=hideBoard)
    exit()



@bot.message_handler(content_types=["text"])
def go_send_messages(message):
    if message.chat.type == 'private':
        if message.text == "Приложения 🌏":

            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item6 = types.KeyboardButton("Уроки 😃")
            item5 = types.KeyboardButton("Домашнее задание 🤓")
            item4 = types.KeyboardButton('Рейтинг 😎')

            markup1.add(item4, item5, item6)
            bot.send_message(message.chat.id, "Самое время учится".format(
                message.from_user), parse_mode="html", reply_markup=markup1)


        elif message.text == "Мероприятия 🍔":
            one_markup = types.InlineKeyboardMarkup(row_width=1)
            ite1 = types.InlineKeyboardButton(text="Ближайшие мероприятия 🌅", url="https://example.com/video.mp4")
            ite2 = types.InlineKeyboardButton(text="Проведенные мероприятия 🗿", url="https://example.com/video.mp4")
            one_markup.add(ite1, ite2)
            bot.send_video_note(message.chat.id, video_note=open('begin.mov', 'rb'), reply_markup=one_markup)

        elif message.text == 'О нас 🎯':
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            itembtn1 = types.InlineKeyboardButton('Основная информация 🔋', url="https://youtu.be/dQw4w9WgXcQ")
            itembtn2 = types.InlineKeyboardButton('Чем мы занимаемся ❓', url="https://youtu.be/dQw4w9WgXcQ")
            itembtn3 = types.InlineKeyboardButton('Где мы находимся ❓', url="https://youtu.be/dQw4w9WgXcQ")
            itembtn4 = types.InlineKeyboardButton('Как попасть в команду 📈', url="https://youtu.be/dQw4w9WgXcQ")
            itembtn5 = types.InlineKeyboardButton('Контакты 📒', url="https://youtu.be/dQw4w9WgXcQ")
            itembtn6 = types.InlineKeyboardButton('Задать вопрос руководителю проекта 👤',
                                                  url="https://youtu.be/dQw4w9WgXcQ")
            markup1.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

            bot.send_message(message.chat.id,
                             "Хочешь узнать немного о проекте  🧩\n"
                             "Выбери нужную категорию: ".format(message.from_user, bot.get_me()),
                             reply_markup=markup1)

        elif message.text == "Уроки 😃":
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ite3 = types.KeyboardButton("Урок 1")
            ite2 = types.KeyboardButton("Урок 2")
            ite1 = types.KeyboardButton("Урок 3")

            markup2.add(ite1, ite2, ite3)
            bot.send_message(message.chat.id, "Выбери нужный урок".format(
                    message.from_user), parse_mode="html", reply_markup=markup2)

        elif message.text == "Урок 1":
            video = open('begin.mov', 'rb')
            bot.send_video(message.chat.id, video)

            f = open("Комикс unitED.pdf", "rb")
            bot.send_document(message.chat.id, f)

            video1 = open('end.mov', 'rb')
            bot.send_video(message.chat.id, video1)




        elif message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Да-да, я тут ☺️')
        elif message.text.lower() == 'пока':
            bot.send_message(message.chat.id, 'Жаль, что ты уходишь😢')
        elif message.text.lower() == 'как дела?':
            bot.send_message(message.chat.id, 'Все хорошо, у тебя как?')
        elif message.text.lower() == 'хорошо':
            bot.send_message(message.chat.id, 'Вот и отличненько 😊')
        elif message.text.lower() == 'плохо':
            bot.send_message(message.chat.id, 'Всё будет хорошо, я уверен ❤️\n'
                                              'А чтобы никогда не грустить - \n'
                                              'присоединяйся к нам 📈')
        else:
            bot.send_message(message.chat.id, 'Не понимаю тебя 🌚')



@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("Приложения 🌏")
        item2 = types.KeyboardButton("Мероприятия 🍔")
        item1 = types.KeyboardButton('О нас 🎯')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выберите пункт меню", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("Назад", callback_data="back")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сообщение", reply_markup=markup)





if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")
