from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.sync import TelegramClient, events
import re

# Setting configuration values
api_id = '5786597'
api_hash = '6bd8ac6d6e6f91b6b02d08c9c7545c42'
phone = '+918287742673'
username = 'khu_shi08'

client = TelegramClient(username, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))


chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

source_group = next(
    (chat for chat in chats if int(chat.id) == 1189021166), None)
second_source_group = next(
    (chat for chat in chats if int(chat.id) == 1455095644), None)
third_source_group = next(
    (chat for chat in chats if int(chat.id) == 1427274960), None)
target_group = next(
    (chat for chat in chats if int(chat.id) == 596451463), None)


@client.on(events.NewMessage(source_group))
async def main(event):
    message = event.message.message
    if("delhi" in message.lower() or
        ("available" in message.lower() and "?" not in message) or
            re.search("\b(D|d|ND) *(:|-)", message)):
        await client.send_message(596451463, "**"+source_group.title+'**\n\n'+event.message.message)


@client.on(events.NewMessage(second_source_group))
async def main(event):
    message = event.message.message
    if("delhi" in message.lower() or
        ("available" in message.lower() and "?" not in message) or
            re.search("\b(D|d|ND) *(:|-)", message)):
        await client.send_message(596451463, "**"+second_source_group.title+'**\n\n'+event.message.message)


@client.on(events.NewMessage(third_source_group))
async def main(event):
    message = event.message.message
    if("delhi" in message.lower() or
        ("available" in message.lower() and "?" not in message) or
            re.search("\b(D|d|ND) *(:|-)", message)):
        await client.send_message(596451463, "**"+third_source_group.title+'**\n\n'+event.message.message)

client.run_until_disconnected()
print('Members scraped successfully.')
