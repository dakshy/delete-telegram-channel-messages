# delete-telegram-channel-messages - A script written in Pyrogram framework to mass delete messages from a Telegram channel.
# Copyright (c) 2022 dakshy/delete-telegram-channel-messages
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os, asyncio
from dotenv import load_dotenv
from pyrogram import idle, Client

if os.path.exists('config.env'):
    load_dotenv('config.env')

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")
search_query = os.environ.get("SEARCH_QUERY")
channel_id = os.environ.get("CHANNEL_ID")

app = Client(
    "client",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)
app.start()

async def del_msg():
    async for message in app.search_messages(channel_id, query=search_query, limit=999):
        await message.delete()
        print("Deleted Message with ID:", message.id)
        await asyncio.sleep(0.5)

app.loop.run_until_complete(del_msg()) 
app.stop()