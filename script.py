import time
from telethon import TelegramClient, events, sync
import asyncio
from keep_alive import keep_alive
keep_alive()
# Account 1 details
api_id_1 = '22971206'
api_hash_1 = '680bc7929a4a41bc4ca6d6ef7d61d383'
phone_number_1 = '+4552766724'

# Account 2 details
api_id_2 = '26226785'
api_hash_2 = '264aea9b3fdb855c1ed17671934f9c49'
phone_number_2 = '+6777437478'

# Create clients for both accounts
client1 = TelegramClient('userbot1', api_id_1, api_hash_1)
client2 = TelegramClient('userbot2', api_id_2, api_hash_2)

async def send_messages(client, name):
    print(f"[{name}] Starting send_messages function...")
    await client.start()

    # Get all dialogs (chats)
    dialogs = await client.get_dialogs()
    print(f"[{name}] Got {len(dialogs)} dialogs.")

    while True:
        for dialog in dialogs:
            if dialog.is_group:  # Check if the dialog is a group
                try:
                    await client.send_message(dialog, f'Dev/Admin please let everyone know that Raydium is very slow right now, and buys are not going through.\n\nPeople need to start using trading bots such as @bonkbot_bot (https://t.me/TheBonkBot) !!\n\nDon’t waste time with Raydium or Jupiter.. Use @bonkbot_bot (https://t.me/TheBonkBot)')
                    print(f'[{name}] Sent message to {dialog.title}')
                except Exception as e:
                    print(f'[{name}] Failed to send message to {dialog.title}: {e}')
                await asyncio.sleep(3)  # Wait for 3 seconds

        print(f'[{name}] Completed sending messages to all groups. Waiting for 5 minutes...')
        await asyncio.sleep(300)  # Wait for 5 minutes

async def send_messagesacc2(client, name):
    print(f"[{name}] Starting send_messages function...")
    await client.start()

    # Get all dialogs (chats)
    dialogs = await client.get_dialogs()
    print(f"[{name}] Got {len(dialogs)} dialogs.")

    while True:
        for dialog in dialogs:
            if dialog.is_group:  # Check if the dialog is a group
                try:
                    await client.send_message(dialog, f'Yes you’re 100% right..\n\nDon’t waste time with Raydium or Jupiter.. Use @bonkbot_bot instead!')
                    print(f'[{name}] Sent message to {dialog.title}')
                except Exception as e:
                    print(f'[{name}] Failed to send message to {dialog.title}: {e}')
                await asyncio.sleep(3)  # Wait for 3 seconds

        print(f'[{name}] Completed sending messages to all groups. Waiting for 5 minutes...')
        await asyncio.sleep(300)  # Wait for 5 minutes

async def main():
    # Start both clients synchronously
    print("Starting clients...")
    await client1.start()
    print(f"Account 1 ({phone_number_1}) started successfully.")
    await client2.start()
    print(f"Account 2 ({phone_number_2}) started successfully.")

    # Run tasks for both accounts concurrently
    task1 = asyncio.create_task(send_messages(client1, "Account 1"))
    task2 = asyncio.create_task(send_messagesacc2(client2, "Account 2"))

    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
