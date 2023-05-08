import telebot
from telebot import types
import random
import time
#6235868131:AAHKo-ATKFv7nMNbSPGU-w6bmqCodD_dPG8
tg_bot=telebot.TeleBot("6235868131:AAHKo-ATKFv7nMNbSPGU-w6bmqCodD_dPG8")

@tg_bot.message_handler(commands=["start"])
def start(message:types.Message):
    user_id=message.from_user.id
    #kb = types.InlineKeyboardMarkup()
    #kb.add(types.InlineKeyboardButton("зашифровать", callback_data="E"))
    print(message.text)
    tg_bot.send_message(user_id, "зашифровать")#, reply_markup=kb)
    tg_bot.send_message(user_id, "/encode:**пробель**сообщение")
    tg_bot.send_message(user_id, "расшифровать")
    tg_bot.send_message(user_id, "/decode:*пробель*калябаля*пробель*password:*пробель*пароль")
    tg_bot.send_message(user_id, "!!!Achtung перед тем как истользовать зашифрованное сообщение попробуйте дешифровать его командой /decode, если не дешифровалось, то зашифруйте исходное сообщение снова командой /encode:!!!")
    time.sleep(random.randint(0,10))
    tg_bot.send_message(user_id, "ты клёвый")
    time.sleep(random.randint(0, 10))
    tg_bot.send_message(user_id, "На самом деле я не бот")
    time.sleep(random.randint(0, 10))
    tg_bot.send_message(user_id, "Паша, когда сотку за работу ботом отдашь?")
@tg_bot.callback_query_handler(func=lambda call: True)
def on_callback(call: types.CallbackQuery):
    #print(call.message)
    tg_bot.edit_message_text("fdggdfgf",call.from_user.id, call.message.id)
    if call.data=="E":
        print("no")

#/encode: azAZаяАЯ
@tg_bot.message_handler(commands=["encode:"])
def mesageEncoder(message:types.Message):

    user_id = message.from_user.id
    x = message.text[9:]

    code_slovo = []
    decode_slovo = []
    code_slovo_in_eng = []
    decode_slovo_in_eng = []
    code_slovo_in_eng_2 = ""
    decode_slovo_in_eng_2 = ""


    for i in x:
        k=ord(i)
        code_slovo.append(k)
    for i in code_slovo:
        random_bukva=random.randint(1000,5000)
        #print(random_bukva,"random_bukva")
        decode_slovo_in_eng.append(random_bukva)
        decode_slovo.append(i + random_bukva)
    for i in decode_slovo:
        code_slovo_in_eng.append(chr(i))
    for i in code_slovo_in_eng:
        code_slovo_in_eng_2 += i
    for i in decode_slovo_in_eng:
        decode_slovo_in_eng_2 += chr(i)

    tg_bot.reply_to(message, "     encoded message: " + code_slovo_in_eng_2)
    tg_bot.send_message(user_id, "     password: " + decode_slovo_in_eng_2)
    tg_bot.send_message(user_id, "/decode: " + code_slovo_in_eng_2 + "  password: " + decode_slovo_in_eng_2)

    print(x)
    print(code_slovo)
    print(decode_slovo)
    print(code_slovo_in_eng_2+"    "+str(len(code_slovo_in_eng_2)))
    print(decode_slovo_in_eng_2+"    "+str(len(decode_slovo_in_eng_2)))



#/decode: ˗˪ƸʧՐޑֻ֪  password: ɶɰŷɍĠ͂ƫŻ

@tg_bot.message_handler(commands=["decode:"])
def mesageEncoder(message:types.Message):

    encoded_message_code = []
    password_code = []
    decode_message_code = []
    decode_message = ""

    user_id = message.from_user.id
    message_text=message.text
    index_find=message_text.find("  password: ")#12

    encoded_message = message_text[9:index_find]
    password=message_text[index_find+12:]

    print(len(encoded_message))
    print(len(password))

    for i in encoded_message:
        encoded_message_code.append(ord(i))
    for i in password:
        password_code.append(ord(i))
    for i in range(len(encoded_message_code)):
        decode_message_code.append(encoded_message_code[i]-password_code[i])
    for i in decode_message_code:
        decode_message += chr(i)

    tg_bot.reply_to(message,"decoded message: "+decode_message)


    print(encoded_message)
    print(encoded_message_code)
    print(password)
    print(password_code)
    print(decode_message)
    print(decode_message_code)

tg_bot.polling()