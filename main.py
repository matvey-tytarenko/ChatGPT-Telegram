import telebot
from telebot import types
import config

from g4f.client import Client

bot = telebot.TeleBot(config.API)

def gpt(prompt):
    client = Client()
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": prompt,
    }],
    )
    return response.choices[0].message.content

@bot.message_handler(commands=['start'])
def start(message):
    send = f"Привет {message.from_user.first_name} я бесплатный ChatGPT4 можешь задавать мне любые вопросы!"
    bot.send_message(message.chat.id, text=send)

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, gpt(message.text))

bot.polling(none_stop=True)