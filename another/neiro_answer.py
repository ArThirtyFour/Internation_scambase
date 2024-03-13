
from openai import OpenAI
from main.klavs import btn_preloshka
client = OpenAI(api_key='бери ключ', base_url="https://api.deepseek.com/v1")
list_scam_words = ['скам','скамер','кидок','кинул']
def check_scam(bot,message):
    for i in list_scam_words:
        if i in message.text.lower():
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "Ты помощник моей базы"},
                    {"role": "user", "content": "Напиши текст , будто пытаешся мне помочь. Обьем текста не больше 10 слов"},
                ]
            )
            text = response.choices[0].message.content.replace('"','').replace("'",'').strip()
            message.reply_text(f'**Ты написал что-то про скам?** \n\n{text} \n\n||⚠️ Данный текст написан нейросетью , так что может выдавать странные ответы. ⚠️||',quote=True,reply_markup=btn_preloshka)
            break