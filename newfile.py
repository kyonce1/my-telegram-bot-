import telebot
from telebot import types
import requests  # Для котиков

bot = telebot.TeleBot("7108628281:AAHCuxX_PqDmyFt1nxIJRAHPs2bmFCgrLcU")  # Получи новый через @BotFather

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Кот"), types.KeyboardButton("Калькулятор"))
    bot.send_message(message.chat.id, "Выбирай:", reply_markup=markup)

# Кнопка "Кот"
@bot.message_handler(func=lambda m: m.text == "Кот")
def send_cat(message):
    try:
        cat = requests.get('https://api.thecatapi.com/v1/images/search').json()
        bot.send_photo(message.chat.id, cat[0]['url'])
    except:
        bot.reply_to(message, "Котики спят 🐱💤")

# Кнопка "Калькулятор"
@bot.message_handler(func=lambda m: m.text == "Калькулятор")
def calc(message):
    bot.send_message(message.chat.id, "Пришли пример типа 2+2")

# Обработка примеров
@bot.message_handler(regexp=r'\d+[\+\-\*/]\d+')
def calculate(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, f"Ответ: {result}")
    except:
        bot.reply_to(message, "Не понимаю пример 😕")

bot.polling(none_stop=True)  # Автопереподключение