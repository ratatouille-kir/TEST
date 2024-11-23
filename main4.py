from telebot import TeleBot, types
from time import time
from random import randint
bot = TeleBot("7614925205:AAE2kyBfQmqCvD4LopvaXLPUhvWMg1WKV0w") 

with open('bad_words.txt','r',encoding ='utf-8') as f:
    data=[word.strip().lower()for word in f.readlines()]

def is_group(message):
    return message.chat.type in ('group','supergroup')

@bot.message_handler(func=lambda message: message.entities is not None and is_group(message))
def delete_links(message):
    for entity in message.entities:
        if entity.type in ['url','text_link']:
            bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(func = lambda message:message.text.lower()in data and is_group(message))
def bad_bad_words(message):
    bot.restrict_chat_member(message.chat.id,message.from_user.id, until_date = time()+ 10)
    bot.send_message(message.chat.id,text = 'Тебе бан на 10 сек', reply_to_message_id = message.message_id)
    bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop = True)