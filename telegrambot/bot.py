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

async def get_latest_message(token: str) -> Optional[tuple]:
    """Simple function: give token, get latest message and chat_id back"""
    bot = TelegramBot(token)
    latest_message = await bot.check_new_messages()

    if latest_message and 'text' in latest_message:
        text = latest_message['text']
        chat_id = latest_message['chat']['id']
        return (text, chat_id)

    return None

async def send_reply(token: str, chat_id: int, message: str) -> bool:
    """Simple function: send message to chat_id"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        'chat_id': chat_id,
        'text': message
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result.get('ok', False)
            return False

async def main():
    TOKEN = "YOUR_BOT_TOKEN_HERE"

    # Get latest message
    result = await get_latest_message(TOKEN)
    if result:
        message_text, chat_id = result
        print(f"Latest message: {message_text}")

        # Send reply
        success = await send_reply(TOKEN, chat_id, "Hello back!")
        if success:
            print("Reply sent!")
    else:
        print("No new messages")

if __name__ == "__main__":
    asyncio.run(main())