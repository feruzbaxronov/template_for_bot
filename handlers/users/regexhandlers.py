from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

EMAIL_REGEX=r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

@dp.message_handler(filters.Regexp(EMAIL_REGEX ))
async def text_email(msg:types.Message):
    await msg.reply("EMAIL qabul qilindi")


@dp.message_handler(filters.Regexp(PHONE_NUM ))
async def text_phone(msg:types.Message):
    await msg.reply("Telefon raqam qabul qilindi")