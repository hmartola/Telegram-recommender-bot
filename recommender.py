from telebot import TeleBot, types
import requests
import data
import config

bot = TeleBot(config.api_key)


@bot.message_handler(commands=["film"])
#data.main()
def recommend(message):
    bot.reply_to(message, "Here you go:\n" + data.randomFilm())
    #bot.send_message(message, data.randomFilm())

@bot.message_handler(commands=["series"])
def recommend(message):
    bot.reply_to(message, "This one seems interesting:\n" + data.randomSeries())

@bot.message_handler(commands=["film5"])
def recommend(message):
    bot.reply_to(message, "Top 5 movies right now:\n" + data.top5movies())

@bot.message_handler(commands=["series5"])
def recommend(message):
    bot.reply_to(message, "Top 5 series right now:\n" + data.top5series())

@bot.message_handler(commands=["randomfilms"])
def recommend(message):
    bot.reply_to(message, "Your random 5 movie picks:\n" + data.random5movies())

@bot.message_handler(commands=["randomseries"])
def recommend(message):
    bot.reply_to(message, "Your random 5 TV shows:\n" + data.random5series())
    


bot.polling()


