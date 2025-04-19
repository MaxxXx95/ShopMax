import os
from telethon import TelegramClient, events

# Variabili ambiente da Railway
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
source_channel = int(os.getenv("SOURCE_CHANNEL"))     # esempio: -1001234567890
target_channel = os.getenv("TARGET_CHANNEL")          # esempio: @canaledestinazione

# Avvia client Telethon
client = TelegramClient('sessione', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        await client.send_message(target_channel, event.message)
        print("Messaggio copiato!")
    except Exception as e:
        print(f"Errore: {e}")

client.start()
print("Bot avviato. In ascolto...")
client.run_until_disconnected()