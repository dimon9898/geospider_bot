from aiogram.utils.keyboard import InlineKeyboardBuilder


async def user_main_kb():
    kb = InlineKeyboardBuilder()
    
    kb.button(text='📡 Сервисы', callback_data='user_service')
    kb.button(text='🌐 Наши контакты', callback_data='user_contacts')
    return kb.adjust(1).as_markup()

async def user_service_main_kb():
    kb = InlineKeyboardBuilder()
    
    kb.button(text='🛰️ Подключиться', callback_data='user_connection')
    kb.button(text='📊 Тарифы', callback_data='user_tariff')
    kb.button(text='📔 Поверки', callback_data='user_verification')
    kb.button(text='⬅️ назад', callback_data='back_to_user_main')
    return kb.adjust(1, 2).as_markup()

async def back_to_user_main_btn():
    kb = InlineKeyboardBuilder()
    kb.button(text='назад', callback_data='back_to_user_main')
    return kb.as_markup()

async def back_to_user_service_main_btn():
    kb = InlineKeyboardBuilder()
    kb.button(text='назад', callback_data='user_service')
    return kb.as_markup()
