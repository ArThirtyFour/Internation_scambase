from sqlite3 import IntegrityError
from time import sleep
from config import lang , cursor , botur , photo_reestr_logo
from main.klavs import klava_resstr
def add_garant(user_id , baze , proofs ):
    try:
        cursor.execute('INSERT INTO garants VALUES(?,?,?)',(user_id,baze,proofs))
        lang.commit()
        return f'✅ Пользователь {user_id} был добавлен в реестр✅'
    except IntegrityError:
        return f'❌ Данный пользовать ({user_id}) был уже добавлен ❌'

def delete_garant(user_id):
    cursor.execute("DELETE FROM garants WHERE user_id=?", (user_id,))
    lang.commit()
    return f'✅ Пользователь {user_id} был удален из реестра.✅'


def list_garant():
    stats = ''
    all_garant = cursor.execute('SELECT * FROM garants').fetchall()
    for id_garant , baze , proofs in all_garant:
        try:
            fist_name = botur.get_users(user_ids=id_garant).first_name
        except:
            fist_name = 'Не удалось получить имя'
        url_garant = f"[{fist_name}](tg://openmessage?user_id={id_garant}) "
        url_proofs = f"[Ссылка на пруфы]({proofs}) "
        stats = stats + (f"| 👤 Гарант: {url_garant}\n| 💎 База: {baze} \n| 👉 {url_proofs} \n - - - - - - - - \n")
    return stats 
def send_reestr(bot, message):
    first_message = bot.send_photo(message.chat.id, photo=photo_reestr_logo ,caption='📰 Я смотрю реестр , подождите...')
    sleep(3)
    bot.edit_message_text(message.chat.id,first_message.id, list_garant(),reply_markup=klava_resstr)
def find_number_garants():
    return cursor.execute('SELECT COUNT(user_id) FROM garants').fetchone()[0]