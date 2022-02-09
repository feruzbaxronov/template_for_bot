from aiogram import types
from aiogram.dispatcher import filters

from loader import dp
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async  def photo_handler(msg:types.Message):
    await msg.answer("Bu Nima Rasm?")


@dp.message_handler(content_types="sticker")
async def emoji_handler(msg:types.Message):
    await msg.answer("😉")

@dp.message_handler(content_types="contact")
async def contact_handler(msg:types.Message):
    await msg.answer("kimning contacti bu?")

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def audio_handler(msg:types.Message):
    await msg.answer("Uzr ovozigizni yaxshi eshitaolmadim")







