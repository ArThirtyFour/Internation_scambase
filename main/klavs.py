from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup , ReplyKeyboardMarkup


klava_ru1 = ReplyKeyboardMarkup([
    [('📓 Информация об проекте 📓'),('❗️ Помощь ❗️')],
    [('🔍 Проверка самого себя 🔍'),('🆔 Проверка пользователя 🔡')],
    [('❓ FAQ ❓'),('📄 Получить историю запросов')],
    [('📒 Реестр гарантов ✅')]
],one_time_keyboard=False,resize_keyboard=True)


btn1 = InlineKeyboardButton('➕ Добавление бота в чат ➕', url='https://t.me/ISB_SCAMCheckbot?startgroup=new')
btn2 = InlineKeyboardButton('📭 Чат мода',url='https://t.me/chat_ISB')
btn3 = InlineKeyboardButton('👨‍💻 Создатель 👨‍💻', url='https://t.me/AR_34_2')
btn4 = InlineKeyboardButton('📘Источник №1', url='https://t.me/AntiScamDatabaseBot')
btn5 = InlineKeyboardButton('📒Источник №2', url='https://t.me/Scam_Alert_SA_bot')
btn6 = InlineKeyboardButton('📕Источник №3',url='https://t.me/RB_CheckRatixBot')
klava_ru2 = InlineKeyboardMarkup([[btn1,btn2],[btn3],[btn4,btn5,btn6]])



def clava_sub(bot,message):
    klava_sub = InlineKeyboardMarkup([[InlineKeyboardButton('📃 Канал 📃', url='https://t.me/internation_scambaseRB')]])
    bot.send_message(message.chat.id,'❗️ Чтобы пользоваться ботом надо подписаться на канал ❗️',reply_markup=klava_sub)

klava_resstr = InlineKeyboardMarkup([[InlineKeyboardButton('📭 Заявление в реестр 📭', url='https://t.me/chat_ISB/399')]])

btn_preloshka = InlineKeyboardMarkup([
    [InlineKeyboardButton('❗️ Слить скамера в базу №1 ❗️',url='t.me/GasdReport')],
    [InlineKeyboardButton('❗️ Слить скамера в базу №2 ❗️',url='t.me/Scam_Alert_Base_Predlog/1845346')],
    [InlineKeyboardButton('❗️ Слить скамера в базу №3 ❗️',url='t.me/PredlogRatixBase/1')]
])

faq_ru = '''
Здесь ответы на самые частые вопросы (а также возможные)
 - - - - - - - - - - - - - - - - - - - - - -
❓ > У меня некоторые базы не присылают ответ.
👉 > Это может быть связано с не ответом баз. Здесь уже не мои проблемы.
 - - - - - - - - - - - - - - - - - - - - - -
❓ > А почему это мод , а не база?
👉 > У меня бот инфу у других баз фактический являсь модификацией для баз.
В свою очередь база берет информацию из своей. 
 - - - - - - - - - - -
❓ > Что такое реестр гарантов?
👉 > Фактический это список всех гарантов (независмо от базы). 
Попасть туда можно подав заявку на попдание ее реестр. 
 - - - - - - - - - - -
❗️ > Ответы в будущем могут добавлятся
'''

