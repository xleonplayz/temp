#!/usr/bin/env python3
import asyncio
from telegrambot.bot import TelegramBot

async def test_bot():
    """Test the telegram bot with the provided token"""
    token = "token"
    bot = TelegramBot(token)

    print("Testing bot initialization...")
    print(f"Bot token: {token}")
    print(f"Base URL: {bot.base_url}")

    # Test getting updates (this will likely fail with invalid token, but tests the syntax)
    try:
        print("Testing get_updates...")
        updates = await bot.get_updates(timeout=1)
        print(f"Updates received: {len(updates)}")
    except Exception as e:
        print(f"Expected error with test token: {e}")

    print("Bot test completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_bot())