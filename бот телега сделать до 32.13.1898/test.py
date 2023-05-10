

alf_list_num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(alf_list_num[9])



    alf=string.ascii_letters
    for i in alf:
        alf_list_en.append(i)#52

    for i in alf_list_num:
        alf_list_num_str+=i

    for i in encoding_message:
        encoding_message1.append(i)

    for i in range(len(encoding_message1)):
        i_temp = 0
        if encoding_message1[i] in alf_list_num:
            index_find_num=alf_list_num_str.find(encoding_message1[i])
            #print(index_find_num)
            if index_find_num + int(password) >= len(alf_list_num):
                i_temp=abs(len(alf_list_num)-(index_find_num + int(password)))
                print(1)
            else:
                i_temp=index_find_num + int(password)
                print(0)
            #print(str(i_temp)+"                       i_temp")
            #print(str(alf_list_num[i_temp])+"                       alf_list_num")
            encoded_message.append(alf_list_num[i_temp])
    tg_bot.send_message(user_id, "encoded message: " + str(encoded_message))
    #    i_temp=i
    #    if encoding_message[i] in alf_list_en:
    #        if i + password > len(alf_list_en):
    #            i_temp=-(len(alf_list_en)-1)
    #        encoded_message.append()


    #print(alf_list_ru)
    #print(alf_list_en)
    print(encoding_message)
    print(password)
    print(encoded_message)
#@tg_bot.message_handler(commands=["decode:"])
#def mesageEncoder(message: types.Message):
#





























msg = 'rGMTLIVrHIQSGIEWIVGIEWIV'  # encrypted msg
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for k in range(len(LETTERS)):
    transformation = ''
    for s in msg:
        if s in LETTERS:
            n = LETTERS.find(s)
            n = n - k
            if n < 0:
                n = n + len(LETTERS)
            transformation = transformation + LETTERS[n]

        else:
            transformation = transformation + s

tg_bot.send_message(user_id, "encoded message: " + str(transformation)))