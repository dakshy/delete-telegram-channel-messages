from pyrogram import Client

api_id   = input("Enter the API ID: ")
api_hash = input("Enter API HASH: ")

app = Client("client",api_id=api_id, api_hash=api_hash, in_memory=True)

async def main():
    async with app:
        string_session = await app.export_session_string()
        print("SESSION STRING:\n", string_session)

app.run(main())