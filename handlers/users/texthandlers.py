from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(contains="assalom",ignore_case=True))
@dp.message_handler(Text(equals='assalomu alaykum', ignore_case=True ))
async def text_example(msg:types.Message):
    await msg.reply("Valaykum assalom")

@dp.message_handler(Text(contains="ahmoq",ignore_case=True))
async def text_example(msg:types.Message):
    await msg.reply("o'zing ahmoq...")
