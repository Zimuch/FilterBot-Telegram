import asyncio
from telethon import TelegramClient, events
from telegram import Bot
import logging

# --- CONFIGURAZIONE ---
API_ID =         # Inserisci il tuo API ID qui
API_HASH = ''     # Inserisci il tuo API HASH qui
BOT_TOKEN = ''   # Inserisci il tuo token del bot qui
MY_CHAT_ID =     # Inserisci il tuo ID chat qui

channels = ['example1', 'example2'] # Aggiungi qui i canali pubblici che desideri monitorare

keyword = ['keyword1' , 'keyword2'] # Aggiungi qui le parole chiave che desideri filtrare

# --- INIZIALIZZAZIONE ---
bot = Bot(token=BOT_TOKEN)
client = TelegramClient('session_name', API_ID, API_HASH)

# --- HANDLER TELETHON ---
@client.on(events.NewMessage(chats=channels))
async def handler(event):
    try:
        message = event.message.message
        message_id = event.message.id
        chat = event.message.chat

        # Creazione del messaggio
        if hasattr(chat, 'username') and chat.username:
            info = f"Puoi vedere il messaggio originale qui: https://t.me/{chat.username}/{message_id}"
        else:
            chat_title = getattr(chat, 'title', 'Sconosciuto')
            chat_id = getattr(chat, 'id', 'Sconosciuto')
            info = (
                "Messaggio da chat privata o senza username pubblico\n"
                f"Titolo chat: {chat_title}\n"
                f"ID chat: {chat_id}\n"
                f"ID messaggio: {message_id}"
            )

        found_keyword = next((k for k in keyword if k.lower() in message.lower()), None)
        if found_keyword:
            print(f"Keyword trovata: {found_keyword}. Invio messaggio in corso...")
            await bot.send_message(
                chat_id=MY_CHAT_ID,
                text=f"🔍 Keyword trovata: {found_keyword}!\n{info}"
            )
    except Exception as e:
        print(f"Errore nel handler: {e}")

# --- CICLO DI RICONNESSIONE INFINITA ---
async def main():
    while True:
        try:
            await client.start(bot_token=BOT_TOKEN)
            print("Connesso a Telegram, in ascolto...")
            await client.run_until_disconnected()
        except Exception as e:
            print(f"Errore di connessione: {e}")
            print("Riprovo tra 10 secondi...")
            await asyncio.sleep(10)

if __name__ == "__main__":

# --- LOGGING DEBUG ---
    logging.basicConfig(level=logging.WARNING) # Cambia il livello di logging a DEBUG per vedere più dettagli
    asyncio.run(main())
