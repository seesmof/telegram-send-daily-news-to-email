from telethon import TelegramClient
import asyncio

TOKEN = "6055667715:AAGlgPKBJftI_Cks1m8n9n_rSpqhN5bXrzg"
CHANNEL_ID = "@mindua"
APP_ID = "29709258"
APP_HASH = "545b92e022b3885152a76625cd74c9d5"
client = TelegramClient('session_name', APP_ID, APP_HASH)


async def main():
    await client.start()
    channel = await client.get_entity(CHANNEL_ID)
    resulting_news = ''
    async for message in client.iter_messages(channel, search='#фотодня', limit=1):
        resulting_news += message.text
    resulting_news = resulting_news.replace('*', '')
    resulting_news = resulting_news.replace(' — у світлинах', '')
    resulting_news = resulting_news.replace(
        '[📱 Підписатись на Майнд пояснює](https://t.me/mindua)', '')
    resulting_news = resulting_news.replace(
        '#фотодня #дайджест #важливе', '')
    resulting_news = resulting_news.replace(
        'Повна інформаційна картина дня — на каналі [Mind tweet](https://t.me/mindUAtweet)', '')
    resulting_news = resulting_news.replace(
        '🛑', '- ')
    print(resulting_news)

if __name__ == '__main__':
    asyncio.run(main())
