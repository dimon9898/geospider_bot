import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.user import user

load_dotenv()

dp = Dispatcher()

async def main():
    bot = Bot(token=os.getenv('TG_TOKEN'))
    dp.include_routers(user)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())    