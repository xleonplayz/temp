import asyncio
import aiohttp
import json
from typing import Optional, List, Dict

class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.offset = 0

    async def get_updates(self, timeout: int = 30) -> List[Dict]:
        """Fetch new messages from Telegram"""
        url = f"{self.base_url}/getUpdates"
        params = {
            'offset': self.offset,
            'timeout': timeout,
            'limit': 100
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if data['ok']:
                        updates = data['result']
                        if updates:
                            self.offset = updates[-1]['update_id'] + 1
                        return updates
                    else:
                        print(f"API Error: {data['description']}")
                        return []
                else:
                    print(f"HTTP Error: {response.status}")
                    return []

    async def send_message(self, chat_id: int, text: str) -> bool:
        """Send a message to a chat"""
        url = f"{self.base_url}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': text
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['ok']
                return False

    async def check_new_messages(self) -> Optional[Dict]:
        """Check for new messages and return the latest one"""
        updates = await self.get_updates(timeout=1)

        if updates:
            # Get the latest message from the updates
            latest_update = updates[-1]
            if 'message' in latest_update:
                return latest_update['message']

        return None

    def process_message(self, message: Dict) -> None:
        """Process incoming message"""
        if 'text' in message:
            chat_id = message['chat']['id']
            text = message['text']
            user = message.get('from', {})
            username = user.get('username', 'Unknown')

            print(f"[{username}] {text}")

            # Echo the message back
            asyncio.create_task(self.send_message(chat_id, f"Echo: {text}"))

    async def start_polling(self):
        """Start polling for messages"""
        print("Bot started. Polling for messages...")

        while True:
            try:
                updates = await self.get_updates()

                for update in updates:
                    if 'message' in update:
                        self.process_message(update['message'])

            except Exception as e:
                print(f"Error: {e}")
                await asyncio.sleep(5)

# Example usage of check_new_messages function
async def check_for_new_message():
    TOKEN = "YOUR_BOT_TOKEN_HERE"
    bot = TelegramBot(TOKEN)

    latest_message = await bot.check_new_messages()

    if latest_message:
        print("New message found:")
        if 'text' in latest_message:
            user = latest_message.get('from', {})
            username = user.get('username', 'Unknown')
            text = latest_message['text']
            print(f"[{username}] {text}")
        return latest_message
    else:
        print("No new messages")
        return None

async def main():
    # Replace with your bot token
    TOKEN = "YOUR_BOT_TOKEN_HERE"

    bot = TelegramBot(TOKEN)

    # Option 1: Use the new check function
    # latest_message = await bot.check_new_messages()
    # if latest_message:
    #     print("Latest message:", latest_message)

    # Option 2: Start continuous polling
    await bot.start_polling()

if __name__ == "__main__":
    asyncio.run(main())