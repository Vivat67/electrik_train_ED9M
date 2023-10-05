"""
Модуль принамает запросы от пользователя,
осуществляется взаимосвязь с БД и отправляет данные
обратно пользователю.
"""
import os

import telebot
from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.orm import Session
from telebot import apihelper

from database.models import (HeadCarDevices, MotorCarDevices,
                             TrailerCarDevices, Wires, engine)
from keyboard_mixin import KeyboardMixin
from logger import logger


class Bot:
    """
    Основное взаимодействие с ботом.
    """

    def __init__(self):
        load_dotenv()
        self.bot = self.do_auth()
        # Словарь для хранения временных данных от пользователя
        self.temp_data = {}
        # kb- keyboard
        self.kb = KeyboardMixin()

    @logger.catch
    def do_auth(self) -> None | telebot.TeleBot:
        """
        Авторизация сообщества. Использует переменную,
        хранящуюся в файле настроек окружения .env,
        в виде строки ACCESS_TOKEN=""
        """
        token = os.getenv("ACCESS_TOKEN")
        try:
            self.bot = telebot.TeleBot(token)
            return self.bot
        except apihelper.ApiTelegramException as e:
            print(f"Произошла ошибка авторизации: {e}")

    def start(self):
        """
        Осуществляет запуск кода, для взаимодействия с telegram API,
        внутри обьекта bot.
        """
        @logger.catch
        @self.bot.message_handler(commands=['start', 'help'])
        def handle_start(message) -> None:
            """
            Функция принимает от пользователя каманды: start и help,
            Выводит подсказку по использованию бота.
            Отправляет стартовую клаввиатуру.
            """
            self.bot.send_message(
                message.chat.id,
                'Вам доступны следующие кнопки:\n'
                '1. Все предохранители в шкафу:\n'
                '  1. выбираете тип вагона;\n'
                '  2. выбираете нужный шкаф;\n'
                '  3. получаете описание всех предохранителей в этом шкафу.\n'
                '2. Аппараты в шкафах:\n'
                '  1. выбираете тип вагона;\n'
                '  2. введите название апарата,\n'
                '     название можно вводить в любом регистре, через тире,\n'
                '     пример: ПР-10, ПТВ-2, КЛП-О;\n'
                '  3. получаете описание аппарата и его место раположения.\n'
                '2. Провода:\n'
                '  1. введите номер провода;\n'
                '  2. получаете описание данного провода.\n',
                reply_markup=self.kb.main_markup()
                )

        @logger.catch
        @self.bot.message_handler()
        def get_data_from_bk_handle(message) -> None:
            """
            Принимает данные из стартовой клавиатуры.
            Осуществляет связь со следующими функциями и клавиатурами.
            """
            if message.text == 'Провода':
                self.bot.send_message(message.chat.id, 'Введите номер провода')
                self.bot.register_next_step_handler(message, self.wires)
            elif message.text == 'Аппараты в шкафах':
                self.bot.send_message(
                    message.chat.id,
                    'Выберите тип вагона',
                    reply_markup=self.kb.markup_type_car()
                    )
            elif message.text == 'Все предохранители в шкафу':
                self.bot.send_message(
                    message.chat.id,
                    'Выберите тип вагона',
                    reply_markup=self.kb.markup_fuses()
                    )

        @logger.catch
        @self.bot.callback_query_handler(
            func=lambda call: call.data.startswith('devices'))
        def dev_type_car_query_handle(call) -> None:
            """
            Принимает данные от инлайн кнопок,
            отвечающих за выбор типа вагона,
            при поиске аппарата в шкафу.
            """
            if call.data == 'devices_motor_car':
                self.get_calldata_type_car(call.message,
                                           MotorCarDevices)
            elif call.data == 'devices_head_car':
                self.get_calldata_type_car(call.message,
                                           HeadCarDevices)
            elif call.data == 'devices_trailer_car':
                self.get_calldata_type_car(call.message,
                                           TrailerCarDevices)

        @logger.catch
        @self.bot.callback_query_handler(
            func=lambda call: call.data.startswith('fuses'))
        def fuses_type_car_query_handle(call) -> None:
            """
            Принимает данные от инлайн кнопок,
            отвечающих за выбор типа вагона,
            при поиске всех предохранителей в шкафу.
            """
            if call.data == 'fuses_motor':
                self.bot.send_message(call.message.chat.id,
                                      'Выберите шкаф',
                                      reply_markup=self.kb.markup_cab_in_motor()
                                      )
            elif call.data == 'fuses_head':
                self.bot.send_message(
                    call.message.chat.id,
                    'Выберите шкаф',
                    reply_markup=self.kb.markup_cab_in_head()
                    )
            elif call.data == 'fuses_trailer':
                self.bot.send_message(
                    call.message.chat.id,
                    'Выберите шкаф',
                    reply_markup=self.kb.markup_cab_in_trailer()
                    )

        @logger.catch
        @self.bot.callback_query_handler(
            func=lambda call: call.data.startswith('head'))
        def fuses_head_query_handle(call) -> None:
            """
            Принимает данные от инлайн кнопок,
            отвечающих за выбор шкафа в головном вагоне,
            для вывода всех предохранителей в шкафу.
            """
            if call.data == 'head_cab_1':
                self.get_calldata_fuses(call.message,
                                        HeadCarDevices,
                                        'шкаф №1')
            elif call.data == 'head_cab_2':
                self.get_calldata_fuses(call.message,
                                        HeadCarDevices,
                                        'шкаф №2')
            elif call.data == 'head_cab_4':
                self.get_calldata_fuses(call.message,
                                        HeadCarDevices,
                                        'шкаф №4')
            elif call.data == 'head_cab_5':
                self.get_calldata_fuses(call.message,
                                        HeadCarDevices,
                                        'шкаф №5')
            elif call.data == 'head_cab_m':
                self.get_calldata_fuses(call.message,
                                        HeadCarDevices,
                                        'кабина, за машинистом')

        @logger.catch
        @self.bot.callback_query_handler(
            func=lambda call: call.data.startswith('motor'))
        def fuses_motor_query_handle(call) -> None:
            """
            Принимает данные от инлайн кнопок,
            отвечающих за выбор шкафа в моторном вагоне,
            для вывода всех предохранителей в шкафу.
            """
            if call.data == 'motor_cab_1':
                self.get_calldata_fuses(call.message,
                                        MotorCarDevices,
                                        'шкаф №1 (ДВК)')
            elif call.data == 'motor_cab_2':
                self.get_calldata_fuses(call.message,
                                        MotorCarDevices,
                                        'шкаф №2 (РУМ)')
            elif call.data == 'motor_cab_4':
                self.get_calldata_fuses(call.message,
                                        MotorCarDevices,
                                        'шкаф №4 (АВ)')
            elif call.data == 'motor_cab_5':
                self.get_calldata_fuses(call.message,
                                        MotorCarDevices,
                                        'шкаф №5')

        @logger.catch
        @self.bot.callback_query_handler(
            func=lambda call: call.data.startswith('trailer'))
        def fuses_trailer_query_handle(call) -> None:
            """
            Принимает данные от инлайн кнопок,
            отвечающих за выбор шкафа в прицепном вагоне,
            для вывода всех предохранителей в шкафу.
            """
            if call.data == 'trailer_cab_3':
                self.get_calldata_fuses(call.message,
                                        TrailerCarDevices,
                                        'шкаф №3')
            elif call.data == 'trailer_cab_4':
                self.get_calldata_fuses(call.message,
                                        TrailerCarDevices,
                                        'шкаф №4')

    @logger.catch
    def wires(self, message) -> None:
        """
        Обрабатывает запрос от пользователя,
        связывается с БД (табличка 'Провода'),
        отпровляет данные с БД (описание провода).
        """
        wire_number = message.text
        session = Session(engine)
        staitment = select(Wires).where(Wires.name.in_([wire_number]))
        try:
            wire = session.scalar(staitment).description
            self.bot.send_message(message.chat.id, wire)
        except AttributeError:
            self.bot.send_message(message.chat.id,
                                  'Такого провода нет.\n'
                                  'В базе есть провода с 1-71.')

    @logger.catch
    def devices_in_cabinets(self, message) -> None:
        """
        Обрабатывает запрос от пользователя,
        связывается с БД (таблички данного типа вагона),
        отпровляет данные с БД (описание конкретного аппарата).
        """
        user = self.temp_data[message.chat.id]
        deviсes = message.text.upper()
        session = Session(engine)
        staitment = select(
            user).where(user.name.in_([deviсes]))
        try:
            deviсes = session.scalar(staitment)
            self.bot.send_message(
                message.chat.id,
                f'Находится: {deviсes.location}\n{deviсes.description}')
        except AttributeError:
            self.bot.send_message(
                message.chat.id,
                'Такого аппарата в данном вагоне нет.\n'
                'Или проверьте правильность написания.\n'
                'Пишите название через тире.\n'
                'Пример: Тр-7, ПР-10, КЛП-О, АВУ')

    @logger.catch
    def fuses_in_cabinets(self, message) -> None:
        """
        Обрабатывает запрос от пользователя,
        связывается с БД (табличка данного типа вагона),
        отпровляет данные с БД (все предохранители в шкафу).
        """
        tablet = self.temp_data[message.chat.id][0]
        cabinet = self.temp_data[message.chat.id][1]
        session = Session(engine)
        staitment = select(
            tablet).where(
                tablet.location.in_(
                    [cabinet])).filter(
                        tablet.name.like('ПР-%'))
        self.bot.send_message(message.chat.id, '----------------------------')
        for fuses in session.scalars(staitment):
            result = []
            result.append(f'{fuses.name}: {fuses.description.lower()}\n')
            self.bot.send_message(message.chat.id, result)

    @logger.catch
    def get_calldata_fuses(
            self,
            message,
            car,
            cabinet: str
    ) -> None:
        """
        Вспомогательная функция.

        Заносит данные от пользователя в словарь, что бы использовать их
        в функции fuses_in_cabinets().

        Args:
            message: данные от телеграмм
            car: class, характеризует тип вагона,
                используется для взаимодействия с БД.
            cabinet: обозначает поле location в БД.
        """
        self.temp_data[message.chat.id] = []
        self.temp_data[message.chat.id].append(car)
        self.temp_data[message.chat.id].append(cabinet)
        self.fuses_in_cabinets(message)

    @logger.catch
    def get_calldata_type_car(self, message, car: str) -> None:
        """
        Вспомогательная функция.

        Заносит данные от пользователя в словарь, что бы использовать их
        в функции devices_in_cabinets().

        Args:
            message: данные от телеграмм
            car: class, характеризует тип вагона,
                используется для взаимодействия с БД.
        """
        self.temp_data[message.chat.id] = car
        self.bot.send_message(message.chat.id, 'Введите название аппарата')
        self.bot.register_next_step_handler(message, self.devices_in_cabinets)

    @logger.catch
    def run(self):
        """
        Запуск бота.
        """
        while True:
            try:
                self.bot.infinity_polling()
            except:
                pass
