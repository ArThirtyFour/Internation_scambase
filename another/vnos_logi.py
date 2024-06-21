from datetime import datetime
from config import lang , cursor , chat_channel
def vnos_v_basy(id_author,arg):
    cursor.execute('DELETE FROM logi WHERE id_check  IS NULL')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO logi VALUES(?,?,?)',(id_author,arg,time))
    lang.commit()

def txt_file(id_user):
    all_zapis = cursor.execute('SELECT id_check , time FROM logi WHERE id_proverka = ?',(id_user,)).fetchall()
    if not all_zapis:
        with open(f'id_{id_user}.txt', 'w+' , encoding='utf-8') as file:
            file.write("Здесь ничего нет!/There's nothing here!")
    else:
        with open(f'id_{id_user}.txt', 'w+' , encoding='utf-8') as file:
            for row in all_zapis:
                com , time = row
                file.write(f'[!] Лог\n[+] Запрос :  {com} \n[+] Время:{time}\n\n')

def sub_check(bot,user_id):
    try:
        bot.get_chat_member(chat_id=chat_channel, user_id=user_id)
        return True
    except:
        return False
