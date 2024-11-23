from telebot import TeleBot,types
import json

TOKEN ='7614925205:AAE2kyBfQmqCvD4LopvaXLPUhvWMg1WKV0w'
bot = TeleBot(TOKEN)

with open('victorina.json','r',encoding = 'utf -8')as f:
    data = json.load(f)
game = False
indx = 0
points = 0
def get_next_question(data,indx):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    for i in range(4):
        btn = types.KeyboardButton(data[indx]['вариант'][i])
        markup.add(btn)
    markup.add(types.KeyboardButton('Выход'))
    return markup
@bot.message_handler(commands = ['quizz'])
def quizz(message):
    global game,indx
    game = True
    markup = get_next_question(data,indx)
    bot.send_message(message.chat.id, text = data[indx]['вопрос'],reply_markup = markup)
@bot.message_handler()
def vicktorinas(message):
    global game
    global indx
    global points
    if game:
        if message.text == data[indx]['ответ']:
            bot.send_message(message.chat.id,'Правильно')
            points += 1
        elif message.text == 'Выход':
            game = False
            bot.send_message(message.chat.id,'Пока')
            return
        else:
            bot.send_message(message.chat.id,f'Неправильно!Правильный ответ - {data[indx]['ответ']}')
        indx += 1
        markup = get_next_question(data,indx)
        bot.send_message(message.chat.id,text = data[indx]['вопрос'],reply_markup = markup)
    






if __name__ == '__main__':
    bot.polling(none_stop = True)

