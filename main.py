import os
import telebot

bot = telebot.Telebot("2120353821:AAF4UrFB9NfAE5k8NXnlcCvGRRvJVQfVlng")

@bot.message_handler(commands=["start"])
def send Welecome(message):
    bot.reply_to(message,"Hello !!! I'm @Kavindu_Shehan Chat Bot")


@bot.message_handler(commands=["How"])
def send_message(message):
    bot.send_message(message, "https://t.me/Kavindu_Shehan)

    bot.polling()
