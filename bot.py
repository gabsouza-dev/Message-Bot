import schedule
import time
from twilio.rest import Client
from telegram import Bot

TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+1234567890'
DESTINATARIO_WHATSAPP = 'whatsapp:+9876543210'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_id'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def enviar_mensagem_whatsapp():
    message = client.messages.create(
        body="Aqui está sua mensagem agendada via WhatsApp!",
        from_=TWILIO_WHATSAPP_NUMBER,
        to=DESTINATARIO_WHATSAPP
    )
    print(f'Mensagem enviada no WhatsApp: {message.sid}')

def enviar_mensagem_telegram():
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Aqui está sua mensagem agendada via Telegram!")
    print('Mensagem enviada no Telegram!')

def enviar_mensagem():
    enviar_mensagem_whatsapp()
    enviar_mensagem_telegram()

schedule.every().day.at("14:00").do(enviar_mensagem)

print("Bot iniciado! Aguardando horários agendados...")

while True:
    schedule.run_pending()
    time.sleep(60)
