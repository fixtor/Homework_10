import telebot


def log_1(value):
	file = open('db.csv', 'a', encoding='utf-8')
	file.write(f'{value}\n')
	file.close()


bot = telebot.TeleBot('5438456464:AAE4VlROk0lfBpwqEauDgyo0rcp06dqniAs')

value = ''
old_value = ''


keyb = telebot.types.InlineKeyboardMarkup()
keyb.row(telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
         telebot.types.InlineKeyboardButton('C', callback_data = 'C'),
		 telebot.types.InlineKeyboardButton('<-', callback_data = '<-'),
		 telebot.types.InlineKeyboardButton('/', callback_data = '/'))

keyb.row(telebot.types.InlineKeyboardButton('7', callback_data = '7'),
		 telebot.types.InlineKeyboardButton('8', callback_data = '8'),
		 telebot.types.InlineKeyboardButton('9', callback_data = '9'),
		 telebot.types.InlineKeyboardButton('*', callback_data = '*'))

keyb.row(telebot.types.InlineKeyboardButton('4', callback_data = '4'),
		 telebot.types.InlineKeyboardButton('5', callback_data = '5'),
		 telebot.types.InlineKeyboardButton('6', callback_data = '6'),
		 telebot.types.InlineKeyboardButton('-', callback_data = '-'))

keyb.row(telebot.types.InlineKeyboardButton('1', callback_data = '1'),
		 telebot.types.InlineKeyboardButton('2', callback_data = '2'),
		 telebot.types.InlineKeyboardButton('3', callback_data = '3'),
		 telebot.types.InlineKeyboardButton('+', callback_data = '+'))

keyb.row(telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
		 telebot.types.InlineKeyboardButton('0', callback_data = '0'),
		 telebot.types.InlineKeyboardButton(',', callback_data = '.'),
		 telebot.types.InlineKeyboardButton('=', callback_data = '='))

@bot.message_handler(commands=['start', 'calc'])
def get_message(message):
	global value
	if value == '':
		bot.send_message(message.from_user.id, '0', reply_markup=keyb)
		log_1(value)
	else:
		bot.send_message(message.from_user.id, value, reply_markup=keyb)
		log_1(value)



@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):

	global value, old_value
	data = query.data
	if data == 'no':
		pass
	elif data == 'C':
		value = ''
		log_1(value)

	elif data == '<-':
		if value != '':
			value = value[:len(value)-1]
			log_1(value)
	elif data == '=':
		try:
			value = str( eval(value) )
			log_1(value)
		except:
			value = 'Error'
			log_1(value)
	else:
		value += data
		log_1(value)
	if value != old_value:
		if value == '':
			bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text = '0', reply_markup=keyb)
		else:
			bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=value, reply_markup=keyb)

	old_value = value
	if value == 'Error':
		value = ''

message.from_user
bot.polling(none_stop=False, interval=0)
