#!/usr/bin/env python3
import asyncio
from telegrambot.bot import get_latest_message, send_reply

async def test_functions():
    """Test the standalone functions"""
    token = "token"

    print("Testing get_latest_message...")
    try:
        result = await get_latest_message(token)
        if result:
            message_text, chat_id = result
            print(f"Latest message: {message_text} from chat: {chat_id}")
        else:
            print("No new messages (expected with test token)")
    except Exception as e:
        print(f"Expected error with test token: {e}")

    print("Testing send_reply...")
    try:
        success = await send_reply(token, 12345, "Test message")
        print(f"Send reply result: {success}")
    except Exception as e:
        print(f"Expected error with test token: {e}")

    print("Function tests completed!")

if __name__ == "__main__":
    asyncio.run(test_functions())