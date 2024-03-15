import sqlite3
from pyrogram import Client 
from pyrogram import enums

botur = Client('bdshka',api_id=123456,api_hash="хуй", bot_token='да')
lang = sqlite3.connect('users.db',check_same_thread=False)
cursor = lang.cursor()
botur.set_parse_mode(enums.ParseMode.MARKDOWN)

lang.commit()


owner_id = 1234567
zam_id = 9876542
photo_reestr_logo = 'https://raw.githubusercontent.com/ArThirtyFour/antiscambaza_RB/main/pictures/reestr_logo.jpg'
photo_admin = 'https://raw.githubusercontent.com/ArThirtyFour/antiscambaza_RB/main/pictures/admin.jpg'
photo_garant ='https://raw.githubusercontent.com/ArThirtyFour/antiscambaza_RB/main/pictures/garant.jpg'
photo_not_in_base = 'https://raw.githubusercontent.com/ArThirtyFour/antiscambaza_RB/main/pictures/notbase.jpg'
photo_scam = 'https://raw.githubusercontent.com/ArThirtyFour/antiscambaza_RB/main/pictures/scam.jpg'
photo_in_reestr = 'https://raw.githubusercontent.com/ArThirtyFour/antiscambaza_RB/main/pictures/in_reestr.jpg'
