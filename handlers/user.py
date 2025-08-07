from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import Router, F
from aiogram.filters import CommandStart
import keyboards.user_kb as kb

user = Router() 
logo = FSInputFile('./img/spider.jpg')

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(photo=logo, 
                               caption='Добро пожаловать!\n\n'
                               'Уникальная спутниковая сеть дифференциальных\n<b>(базовых | опорных | референцных)</b> геодезических станций - <b>"ГЕОСПАЙДЕР"!</b>\n\n📢 Работы по расширению сети продолжаются.\n\n'
                               'Я бот-Геоспайдер 🕷️\n',
                               parse_mode='HTML',
                               reply_markup=await kb.user_main_kb())

@user.callback_query(F.data == 'user_service')
async def user_service(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>📡 Сервисы</b>\n\n'
                                  'Выберите действие: ',
                                  reply_markup=await kb.user_service_main_kb(),
                                  parse_mode='HTML')    

@user.callback_query(F.data == 'user_verification')
async def user_verification(callback: CallbackQuery):
    await callback.answer()
    file = FSInputFile('./files/приемники.xlsx')
    await callback.message.answer_document(file, reply_markup=await kb.user_main_kb(), caption='ПРИЕМНИКИ')    