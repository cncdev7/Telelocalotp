from fastapi import FastAPI
from telethon import TelegramClient, events
import re

# Telegram API ma'lumotlari
API_ID = 11111111  # my.telegram.org'dan olingan API_ID
API_HASH = ""  # my.telegram.org'dan olingan API_HASH
PHONE_NUMBER = "+"  # O'z telefon raqamingizni kiriting

app = FastAPI()
client = TelegramClient("session_name", API_ID, API_HASH)
latest_code = None  # Oxirgi kodni saqlash uchun global o'zgaruvchi

@app.on_event("startup")
async def startup():
    """ Dastur ishga tushganda Telegram botini ishga tushirish """
    await client.start(PHONE_NUMBER)

    @client.on(events.NewMessage)
    async def handler(event):
        global latest_code
        if event.chat_id == 777000:  # Telegram rasmiy botining ID'si
            message = event.message.message
            code = re.findall(r'\b\d{5}\b', message)  # 5 xonali kodni ajratib olish
            if code:
                latest_code = code[0]
                print(f"Kelgan kod: {latest_code}")

    print("Telegram bot ishga tushdi...")
    await client.run_until_disconnected()

@app.get("/get_code")
def get_code():
    """ Oxirgi kelgan kodni qaytaruvchi API """
    return {"code": latest_code}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

