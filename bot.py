"""
Модуль принамает запросы от пользователя,
осуществляется взаимосвязь с БД и отправляет данные
обратно пользователю.
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import Wires, engine
from database.models import HeadCarDEvices, MotorCarDEvices, TrailerCarDEvices
from keyboard_mixin import KeyboardMixin as kb
from logger import logger
import os

import telebot
from dotenv import load_dotenv


class Bot():

    def __init__(self):
        load_dotenv()
        self.bot = self.do_auth()
        # Словарь для хранения временных данных от пользователя
        self.TCFU = {}

    @logger.catch
    def do_auth(self) -> None:
        """
        Авторизация сообщества. Использует переменную,
        хранящуюся в файле настроек окружения .env,
        в виде строки ACCESS_TOKEN=""
        """
        token = os.getenv("ACCESS_TOKEN")
        try:
            self.bot = telebot.TeleBot(token)
            return self.bot
        except Exception as error:
            print(error)

    def start(self):
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
                reply_markup=kb.main_markup()
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
                    reply_markup=kb.markup_type_car()
                    )
            elif message.text == 'Все предохранители в шкафу':
                self.bot.send_message(
                    message.chat.id,
                    'Выберите тип вагона',
                    reply_markup=kb.markup_fuses()
                    )

        @logger.catch
        @self.bot.callback_query_handler(func=lambda _: True)
        def all_query_handle(call) -> None:
            """
            Принимает данные со всех инлайн кнопок,
            осуществляет связь со следующими функциями и клавиатурами.
            """
            if call.data == 'motor_car_for_devices':
                self.get_calldata_type_car(call.message,
                                           MotorCarDEvices)
            elif call.data == 'head_car_for_devices':
                self.get_calldata_type_car(call.message,
                                           HeadCarDEvices)
            elif call.data == 'trailer_car_for_devices':
                self.get_calldata_type_car(call.message,
                                           TrailerCarDEvices)
            elif call.data == 'motor_fuses':
                self.bot.send_message(call.message.chat.id,
                                      'Выберите шкаф',
                                      reply_markup=kb.markup_cab_in_motor()
                                      )
            elif call.data == 'head_fuses':
                self.bot.send_message(
                    call.message.chat.id,
                    'Выберите шкаф',
                    reply_markup=kb.markup_cab_in_head()
                    )
            elif call.data == 'trailer_fuses':
                self.bot.send_message(
                    call.message.chat.id,
                    'Выберите шкаф',
                    reply_markup=kb.markup_cab_in_trailer()
                    )
            elif call.data == 'head_cab_1':
                self.get_calldata_fuses(call.message,
                                        HeadCarDEvices,
                                        'шкаф №1')
            elif call.data == 'head_cab_2':
                self.get_calldata_fuses(call.message,
                                        HeadCarDEvices,
                                        'шкаф №2')
            elif call.data == 'head_cab_4':
                self.get_calldata_fuses(call.message,
                                        HeadCarDEvices,
                                        'шкаф №4')
            elif call.data == 'head_cab_5':
                self.get_calldata_fuses(call.message,
                                        HeadCarDEvices,
                                        'шкаф №5')
            elif call.data == 'head_cab_m':
                self.get_calldata_fuses(call.message,
                                        HeadCarDEvices,
                                        'кабина, за машинистом')
            elif call.data == 'motor_cab_1':
                self.get_calldata_fuses(call.message,
                                        MotorCarDEvices,
                                        'шкаф №1 (ДВК)')
            elif call.data == 'motor_cab_2':
                self.get_calldata_fuses(call.message,
                                        MotorCarDEvices,
                                        'шкаф №2 (РУМ)')
            elif call.data == 'motor_cab_4':
                self.get_calldata_fuses(call.message,
                                        MotorCarDEvices,
                                        'шкаф №4 (АВ)')
            elif call.data == 'motor_cab_5':
                self.get_calldata_fuses(call.message,
                                        MotorCarDEvices,
                                        'шкаф №5')
            elif call.data == 'trailer_cab_3':
                self.get_calldata_fuses(call.message,
                                        TrailerCarDEvices,
                                        'шкаф №3')
            elif call.data == 'trailer_cab_4':
                self.get_calldata_fuses(call.message,
                                        TrailerCarDEvices,
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
        stmt = select(Wires).where(Wires.name.in_([wire_number]))
        try:
            wire = session.scalar(stmt).description
            self.bot.send_message(message.chat.id, wire)
        except Exception:
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
        # from bot import TCFU
        user = self.TCFU[message.chat.id]
        deviсes = message.text.upper()
        session = Session(engine)
        stmt = select(
            user).where(user.name.in_([deviсes]))
        try:
            deviсes = session.scalar(stmt)
            self.bot.send_message(
                message.chat.id,
                f'Находится: {deviсes.location}\n{deviсes.description}')
        except Exception:
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
        # from bot import TCFU
        tablet = self.TCFU[message.chat.id][0]
        cabinet = self.TCFU[message.chat.id][1]
        session = Session(engine)
        stmt = select(
            tablet).where(
                tablet.location.in_(
                    [cabinet])).filter(
                        tablet.name.like('ПР-%'))
        self.bot.send_message(message.chat.id, '----------------------------')
        for fuses in session.scalars(stmt):
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
        self.TCFU[message.chat.id] = []
        self.TCFU[message.chat.id].append(car)
        self.TCFU[message.chat.id].append(cabinet)
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
        self.TCFU[message.chat.id] = car
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
            except Exception:
                pass
