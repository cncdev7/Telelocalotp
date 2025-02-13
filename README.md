# Telegram OTP Koder Bot
Telelocalotp
Bu loyiha **Telethon** kutubxonasidan foydalangan holda Telegramdan keladigan **OTP (One-Time Password)** kodlarini avtomatik ravishda o'qib olish va ekranga chiqarish uchun yaratilgan.

## Xususiyatlari
- **Telegram'ga ulanadi** va yangi xabarlarni kuzatib boradi.
- **Rasmiy Telegram botidan kelgan OTP kodlarini avtomatik ajratib oladi.**
- **Foydalanuvchiga tasdiqlash kodini ko'rsatadi.**

## O'rnatish
1. **Python 3** o'rnatilganligiga ishonch hosil qiling.
2. **Telethon** kutubxonasini o'rnating:
   ```bash
   pip install telethon
   ```
3. Loyiha fayllarini yuklab oling yoki klon qiling:
   ```bash
   git clone https://github.com/cncdev7/Telelocalotp.git
   cd repository
   ```
4. **API_ID va API_HASH** ni o'zgartiring:
   - [my.telegram.org](https://my.telegram.org) sahifasiga kiring va **API_ID** hamda **API_HASH** oling.
   - `main.py` faylida **API_ID**, **API_HASH**, va **PHONE_NUMBER** ni o'zingizga mos ravishda o'zgartiring.

## Ishga tushirish
Loyihani ishga tushirish uchun terminal yoki CMD'da quyidagilarni bajaring:
```bash
python main.py
```

## Loyiha Tuzilishi
```
📂 Telegram-OTP-Bot
│── app.py           # Asosiy bot kodi
│── requirements.txt  # Kutubxonalar ro'yxati
│── README.md        # Loyihaning tavsifi
```

## Muallif
- **Ismingiz yoki GitHub profilingiz**
- Telegram: [@cncdev7 ](https://t.me/cncdev7)

## Litsenziya
Bu loyiha **MIT** litsenziyasi ostida tarqatiladi.

