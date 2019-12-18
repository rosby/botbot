import telebot


TOKEN = '867774052:AAEzvChhiW2GKbbIPuF3tM1tG_8VHb7WQAg'
bot = telebot.TeleBot(TOKEN)
i = 0


def change_status(n):
    global i
    i = n


def check_password(pas, message):
    if pas == '3342':
        change_status(2)
        bot.send_message(message.chat.id, 'Доступ подтвержден.')
        bot.send_message(message.chat.id, 'От чего вы хотете узнать пароль?. Варианты ввода: "vk", "inst", "mail"')

    else:
        bot.send_message(message.chat.id, 'Пароль неверный, попробуйте ввести пароль ещё раз.')


def pass_list(name):
    if name == 'vk':
        return 'password_vkkk'
    elif name == 'inst':
        return 'password_inst'
    elif name == 'mail':
        return 'password_mail'
    else:
        return 'Такое зарезервированное имя не обнаружено.'


@bot.message_handler(commands = ['start', 'stop'])
def check_com(message):
    if message.text == '/start':
        change_status(1)
        bot.send_message(message.chat.id, 'Вы начали работу с пароль менеджерем.')
        bot.send_message(message.chat.id, 'Введите пароль...')

    elif message.text == '/stop':
        change_status(0)
        bot.send_message(message.chat.id, 'Вы закончили работу с пароль менеджерем.')


@bot.message_handler(content_types = ['text'])
def check_text(message):
    if i == 1:
        password = message.text
        check_password(password, message)
    elif i == 0:
        bot.send_message(message.chat.id, 'Для работы с менеджером паролей вам надо ввести "/start"')
    elif i == 2:
        bot.send_message(message.chat.id, pass_list(message.text))


bot.polling()
