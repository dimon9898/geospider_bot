import json
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
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
    
@user.callback_query(F.data == 'back_to_user_main')
async def back_to_user_main(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo=logo, 
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
    await callback.message.delete()
    file = FSInputFile('./files/Приемники.xlsx')
    await callback.message.answer_document(file, reply_markup=await kb.back_to_user_service_main_btn())


@user.callback_query(F.data == 'user_tariff')
async def user_tariff(callback: CallbackQuery):
    await callback.message.delete()
    file = FSInputFile('./files/Тарифы.png')
    await callback.message.answer_document(file, reply_markup=await kb.back_to_user_service_main_btn())

@user.callback_query(F.data == 'user_contacts')
async def user_contacts(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>🌐 Наши контакты</b>\n\n'
                                  '<b>👨‍💻 Техподдержка:</b>  <code>s@geospider.ru</code>\n'
                                  '<b>📩 Для обращений:</b>  <code>m@geospider.ru</code>\n'
                                  '<b>📞 Тел.:</b> +7 (812) 910-13-39\n'
                                  '<b>📬 E-mail:</b> <code>mail@geospider.ru</code>\n\n'
                                  '--------<b>Режим работы</b>--------\n\n'
                                  '▪︎ Пн. – Пт.: 9:00–18:00 \n'
                                  '▪︎ Сб, Вс.: выходные дни',
                                  reply_markup=await kb.back_to_user_main_btn(),
                                  parse_mode='HTML')    


@user.callback_query(F.data == 'user_connection')
async def user_connection(callback: CallbackQuery):
    await callback.message.answer('Нажмите на "Открыть" чтобы оставить заявку 👇',
                                  reply_markup=await kb.connect())

@user.message(F.web_app_data)
async def get_web_app_data(message: Message):
    user_data = json.loads(message.web_app_data.data)
    name = str(user_data['name'])
    email = str(user_data['email'])
    phone = str(user_data['phone'])
    await message.answer('Ваши данные:\n\n'
                         f'ФИО: {name}\n'
                         f'Email: {email}\n'
                         f'Тел: {phone}',
                         reply_markup=ReplyKeyboardRemove())    