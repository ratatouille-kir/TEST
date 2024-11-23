from random import choice
from telebot import TeleBot, types 
bot = TeleBot("7614925205:AAE2kyBfQmqCvD4LopvaXLPUhvWMg1WKV0w") 


game = False
used_cities = []
letter =''
points = 0
leaderboard = {}

with open ('cities.txt','r',encoding = 'utf-8') as f:
    cities = [word.strip().lower()for word in f.readlines()]

def sellect(text):
    i = 1
    while text[-1*i] in ('ь','ъ','й','Ы','ё','ц','э','я','ю','ф'):
        i += 1
    return text[-1*i]
0
@bot.message_handler(commands=['goroda'])
def start_game(message):
    global game
    global letter
    game = True
    city = choice(cities)
    letter = sellect(city)
    bot.send_message(message.chat.id,text= city)

@bot.message_handler()
def play(message):
    global used_cities,letter,game
    if game:
        if message.text.lower() in used_cities:
            bot.send_message(message.chat.id,'Город назывался!')
            return
        if message.text.lower()[0] != letter:
            bot.send_message(message.chat.id,'Не та буква!')
            return
        if message.text.lower() in cities:
            letter = sellect(message.text.lower())
            used_cities.append(message.text.lower())
            for city in cities:
                if city[0] == letter and city not in used_cities:
                    letter = sellect(city)
                    bot.send_message(message.chat.id,city)
                    used_cities.append(city)
                    return
            bot.send_message(message.chat.id,'Я проиграл')
            game = False
            return
        bot.send_message(message.chat.id,'Такого города не существует!')
    
if __name__ == '__main__':
    bot.polling(non_stop=True)

