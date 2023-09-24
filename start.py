import os

from dotenv import load_dotenv

import telebot

from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import engine

from database.models import Wires
from database.models import HeadCarDEvices, MotorCarDEvices, TrailerCarDEvices

from keyboard_mixin import KeyboardMixin as kb

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
bot = telebot.TeleBot(token)
# Хранится тип вагона, который выбрал пользователь.
TCFU = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Привет',
        reply_markup=kb.main_markup()
        )


@bot.message_handler()
def get_data_from_basic_keyboard(message):
    if message.text == 'Провода':
        bot.send_message(message.chat.id, 'Введите номер провода')
        bot.register_next_step_handler(message, wires)
    elif message.text == 'Аппараты в шкафах':
        bot.send_message(
            message.chat.id,
            'Выберите тип вагона',
            reply_markup=kb.markup_type_car_for_dev_in_cab()
            )
    elif message.text == 'Все предохранители в шкафу':
        bot.send_message(
            message.chat.id,
            'Выберите тип вагона',
            reply_markup=kb.markup_fuses()
            )


@bot.callback_query_handler(func=lambda _: True)
def query_type_car_for_dev_in_cab(call):
    if call.data == 'motor_car_for_devices':
        TCFU[call.message.chat.id] = MotorCarDEvices
        bot.send_message(call.message.chat.id, 'Введите название аппарата')
        bot.register_next_step_handler(call.message, devices_in_cabinets)
    elif call.data == 'head_car_for_devices':
        TCFU[call.message.chat.id] = HeadCarDEvices
        bot.send_message(call.message.chat.id, 'Введите название аппарата')
        bot.register_next_step_handler(call.message, devices_in_cabinets)
    elif call.data == 'trailer_car_for_devices':
        TCFU[call.message.chat.id] = TrailerCarDEvices
        bot.send_message(call.message.chat.id, 'Введите название аппарата')
        bot.register_next_step_handler(call.message, devices_in_cabinets)
    elif call.data == 'motor_fuses':
        bot.send_message(
            call.message.chat.id,
            'Выберите шкаф',
            reply_markup=kb.markup_cab_in_motor()
            )
    elif call.data == 'head_fuses':
        bot.send_message(
            call.message.chat.id,
            'Выберите шкаф',
            reply_markup=kb.markup_cab_in_head()
            )
    elif call.data == 'trailer_fuses':
        bot.send_message(
            call.message.chat.id,
            'Выберите шкаф',
            reply_markup=kb.markup_cab_in_trailer()
            )
    elif call.data == 'head_cab_1':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(HeadCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №1")
        fuses_in_cabinets(call.message)
    elif call.data == 'head_cab_2':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(HeadCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №2")
        fuses_in_cabinets(call.message)
    elif call.data == 'head_cab_4':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(HeadCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №4")
        fuses_in_cabinets(call.message)
    elif call.data == 'head_cab_5':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(HeadCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №5")
        fuses_in_cabinets(call.message)
    elif call.data == 'head_cab_m':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(HeadCarDEvices)
        TCFU[call.message.chat.id].append("кабина, за машинистом")
        fuses_in_cabinets(call.message)
    elif call.data == 'motor_cab_1':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(MotorCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №1")
        fuses_in_cabinets(call.message)
    elif call.data == 'motor_cab_2':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(MotorCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №2")
        fuses_in_cabinets(call.message)
    elif call.data == 'motor_cab_4':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(MotorCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №4")
        fuses_in_cabinets(call.message)
    elif call.data == 'motor_cab_5':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(MotorCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №5")
        fuses_in_cabinets(call.message)
    elif call.data == 'trailer_cab_3':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(TrailerCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №3")
        fuses_in_cabinets(call.message)
    elif call.data == 'trailer_cab_4':
        TCFU[call.message.chat.id] = []
        TCFU[call.message.chat.id].append(TrailerCarDEvices)
        TCFU[call.message.chat.id].append("шкаф №4")
        fuses_in_cabinets(call.message)


def wires(message):
    wire_number = message.text
    session = Session(engine)
    stmt = select(Wires).where(Wires.name.in_([wire_number]))
    wire = session.scalar(stmt).description
    bot.send_message(message.chat.id, wire)


def devices_in_cabinets(message):
    user = TCFU[message.chat.id]
    devises = message.text.upper()
    session = Session(engine)
    stmt = select(
        user).where(user.name.in_([devises]))
    devises = session.scalar(stmt)
    bot.send_message(
        message.chat.id,
        f'Находится: {devises.location}\n{devises.description}')


def fuses_in_cabinets(message):
    tablet = TCFU[message.chat.id][0]
    cabinet = TCFU[message.chat.id][1]
    session = Session(engine)
    stmt = select(
        tablet).where(
            tablet.location.in_(
                [cabinet])).filter(
                    tablet.name.like('ПР-%'))
    for fuses in session.scalars(stmt):
        result = []
        result.append(f'{fuses.name}: {fuses.description.lower()}\n')
        bot.send_message(message.chat.id, result)


if __name__ == '__main__':
    print('Я запущен!')
    bot.infinity_polling()
