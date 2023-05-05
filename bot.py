import os

from telethon import TelegramClient, events
from telethon.tl.functions.channels import CreateChannelRequest


async def create_supergroup(title):
    api_id = os.environ.get('API_ID')
    api_hash = os.environ.get('API_HASH')

    phone_number = os.environ.get('PHONE_NUMBER')
    username = os.environ.get('USERNAME')
    async with TelegramClient(username, api_id, api_hash) as client:

        result = await client(CreateChannelRequest(
            title=title,
            about='',
            megagroup=True
        ))
