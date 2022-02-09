from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

SUPERUSERS=[1311531305]
BLACKLIST=[5061669131]

@dp.message_handler(chat_id="1311531305", commands="start")
async def id_filter_example(msg:types.Message):
    await msg.answer("XUSH KELIPSIZ ADMIN")