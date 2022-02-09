from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Feruz Baxronov  Botiga Xush kelibsiz\n Iltimos 2tadan ortiq so'z yuboring\n Ingliz or uzbek tilida")


