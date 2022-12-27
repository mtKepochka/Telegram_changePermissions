import telebot
import telegram


bot = telebot.TeleBot('TOKEN')


print('[~] Bot started')


@bot.message_handler(commands=['start'])
def start_menu(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, "To change permissions write: /change_permissions")


@bot.message_handler(commands=['change_permissions'])
def info(message):
    msg = bot.send_message(message.chat.id, "Input values for permissions\
        \n (can_send_messages,\n can_send_media_messages,\n can_send_polls,\
        \n can_send_other_messages,\n can_add_web_page_previews,\n can_change_info,\
        \n can_invite_users,\n can_pin_messages)\nExample: 0:0:0:0:0:0:0:0")
    bot.register_next_step_handler(msg, change_permissions)


def change_permissions(message):
    if message.content_type == 'text':
        value = message.text
        value = value.split(":")
        if len(value) != 8:
            bot.reply_to(message, 'Something went wrong, please check input string')
        perms = telegram.ChatPermissions()
        try:
            perms.can_send_messages = bool(int(value[0]))
            perms.can_send_media_messages = bool(int(value[1]))
            perms.can_send_polls = bool(int(value[2]))
            perms.can_send_other_messages = bool(int(value[3]))
            perms.can_add_web_page_previews = bool(int(value[4]))
            perms.can_change_info = bool(int(value[5]))
            perms.can_invite_users = bool(int(value[6]))
            perms.can_pin_messages = bool(int(value[7]))
            bot.set_chat_permissions(message.chat.id, permissions=a)
            bot.send_message(message.chat.id, "✅Done")
        except:
            bot.reply_to(message, 'Something went wrong, please check input string')
    else:
        bot.reply_to(message, '❌Wrong values')


if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)
