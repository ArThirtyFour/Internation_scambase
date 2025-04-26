from random import choice
from time import sleep
from pyrogram import Client
from pyrogram.errors import UsernameNotOccupied
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from main import klava_resstr

    

chat_ids = [ ]
slovo_garant = ['Является 🥉Мини-Гарантом','Является 🥈Обычным Гарантом','Репутация: Гарант','Ему можно доверять']
slovo_scam = ['Находится в SCAM базе!','| Данный человек, является СКАМЕРОМ ','Репутация: СКАММЕР','Репутация: Петух','Репутация: Возможно Скаммер','Репутация: Плохая Репутация','Репутация: На рассмотрении']
slovo_admin = ['💙 Персонал GASD','Данный человек, является персоналом бота. [админ]','👑 | Звание: Владелец','🔫Является Старшим Администратором','Является младщим Администратором','👑Является Владельцем']
slovo_not = ['Является обычным пользователем.','Репутация: Проверен(а) гарантом',
             '| Данный человек, не является скамером',
             'Человека нет в базе!','📗 | coder']



def send_photo_base(message,chat_id,reply_markup):
    for i in app.get_chat_history(chat_id,limit=4):
        if i.text != None and i.from_user.id != app_id:
            text = i.text
        elif i.caption != None and i.from_user.id != app_id:
            text = i.caption
        for i in range(0,4):
            if text.count(slovo_garant[i]) > 0:
                message.reply_photo(photo=photo_garant,quote=True,caption=text,reply_markup=reply_markup)
            else:
                pass
        for i in range(0,6):
            if text.count(slovo_admin[i]) > 0:
                message.reply_photo(photo=photo_admin,quote=True,caption=text,reply_markup=reply_markup)
            else:
                pass
        for i in range(0,7):
            if text.count(slovo_scam[i]) > 0:
                message.reply_photo(photo=photo_scam,quote=True,caption=text,reply_markup=reply_markup)
            else:
                pass
        for i in range(0,5):
            if text.count(slovo_not[i]) > 0:
                message.reply_photo(photo=photo_not_in_base,quote=True,caption=text,reply_markup=reply_markup)
            else:
                pass


def check(bot, message):
    try:
        arg = message.text.split()[1]
        if arg[0] == '@':
            try:
                user_id = bot.get_users(user_ids=arg).id
                btn=InlineKeyboardMarkup([[InlineKeyboardButton('🟢 Вечная ссылка 🟢',url=f'tg://openmessage?user_id={user_id}')]])
                mess = bot.send_message(message.chat.id,'⚡️ Я отправил запрос! Время ожидания: +- 1 секунда ⚡️')
                chat_id = choice(chat_ids)
                app.delete_messages(chat_id,[i.id for i in app.get_chat_history(chat_id)])
                app.send_message(chat_id, f'/check {user_id}')
                sleep(1)
                bot.delete_messages(message.chat.id, mess.id)
                send_photo_base(message,chat_id,btn)
                bot.send_message(channel_logs,f'Мне пришел лог! Отправлял {message.from_user.id} запрос /check')
            except Exception as exo:
                bot.send_message(message.chat.id,f'❗️ Телеграмм вернул ошибку ❗️ \n- - - - - - - - - -\n{exo}')   
                bot.send_message(channel_logs,f'Мне пришел лог! Отправлял {message.from_user.id} запрос /check')
        elif arg[0] in [str(i) for i in range(0,10)]:
            btn=InlineKeyboardMarkup([[InlineKeyboardButton('🟢 Вечная ссылка 🟢',url=f'tg://openmessage?user_id={arg}')]])
            mess = bot.send_message(message.chat.id,'⚡️ Я отправил запрос! Время ожидания: +- 1 секунда ⚡️')
            chat_id = choice(chat_ids)
            app.delete_messages(chat_id,[i.id for i in app.get_chat_history(chat_id)])
            app.send_message(chat_id, f'/check {arg}')
            sleep(1)
            bot.delete_messages(message.chat.id, mess.id)
            send_photo_base(message,chat_id,btn)
            bot.send_message(channel_logs,f'Мне пришел лог! Отправлял {message.from_user.id} запрос /check')
        else:
            message.reply_text('Неправильно задан агрумент!', quote=True)
            bot.send_message(channel_logs,f'Мне пришел лог! Отправлял {message.from_user.id} запрос /check')
        return f'/check {arg}'
    except IndexError:
        bot.send_message(message.chat.id,'❗️ Агрумент не задан ❗️')
    



