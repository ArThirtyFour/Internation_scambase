import os
from datetime import datetime
from config import cursor
from main.check import check_you , check_resster_me , check_prepiska_me
from main.klavs import *
from another.vnos_logi import txt_file , vnos_v_basy
from another.garants import send_reestr , find_number_garants

def clava(bot,message):
    zapos = cursor.execute('SELECT COUNT(id_check) FROM logi').fetchone()[0]
    subs = cursor.execute('SELECT COUNT(id) FROM users').fetchone()[0]
    if message.text == '📓 Информация об проекте 📓':
       bot.send_message(message.chat.id,f'> 🕒 С создания прошло {(datetime.now() - datetime(2024, 1,20)).days} дней \n\n> 📈 Версия 1.5 \n\n> 🔎 Мной пользуются {subs} человек\n\n> 💬 Ко мне обращались {zapos} раз\n\n> ✅ В нашем реестре  {find_number_garants()} гарантов\n\n> 👇 Вот интересные ссылки на конец',reply_markup=klava_ru2)
    
    
    elif message.text == '❗️ Помощь ❗️':
        bot.send_message(message.chat.id,'Смотри что могу!\n| /start > Запуск\n| /info > Информация \n| /check (id/@) > Проверка по пользователю \n| /me > Проверка самого себя.\n| /history > История запросов твоего аккаунта \n| /garants > Открытие реестра гарантов')
    
    
    elif message.text == '🔍 Проверка самого себя 🔍':
        arg = check_you(bot,message)
        check_resster_me(bot,message)
        check_prepiska_me(bot,message)
        vnos_v_basy(message.from_user.id,arg)
    
    
    elif message.text == '🆔 Проверка пользователя 🔡':
        bot.send_message(message.chat.id,'📪 Для того чтоб проверить вводи /check [ID/@Username] 📪')
 

    elif message.text == '📄 Получить историю запросов':
        bot.send_message(message.chat.id,'📋 Ищу твои запросы...')
        txt_file(message.from_user.id)
        bot.send_document(message.chat.id, f"id_{message.from_user.id}.txt", caption="✏️ Вот твоя история запросов!")
        os.remove(f'id_{message.from_user.id}.txt')
    
    elif message.text == '❓ FAQ ❓':
        bot.send_message(message.chat.id,faq_ru)
    
    elif message.text == '📒 Реестр гарантов ✅' or message.text == '📒 Register of guarantors ✅':
        send_reestr(bot,message)