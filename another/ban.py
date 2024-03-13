from sqlite3 import IntegrityError
from config import lang , cursor

def ban(user_id):
    try:
        cursor.execute('INSERT INTO banned VALUES(?)',(user_id,))
        lang.commit()
        return f'✅ Пользователь {user_id} был закрыт доступ к моду.✅'
    except IntegrityError:
        return f'❌ Данный пользовать ({user_id}) был уже заблокирован ❌'

def unban(user_id):
    cursor.execute("DELETE FROM banned WHERE user_id=?", (user_id,))
    lang.commit()
    return f'✅ Пользователь {user_id} был разблокирован доступ к моду.✅'

def check_ban(user_id):
    if cursor.execute('SELECT * FROM banned WHERE user_id=?',(user_id,)).fetchone() != None:
        return True
    else:
        return False