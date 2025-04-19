from telethon import TelegramClient

api_id = 123456
api_hash = 'abc123def456'

client = TelegramClient('sessione', api_id, api_hash)

async def main():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(f'{dialog.name} - {dialog.id}')

with client:
    client.loop.run_until_complete(main())