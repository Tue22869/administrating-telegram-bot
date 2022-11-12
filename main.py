import telebot
from telebot import types

TOKEN = '5761594334:AAGeW1HGomR-pWhz8TTKdx_Reo0r5IaH6u0'

bot = telebot.TeleBot(TOKEN)
users = {'volrikone': 918808482}


@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id, "Привет ✌️, я мощнейший ботик, помогу с управлением в чатах\n"
                                      "Что я умею:\n"
                                      "/remember_me - отправьте, чтобы я мог вас распознать\n"
                                      "/make_admin username - сделать юзера админом\n"
                                      "/ban username - забанить юзера\n"
                                      "/unban username - разбанить юзера\n"
                                      "/get_stat - получить статистику чата\n"
                                      "/leave - выйти из чата\n")


@bot.message_handler(commands=['remember_me'])
def handle_message(message):
    users[str(message.from_user.username)] = message.from_user.id
    print(users)


@bot.message_handler(commands=['make_admin'])
def make_admin(message):
    username = message.text.split()[1:][0]
    try:
        if users[username] is None:
            return
        bot.promote_chat_member(message.chat.id, users[username], can_promote_members=True)
    except Exception as error:
        print(error)


@bot.message_handler(commands=['ban'])
def ban_user(message):
    username = message.text.split()[1:][0]
    try:
        if users[username] is None:
            return
        bot.ban_chat_member(message.chat.id, users[username])
    except Exception as error:
        print(error)


@bot.message_handler(commands=['unban'])
def unban_user(message):
    username = message.text.split()[1:][0]
    try:
        if users[username] is None:
            return
        bot.unban_chat_member(message.chat.id, users[username])
    except Exception as error:
        print(error)


@bot.message_handler(commands=['get_stat'])
def get_stat(message):
    member_count = bot.get_chat_member_count(message.chat.id)
    admins_count = len(bot.get_chat_administrators(message.chat.id))
    bot.send_message(message.chat.id, 'Количество людей: ' + str(member_count) + '\n'
                     + 'Количество админов: ' + str(admins_count))


@bot.message_handler(commands=['leave'])
def leave_chat(message):
    bot.send_message(message.chat.id, 'С вами было круто!')
    bot.leave_chat(message.chat.id)


bot.polling(none_stop=True, interval=0)
