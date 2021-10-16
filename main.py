import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests





bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"ASSALOMU ALAYKUM\n{message.from_user.first_name}\nAndijonda namoz vaqtlari botimizga xush kelibsiz\n\n/BOSH_SAHIFA")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == '/BOSH_SAHIFA':
        bot.send_message(message.from_user.id, "/Namoz_vaqtlarini_bilish")
        bot.register_next_step_handler(message, viloyatlar)



def viloyatlar(message):
    keyboard = types.InlineKeyboardMarkup()
    key_ASh = types.InlineKeyboardButton(text="ANDIJON VILOYATI", callback_data="AV")
    key_AT = types.InlineKeyboardButton(text="ANDIJON TUMANI", callback_data="AT")
    keyboard.add(key_ASh, key_AT)

    key_Ac = types.InlineKeyboardButton(text="ASAKA TUMANI", callback_data="AC")
    key_BALT = types.InlineKeyboardButton(text="BALIQCHI TUMANI", callback_data="BALT")
    keyboard.add(key_Ac, key_BALT)

    key_BOZ = types.InlineKeyboardButton(text="BO'Z TUMANI", callback_data="BO'Z")
    key_BUL = types.InlineKeyboardButton(text="BULOQBOSHI TUMANI", callback_data="BULOQ")
    keyboard.add(key_BOZ, key_BUL)

    key_IZ = types.InlineKeyboardButton(text="IZBOSKAN TUMANI", callback_data="IZB")
    key_JALO = types.InlineKeyboardButton(text="JALOLQUDUQ TUMANI", callback_data="JA")
    keyboard.add(key_IZ, key_JALO)

    key_MAR = types.InlineKeyboardButton(text="MARHAMAT TUMANI", callback_data="MAR")
    key_OL = types.InlineKeyboardButton(text="OLTINKO'L TUMANI", callback_data="OL")
    keyboard.add(key_MAR, key_OL)

    key_PX = types.InlineKeyboardButton(text="PAXTAOBOD TUMANI", callback_data="PX")
    key_QT = types.InlineKeyboardButton(text="QO'RG'ONTEPA TUMANI", callback_data="QT")
    keyboard.add(key_PX, key_QT)

    key_SHAH = types.InlineKeyboardButton(text="SHAHRIXON TUMANI", callback_data="SHAH")
    key_UL = types.InlineKeyboardButton(text="ULUG'UNOR TUMANI", callback_data="UL")
    keyboard.add(key_SHAH, key_UL)

    key_XO = types.InlineKeyboardButton(text="XO'JAOBOD TUMANI", callback_data="XO")
    key_XON = types.InlineKeyboardButton(text="XONOBOD SHAHRI", callback_data="XON")
    keyboard.add(key_XO, key_XON)

    question = "JOYLASHUVNI TANLANG"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "AV":
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id, f"Andijon shahrida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                                               f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")


    elif call.data == "AT":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Andijon tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "AC":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Asaka tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")
    elif call.data == "BALT":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Baliqchi tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "BO'Z":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Bo'z tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "BULOQ":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Buloqboshi tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "IZB":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Izboskan tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "JA":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Jalolquduq tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "MAR":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Marhamat tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "OL":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Oltinko'l tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "PX":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Paxtaobod tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "QT":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Qo'rg'ontepa tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "SHAH":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Shahrixon tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "UL":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Ulug'unor tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "XO":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Xo'jaobod tumanida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")

    elif call.data == "XON":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://namozvaqti.uz/shahar/andijon', headers=headers).text
        soup = BeautifulSoup(resp, "html.parser")

        bomdod = soup.find("p", class_="time", id="bomdod")
        peshin = soup.find("p", class_="time", id="peshin")
        asr = soup.find("p", class_="time", id="asr")
        shom = soup.find("p", class_="time", id="shom")
        xufton = soup.find("p", class_="time", id="hufton")
        bot.send_message(call.message.chat.id,
                         f"Xonobod shahrida namoz vaqti\n\nBOMDOD 🌥  {bomdod.get_text()}\nPESHIN ☀ ️   {peshin.get_text()}\nASR 🌤           {asr.get_text()}\n"
                         f"SHOM 🌥       {shom.get_text()}\nXUFTON 🌙   {xufton.get_text()}\n\n/BOSH_SAHIFA")


bot.polling(none_stop=True)
