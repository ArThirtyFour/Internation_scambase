import os

from pyrogram import filters
from datetime import datetime 

from main import *
from another import *
from config import botur , cursor , lang , owner_id , zam_id
from main.clava_obra import clava


@botur.on_message(filters.command('start'))
def da(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        lan=cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()
        if lan == None:
            cursor.execute('INSERT INTO users VALUES (?)',(message.from_user.id))
            lang.commit()
            da(bot,message)
        else:
            bot.send_message(message.chat.id,f'✋ > Привет , {message.from_user.first_name}\n👮 > Я мод для проверки по 3 базам на скам.\n🆔 > Твой ID: {message.from_user.id}\n❗️ > За помощью пиши - /help',reply_markup=klava_ru1)
    else:
        clava_sub(bot,message)


@botur.on_message(filters.command('check'))
def check_1(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        try:
            lan = cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()[0]
        except TypeError:
            cursor.execute('INSERT INTO users VALUES (?)',(message.from_user.id))
            lang.commit()
            lan = cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()[0]
        except AttributeError:
            lan = cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()[0]
            lang.commit()
        finally:
            arg = check(bot,message)
            check_reestr(bot,message)
            check_prepiska(bot,message)
            vnos_v_basy(message.from_user.id,arg)         
    else:
        clava_sub(bot,message)
        
    


@botur.on_message(filters.command('info'))
def info(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        lan=cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()
        if lan == None:
            cursor.execute('INSERT INTO users VALUES (?)',(message.from_user.id,))
            lang.commit()
            info(bot,message)
        else:
            subs = cursor.execute('SELECT COUNT(id) FROM users').fetchone()[0]
            zapos = cursor.execute('SELECT COUNT(id_check) FROM logi').fetchone()[0]
            bot.send_message(message.chat.id,f'> 🕒 С создания прошло {(datetime.now() - datetime(2024, 1,20)).days} дней \n\n> 📈 Версия 1.5 \n\n> 🔎 Мной пользуются {subs} человек\n\n> 💬 Ко мне обращались {zapos} раз\n\n> ✅ В нашем реестре  {find_number_garants()} гарантов\n\n> 👇 Вот интересные ссылки на конец',reply_markup=klava_ru2)
    else:
        clava_sub(bot,message)
@botur.on_message(filters.command('help'))
def help(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        lan=cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()
        if lan == None:
            cursor.execute('INSERT INTO users VALUES (?,?)',(message.from_user.id,))
            lang.commit()
            help(bot,message)
        else:
            bot.send_message(message.chat.id,'Смотри что могу!\n| /start > Запуск\n| /info > Информация \n| /check (id/@) > Проверка по пользователю \n| /me > Проверка самого себя.\n| /history > История запросов твоего аккаунта \n| /garants > Открытие реестра гарантов')
    else:
        clava_sub(bot,message)
        


@botur.on_message(filters.command('me'))
def check_u(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        try:
            lan = cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()[0]
        except TypeError:
            cursor.execute('INSERT INTO users VALUES (?)',(message.from_user.id,))
            lang.commit() 
            lan = cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()[0]
        finally:
            arg = check_you(bot,message)
            check_resster_me(bot,message)
            check_prepiska_me(bot,message)
            vnos_v_basy(message.from_user.id,arg)
    else:
        clava_sub(bot,message)
@botur.on_message(filters.command('history'))
def history(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        try:
            lan = cursor.execute('SELECT * FROM users WHERE id =?',(message.from_user.id,)).fetchone()[0]
        except:
            cursor.execute('INSERT INTO users VALUES (?)',(message.from_user.id))
            lang.commit()
            history(bot,message)
        finally:
            bot.send_message(message.chat.id,'📋 Ищу твои запросы...')
            txt_file(message.from_user.id)
            bot.send_document(message.chat.id, f"id_{message.from_user.id}.txt", caption="✏️ Вот твоя история запросов!")
            os.remove(f'id_{message.from_user.id}.txt')  
    else:
        clava_sub(bot,message)
@botur.on_message(filters.command('garants'))
def listur(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        send_reestr(bot,message)
    else:
        clava_sub(bot,message)
@botur.on_message(filters.command('send'))
def rasskilka(bot,message):
    if message.from_user.id == owner_id:
        all_sends = 0
        all_users = cursor.execute('SELECT id FROM users').fetchall()
        text=" ".join(message.text.split()[1:])
        for i in all_users[::-1]:
            try:
                bot.send_message(i[0],text)
                all_sends += 1
            except:
                pass
        bot.send_message(message.chat.id,f'✅ Рассылка окочена я переслал {all_sends}')

@botur.on_message(filters.command('ban'))
def banned(bot,message):
    if message.from_user.id ==  owner_id:
        try:
            id = int(message.text.split()[1])
            bot.send_message(message.chat.id, ban(id) )
        except ValueError:
            bot.send_message(message.chat.id,'❗️ Мне айди нужен для бана ❗️ ')
    else:
        bot.send_message(message.chat.id,'❌ Вы не имеете прав ❌')
@botur.on_message(filters.command('unban'))
def banned(bot,message):
    if message.from_user.id == owner_id:
        try:
            id = int(message.text.split()[1])
            bot.send_message(message.chat.id, unban(id) )
        except ValueError:
            bot.send_message(message.chat.id,'❗️ Мне айди нужен для разбана ❗️ ')
    else:
        bot.send_message(message.chat.id,'❌ Вы не имеете прав ❌')
@botur.on_message(filters.command('addgarant'))
def add_garant1(bot,message):
    if message.from_user.id == owner_id or message.from_user.id == zam_id:
        try:
            da = message.text.split('|')
            id_g , baza , proofs = da[1].strip() , da[2].strip() , da[3].strip()
            if id_g[0] == '@':
                id_g = bot.get_users(user_ids=id_g).id
            bot.send_message(message.chat.id,add_garant(id_g,baza,proofs))
        except IndexError:
            bot.send_message(message.chat.id,'❗️ Неправильно задан агрумент ❗️')

@botur.on_message(filters.command('delgarant'))
def del_garant1(bot,message):
    if message.from_user.id == owner_id or message.from_user.id == zam_id:
        try:
            arg = message.text.split()[1]
            if arg[0] == '@':
                arg = bot.get_users(user_ids=arg).id
            bot.send_message(message.chat.id,delete_garant(arg))
        except IndexError:
            bot.send_message(message.chat.id,'❗️ Неправильно задан агрумент ❗️')

@botur.on_message(filters.group)
def da_i(bot,message):
    check_scam(bot,message)
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        clava(bot,message)
@botur.on_message()
def d(bot,message):
    if sub_check(bot,message.from_user.id) and not check_ban(message.from_user.id):
        clava(bot,message)


app.start()
botur.run()
