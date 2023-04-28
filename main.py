from aiogram import types, Dispatcher, Bot, executor
import parser_apteka
import emoji
from config import TOKEN

BOT_TOKEN = TOKEN
bot = Bot(BOT_TOKEN)
disp = Dispatcher(bot)
cross = emoji.emojize(":cross_mark:")
medic = emoji.emojize(":green_heart:")

HELP_COMMAND = """
Основные команды для работы с ботом:
/start - начать работу с ботом
/help - основные команды для работы с ботом"""

START_COMMAND = """Этот бот - агрегатор лекарственных препаратов в аптеках города Омска. 
Чтобы найти информацию о необходимом препарате отправьте боту сообщение с его названием."""

FARMA_COMMAND = """Для поиска в сети аптек "Фармакопейка" 
отправьте боту сообщение с названием лекарственного средства"""

@disp.message_handler(commands= ['start'])
async def start_command(message: types.Message):
    await message.answer(text = START_COMMAND)

@disp.message_handler(commands= ['help'])
async def help_command(message: types.Message):
    await message.answer(text = HELP_COMMAND)

@disp.message_handler(content_types=['text'])
async def treatment(message: types.Message):
    await message.answer(text=f"{parser_apteka.parse(message.text)}")

async def on_startup(_):
    print('Бот успешно запущен!')

if __name__ == '__main__':
    executor.start_polling(dispatcher=disp, skip_updates=True, on_startup=on_startup)


#@disp.message_handler(commands= ['farmakopeika'])
#async def farma(message: types.Message):
#    await message.answer(text = FARMA_COMMAND)