def check_you(bot,message):
    arg = message.from_user.id
    btn=InlineKeyboardMarkup([[InlineKeyboardButton('🟢 Вечная ссылка 🟢',url=f'tg://openmessage?user_id={message.from_user.id}')]])
    mess = bot.send_message(message.chat.id,'⚡️ Я отправил запрос! Время ожидания: +- 1 секунда ⚡️')
    chat_id = choice(chat_ids)
    app.delete_messages(chat_id,[i.id for i in app.get_chat_history(chat_id)])
    app.send_message(chat_id, f'/check {arg}')
    sleep(1)
    bot.delete_messages(message.chat.id, mess.id)
    send_photo_base(message,chat_id,btn)
    bot.send_message(channel_logs,f'Мне пришел лог! Отправлял {message.from_user.id} запрос /me')
    return f'/me'

def check_reestr(bot , message):
    try:
        arg = message.text.split()[1]
        if arg[0] == '@':
            try:
                user_id = bot.get_users(user_ids=arg).id
                info = cursor.execute('SELECT baze , proofs FROM garants WHERE user_id = ?',(user_id,)).fetchone()
                if info:
                    baze , proofs = info[0] , info[1]
                    message.reply_photo(photo=photo_in_reestr,quote=True,caption=f'✅ Данный пользователь находится в реестре гарантов ✅ \n💎 База - {baze} \n[👉 Ссылка на пруфы]({proofs})')
                else:
                    message.reply_text('❌ Данного пользователя нет в реестре.\n Мы рекомендуем проводить сделки с гарантом из реестра.❌',quote=True,reply_markup=klava_resstr)
            except:
                pass
        elif arg[0] in [str(i) for i in range(0,10)]:
            info = cursor.execute('SELECT baze , proofs FROM garants WHERE user_id = ?',(arg,)).fetchone()
            if info:
                baze , proofs = info[0] , info[1]
                message.reply_photo(photo=photo_in_reestr,quote=True,caption=f'✅ Данный пользователь находится в реестре гарантов ✅ \n💎 База - {baze} \n[👉 Ссылка на пруфы]({proofs})')
            else:
                message.reply_text('❌ Данного пользователя нет в реестре.\n Мы рекомендуем проводить сделки с гарантом из реестра.❌',quote=True,reply_markup=klava_resstr)
    except IndexError:
        pass
def check_resster_me(bot,message):
    id_user = message.from_user.id
    info = cursor.execute('SELECT baze , proofs FROM garants WHERE user_id = ?',(id_user,)).fetchone()
    if info:
        baze , proofs = info[0] , info[1]
        message.reply_photo(photo=photo_in_reestr,quote=True,caption=f'✅ Данный пользователь находится в реестре гарантов ✅ \n💎 База - {baze} \n[👉 Ссылка на пруфы]({proofs})')
    else:
        message.reply_text('❌ Данного пользователя нет в реестре.\n Мы рекомендуем проводить сделки с гарантом из реестра.❌',quote=True,reply_markup=klava_resstr)
def check_prepiska_me(bot , message):
    try:
        name = bot.get_users(user_ids=message.from_user.id).first_name + bot.get_users(user_ids=message.from_user.id).last_name
    except:
        name = bot.get_users(user_ids=message.from_user.id).first_name
    prepiski=['[ISB]','ɪsʙ','𝐈𝐒𝐁','ISᗷ','ＩＳＢ','丨丂乃']
    for i in range(0,len(prepiski)-1):
        if name.count(prepiski[i]) > 0:
            prepiska1 = prepiski[i]
            bot.send_message(message.chat.id,f'**{name} поддерживает борьбу с скамом и наш проект , поставив в ник --НАШУ ПРЕПИСКУ--**\n - - - - - - - - - - - - - - - \n(Нажмите на `{prepiska1}`, чтобы скопировать и поставить к себе в ник)')
            break
def check_prepiska(bot,message):
    try:
        arg = message.text.split()[1]
        if arg[0] == '@':
            arg = bot.get_users(user_ids=arg).id
        try:
            name = bot.get_users(user_ids=arg).first_name + bot.get_users(user_ids=arg).last_name
        except:
            name = bot.get_users(user_ids=arg).first_name
        prepiski=['[ISB]','ɪsʙ','𝐈𝐒𝐁','ISᗷ','ＩＳＢ','丨丂乃']
        for i  in range(0,len(prepiski)-1):
            if name.count(prepiski[i]) > 0:
                bot.send_message(message.chat.id,f'**{name} поддерживает борьбу с скамом и наш проект , поставив в ник --НАШУ ПРЕПИСКУ--**\n - - - - - - - - - - - - - - - \n(Нажмите на `{prepiski[i]}`, чтобы скопировать и поставить к себе в ник)')
                break
    except IndexError:
        pass
    except UsernameNotOccupied:
        pass