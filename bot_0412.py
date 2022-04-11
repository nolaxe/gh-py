# 123
# fork BOT HTTP API Telegram bot  # Бот, только в свой канал @WTFtheNewBot  # !!! pip3 install pyTelegramBotAPI

import telebot
# import config
import random
import os

from telebot import types

telegram_token = "1969920277:AAGPTIPOFax1lbHjrhRyy6D2LtyFvkJh-_" #U
## telegram_token = os.environ['tg_tok']

bot = telebot.TeleBot(telegram_token) # bot

@bot.message_handler(commands=['start'])
def welcome(message):
	#sti = open('static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
  # keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲 Random number")
	item2 = types.KeyboardButton("😊 How are u?")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Welcome, {0.first_name}!\n im - <b>{1.first_name}</b>, bot.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🎲 Random number':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == '😊 How are u?':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("good", callback_data='good')
			item2 = types.InlineKeyboardButton("bad", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'ok, how ab u?', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'wtf 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'ok its good 😊')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'nevermind 😢')

			# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 how a u?",
				reply_markup=None)

			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="this is Sparta")

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)
