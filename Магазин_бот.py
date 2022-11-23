import telebot
import random
from telebot import types, TeleBot
import sqlite3
bot: TeleBot = telebot.TeleBot('5647893598:AAEMNExWmc_dRh8_3y9WPdzxnVxdPsFKEgI')

conn = sqlite3.connect("easy.sqlite", check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(commands=["start"])
def START(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("АККАУНТЫ")
    btn2 = types.KeyboardButton("БЕСПЛАТНЫЕ АККАУНТЫ")
    btn3 = types.KeyboardButton("ПРОМОКОД")
    btn4 = types.KeyboardButton("ОТЗЫВЫ")
    btn5 = types.KeyboardButton("СКИНЫ")
    btn6 = types.KeyboardButton("ГОЛДА ЗА КЛИКИ")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(m.from_user.id, "Привет, ты хочешь аккаунт? Тогда жми на кнопочки снизу:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "ГОЛДА ЗА КЛИКИ" or m.text == "ЛОПРТКМИОЛЫТ")
def chgfg(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🙃КЛИК")
    btn2 = types.KeyboardButton("БАЛАНС")
    markup.add(btn1, btn2)
    bot.send_message(m.from_user.id, "В этом разделе у нас бесплатная голда за клики, нажимай на кнопочку, чтобы получить голду 🤑", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🙃КЛИК" or m.text == "ТЫ ДАУН?")
def cdghter(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🙃КЛИК")
    btn2 = types.KeyboardButton("БАЛАНС")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.chat.id, "😎 ГОЛДА +1", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "БАЛАНС" or m.text == "ТЫ ДАУН2?")
def cdtjygbdr(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Вывести")
    btn2 = types.KeyboardButton("🙃КЛИК")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой баланс голды:")
    bot.send_message(m.from_user.id,"Вывод доступен от 5000 голды", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Вывести" or m.text == "ТЫ ДАУН2?")
def cdtjkfjjvnjdknygbdr(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("🙃КЛИК")
    markup.add(btn1, btn2)
    bot.send_message(m.from_user.id,"Извини, выводы пока не работают 😞 мы обязательно скоро их починим, ну а пока ты можешь получить бесплатный аккаунт за приглашения людей.", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "ОТЗЫВЫ" or m.text == "ТЫ ДОЛБАЕБ?")
def chmed(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(m.from_user.id, "Отзывы находятся вот в этом канале: https://t.me/easystoremyotzyvy", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "ВВЕСТИ ПРОМОКОД" or m.text == "ПРОМОКОД")
def chmed(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(m.from_user.id, "Введи промокод:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Главное меню" or m.text == "Назад")
def choed(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("АККАУНТЫ")
    btn2 = types.KeyboardButton("БЕСПЛАТНЫЕ АККАУНТЫ")
    btn3 = types.KeyboardButton("ВВЕСТИ ПРОМОКОД")
    btn4 = types.KeyboardButton("ОТЗЫВЫ")
    btn5 = types.KeyboardButton("СКИНЫ")
    btn6 = types.KeyboardButton("ГОЛДА ЗА КЛИКИ")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(m.from_user.id, "Выбери то, что тебе нужно", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "СКИНЫ" or m.text == "Ж")
def fshbhus(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("БЕСПЛАТНЫЕ СКИНЫ")
    btn2 = types.KeyboardButton("КЕЙСЫ")
    btn3 = types.KeyboardButton("БЕСПЛАТНЫЕ КЕЙСЫ")
    btn4 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(m.from_user.id, "Выбирай:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "БЕСПЛАТНЫЕ СКИНЫ" or m.text == "г")
def fshus(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ПРИГЛАСИЛ")
    markup.add(btn1)
    bot.send_message(m.from_user.id, "Чтобы получить этот бесплатный скин, тебе нужно пригласить 5 человек в бота:", reply_markup=markup)



@bot.message_handler(func=lambda m: m.text == "БЕСПЛАТНЫЕ АККАУНТЫ" or m.text == "ХАЛЯВА")
def choosed(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Пригласил")
    markup.add(btn1)
    bot.send_message(m.from_user.id, "Чтобы получить бесплатный аккаунт, тебе нужно пригласить 15 человек в этого бота и отправить сюда скрин:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Пригласил" or m.text == "Разослал" or m.text == "hhh")
def haan(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ПОЛУЧИТЬ АККАУНТ ЗА ПРИГЛАШЕНИЯ")
    btn2 = types.KeyboardButton("Хочу перекрутить")
    markup.add(btn1, btn2)
    text_list = ["Аккаунт 1", "Аккаунт 2", "Аккаунт 3", "Аккаунт 4", "Аккаунт 5", "Аккаунт 6", "Аккаунт 7", "Аккаунт 8", "Аккаунт 9", "Аккаунт 10", "Аккаунт 11", "Аккаунт 12", "Аккаунт 13", "Аккаунт 14", "Аккаунт 15", "Аккаунт 16", "Аккаунт 17", "Аккаунт 18", "Аккаунт 19", "Аккаунт 20", "Аккаунт 21", "Аккаунт 22", "Аккаунт 23", "Аккаунт 24", "Аккаунт 25", "Аккаунт 26", "Аккаунт 27"]
    text_path = random.choice(text_list)
    img_list = ['saleaccount1.jpg', 'account6.jpg', 'ggF.jpg', 'ff.jpg', 'scam.jpg', 'scam1.jpg', 'scam2.jpg', 'scam3.jpg', 'scam4.jpg', 'scam5.jpg', 'scam6.jpg', 'scam8.jpg', 'scam9.jpg', 'scam10.jpg', 'account12.jpg']
    img_path = random.choice(img_list)
    bot.send_message(m.chat.id, (text_path))
    bot.send_photo(m.chat.id, photo=open(img_path, 'rb'))
    bot.send_message(m.chat.id,"Вот с таким инвентарём будет твой аккаунт. Как только модерация проверит присланные тобой скриншоты - ты получишь данные от своего будущего аккаунта, но учти: если ты не пригласил ровно 15 человек, администрация не сможет выдать тебе аккаунт. Заявки проверяются в среднем 1-2 дня, но в случаях повышенной нагрузки на бота и модерацию, это может занять до 5-и дней.", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Хочу перекрутить" or m.text == "Перекрутить" or m.text == "ЛедиБаг")
def hnnvan(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ПОЛУЧИТЬ АККАУНТ ЗА ПРИГЛАШЕНИЯ")
    btn2 = types.KeyboardButton("Перекрутить еще раз")
    markup.add(btn1, btn2)
    text_list = ["Аккаунт 1", "Аккаунт 2", "Аккаунт 3", "Аккаунт 4", "Аккаунт 5", "Аккаунт 6", "Аккаунт 7", "Аккаунт 8", "Аккаунт 9", "Аккаунт 10", "Аккаунт 11", "Аккаунт 12", "Аккаунт 13", "Аккаунт 14", "Аккаунт 15", "Аккаунт 16", "Аккаунт 17", "Аккаунт 18", "Аккаунт 19", "Аккаунт 20", "Аккаунт 21", "Аккаунт 22", "Аккаунт 23", "Аккаунт 24", "Аккаунт 25", "Аккаунт 26", "Аккаунт 27"]
    text_path = random.choice(text_list)
    img_list = ['saleaccount1.jpg', 'account6.jpg', 'ggF.jpg', 'ff.jpg', 'scam.jpg', 'scam1.jpg', 'scam2.jpg', 'scam3.jpg', 'scam4.jpg', 'scam5.jpg', 'scam6.jpg', 'scam8.jpg', 'scam9.jpg', 'scam10.jpg', 'account12.jpg']
    img_path = random.choice(img_list)
    bot.send_message(m.chat.id, (text_path))
    bot.send_photo(m.chat.id, photo=open(img_path, 'rb'))
    bot.send_message(m.chat.id,"Вот с таким инвентарём будет твой аккаунт. Как только модерация проверит присланные тобой скриншоты - ты получишь данные от своего будущего аккаунта, но учти: если ты не пригласил ровно 15 человек, администрация не сможет выдать тебе аккаунт. Заявки проверяются в среднем 1-2 дня, но в случаях повышенной нагрузки на бота и модерацию, это может занять до 5-и дней.", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Перекрутить еще раз" or m.text == "ппппп" or m.text == "рараув")
def hnffvan(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ПОЛУЧИТЬ АККАУНТ ЗА ПРИГЛАШЕНИЯ")
    btn2 = types.KeyboardButton("ПЕРЕКРУТИТЬ")
    markup.add(btn1, btn2)
    text_list = ["Аккаунт 1", "Аккаунт 2", "Аккаунт 3", "Аккаунт 4", "Аккаунт 5", "Аккаунт 6", "Аккаунт 7", "Аккаунт 8", "Аккаунт 9", "Аккаунт 10", "Аккаунт 11", "Аккаунт 12", "Аккаунт 13", "Аккаунт 14", "Аккаунт 15", "Аккаунт 16", "Аккаунт 17", "Аккаунт 18", "Аккаунт 19", "Аккаунт 20", "Аккаунт 21", "Аккаунт 22", "Аккаунт 23", "Аккаунт 24", "Аккаунт 25", "Аккаунт 26", "Аккаунт 27"]
    text_path = random.choice(text_list)
    img_list = ['saleaccount1.jpg', 'account6.jpg', 'ggF.jpg', 'ff.jpg', 'scam.jpg', 'scam1.jpg', 'scam2.jpg', 'scam3.jpg', 'scam4.jpg', 'scam5.jpg', 'scam6.jpg', 'scam8.jpg', 'scam9.jpg', 'scam10.jpg', 'account12.jpg']
    img_path = random.choice(img_list)
    bot.send_message(m.chat.id, (text_path))
    bot.send_photo(m.chat.id, photo=open(img_path, 'rb'))
    bot.send_message(m.chat.id,"Вот с таким инвентарём будет твой аккаунт. Как только модерация проверит присланные тобой скриншоты - ты получишь данные от своего будущего аккаунта, но учти: если ты не пригласил ровно 15 человек, администрация не сможет выдать тебе аккаунт. Заявки проверяются в среднем 1-2 дня, но в случаях повышенной нагрузки на бота и модерацию, это может занять до 5-и дней.", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "ПЕРЕКРУТИТЬ" or m.text == "пъпппп" or m.text == "раъъъраув")
def hnffvan(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ПОЛУЧИТЬ АККАУНТ ЗА ПРИГЛАШЕНИЯ")
    btn2 = types.KeyboardButton("ПЕРЕКРУТИТЬ")
    markup.add(btn1, btn2)
    bot.send_message(m.chat.id,"Извини, больше крутить нельзя", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'ПОЛУЧИТЬ АККАУНТ ЗА ПРИГЛАШЕНИЯ' or m.text == 'попасься на удочку')
def oplata(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ОК")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Заявка на получение аккаунта успешно создана! Проверка модерацией будет длиться примерно 2-3 дня, но в дни повышенной нагрузки проверка может занять 6-7 дней.", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "ОК" or m.text == "НОСОК" or m.text == "ЛОК 3")
def hakran(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("АККАУНТЫ")
    btn2 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2)
    bot.send_message(m.from_user.id,"Ну а пока твоя заявка проверяется, можешь купить у нас аккаунт", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "АККАУНТЫ")
def accounts(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Аккаунт за 15Р")
    btn2 = types.KeyboardButton("Аккаунт за 25Р")
    btn3 = types.KeyboardButton('Аккаунт за 50Р')
    btn4 = types.KeyboardButton('Аккаунт за 100Р')
    btn5 = types.KeyboardButton('Аккаунт за 150Р')
    btn6 = types.KeyboardButton('Аккаунт за 200Р')
    btn7 = types.KeyboardButton('Аккаунт за 300Р')
    btn8 = types.KeyboardButton('Аккаунт за 500Р')
    btn9 = types.KeyboardButton('Аккаунт за 1000Р')
    btn10 = types.KeyboardButton('Аккаунт за 2000Р')
    btn11 = types.KeyboardButton('Аккаунт за 3000Р')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    bot.send_message(m.from_user.id, "Выбери аккаунт себе по душе, ты получишь аккаунт со скинами стоимостью на 5Р дороже стоимости аккаунта", reply_markup=markup)

@bot.message_handler(regexp="Аккаунт за 15Р")
def account_1(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('ggF.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == "Аккаунт за 25Р" or m.text == 'Аккаунт за 25Р')
def account_2(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('account6.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == "Аккаунт за 50Р" or m.text == 'Аккаунт за 50Р')
def account_2(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('account12.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 100Р' or m.text == 'Аккаунт за 100Р')
def account_4(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('saleaccount1.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 150Р' or m.text == 'Аккаунт за 150Р')
def account_3(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('ff.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 200Р' or m.text == 'Аккаунт за 200Р')
def account_3(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('vsvvs.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 300Р' or m.text == 'Аккаунт за 300Р')
def account_5(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('ggggg.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 500Р' or m.text == 'Аккаунт за 500Р')
def account_6(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:",reply_markup=markup)
    img = open('account228.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 1000Р' or m.text == 'Аккаунт за 1000Р')
def account_7(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:",reply_markup=markup)
    img = open('saleaccount2.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 2000Р' or m.text == 'Аккаунт за 2000Р')
def account_8(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('account11.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'Аккаунт за 3000Р' or m.text == 'Аккаунт за 3000Р')
def account_9(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Вот твой аккаунт, осталось только приобрести и получить данные:", reply_markup=markup)
    img = open('account8.jpg', 'rb')
    bot.send_photo(m.chat.id, img)

@bot.message_handler(func=lambda m: m.text == 'КУПИТЬ' or m.text == 'попасться на удочку')
def oplata(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ОПЛАТИЛ")
    btn2 = types.KeyboardButton("АККАУНТЫ")
    btn3 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "Поздравляю тебя! Ты уже почти завершил покупку, осталось только оплатить. Сразу после оплаты тебе необходимо будет нажать на кнопку 'ОПЛАТИЛ', и отправить сюда скриншот об оплате и свою электронную почту. Администрация проверит введенные тобой данные и отправит тебе на почту логин и пароль от нового аккаунта. Оплачивать вот по этой ссылке: https://www.donationalerts.com/r/nekto129 Учти, если ты введешь неправильную сумму, то мы не сможем отдать аккаунт или вернуть деньги, потому, что у нас строгий учёт.", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'FRAGGERYT' or m.text == 'ОТКУДА МНЕ ЕГО ЗНАТЬ?')
def ogryzok(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("АККАУНТЫ")
    btn2 = types.KeyboardButton("Главное меню")
    btn3 = types.KeyboardButton("Купить аккаунт со скидкой")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, "ПРОМОКОД ВЕРНЫЙ, ТЕБЕ ПРЕДОСТАВЛЕНА СКИДКА 20%", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Купить аккаунт со скидкой' or m.text == 'скам')
def ogryzoh2(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Первый")
    btn2 = types.KeyboardButton("Второй")
    btn3 = types.KeyboardButton("Третий")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.from_user.id, 'Выбирай любой аккаунт, все зависит от того, насколько тебе повезёт. На тот аккаунт, который тебе выпадет будет действовать скидка 20%', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Первый')
def ogryzoh3(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    markup.add(btn1)
    img_list = ['scam4.jpg', 'scam5.jpg', 'scam8.jpg', 'scam9.jpg', 'scam10.jpg', 'ggF.jpg', 'account6.jpg']
    img_path = random.choice(img_list)
    bot.send_photo(m.chat.id, photo=open(img_path, 'rb'))
    bot.send_message(m.from_user.id, "Стоимость первого аккаунта - 100Р, со скидкой - 80Р")
    bot.send_message(m.from_user.id, "Вот твой аккаунт со скидкой:       СКОРЕЕ НАЖИМАЙ КУПИТЬ,     ПОКА НЕ РАЗОБРАЛИ", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Второй')
def ogryzoh4(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    markup.add(btn1)
    img_list = ['saleaccount1.jpg', 'ff.jpg', 'scam8.jpg', 'scam.jpg', 'scam3.jpg', 'ggF.jpg', 'account6.jpg']
    img_path = random.choice(img_list)
    bot.send_photo(m.chat.id, photo=open(img_path, 'rb'))
    bot.send_message(m.from_user.id, "Стоимость второго аккаунта - 200Р, со скидкой - 160Р")
    bot.send_message(m.from_user.id, "Вот твой аккаунт со скидкой:       СКОРЕЕ НАЖИМАЙ КУПИТЬ,     ПОКА НЕ РАЗОБРАЛИ!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Второй')
def ogryzoh5(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    markup.add(btn1)
    img_list = ['vsvvs.jpg', 'scam2.jpg', 'scam9.jpg', 'dal6.jpg', 'scam3.jpg', 'ggF.jpg', 'account6.jpg']
    img_path = random.choice(img_list)
    bot.send_photo(m.chat.id, photo=open(img_path, 'rb'))
    bot.send_message(m.from_user.id, "Стоимость второго аккаунта - 200Р, со скидкой - 160Р")
    bot.send_message(m.from_user.id, "Вот твой аккаунт со скидкой:       СКОРЕЕ НАЖИМАЙ КУПИТЬ,     ПОКА НЕ РАЗОБРАЛИ!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Третий')
def ogryh5(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КУПИТЬ")
    markup.add(btn1)
    img_list = ['account8.jpg', 'account11.jpg', 'scam600.jpg', 'scam700.jpg', 'scam7.jpg', 'dar1.jpg', 'dar2.jpg', 'dal3.jpg', 'scam900.jpg', 'saleaccount3.jpg', 'dal4', 'dal5.jpg']
    img_path = random.choice(img_list)
    bot.send_photo(m.chat.id, photo=open(img_path, 'rb'))
    bot.send_message(m.from_user.id, "Стоимость третьего аккаунта - 1500Р, со скидкой - 1200Р")
    bot.send_message(m.from_user.id, "Вот твой аккаунт со скидкой:       СКОРЕЕ НАЖИМАЙ КУПИТЬ,     ПОКА НЕ РАЗОБРАЛИ!", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == 'ОПЛАТИЛ' or m.text == 'попался на удочку')
def oplata456(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("АККАУНТЫ")
    btn2 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2)
    bot.send_message(m.from_user.id, "Поздравляю тебя! Ты полностью оплатил аккаунт. Теперь отправь сюда скриншот об оплате и свою электронную почту. В течении часа к тебе на почту придут логин и пароль от нового аккаунта.", reply_markup=markup)

bot.polling(none_stop=True, interval=0)

