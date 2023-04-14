import logging

from aiogram import Bot, Dispatcher, executor, types
# from aiogram.methods.send_audio import SendAudio

API_TOKEN = '5957160345:AAHSojKtcnuM61tMq3djdwdIp3pxZztp4Bk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    # await message.answer(message.text)  
    if message.text =="phonk":
        await bot.send_audio(message.chat.id, open('phonk.mp3', 'rb'))
    if message.text =="soul":
        await bot.send_audio(message.chat.id, open('George Michael - Careless Whisper.mp3', 'rb'))
    if message.text =="Shinunoga":
        await bot.send_audio(message.chat.id, open('Shinunoga.mp3', 'rb'))
    if message.text =="bbs":
        await bot.send_audio(message.chat.id, open('bbs.mp3', 'rb'))
    if message.text =="снов":
        await bot.send_audio(message.chat.id, open('снов.mp3', 'rb'))
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)