"""
Модуль принамает запросы от пользователя.
"""
from database.models import HeadCarDEvices, MotorCarDEvices, TrailerCarDEvices
from keyboard_mixin import KeyboardMixin as kb
from logger import logger
from main import bot
from server import Worker as w

# Словарь для хранения временной информации от пользователя.
TCFU = {}


@logger.catch
@bot.message_handler(commands=['start', 'help'])
def start(message) -> None:
    """
    Функция принимает от пользователя каманды: start и help,
    Выводит подсказку по использованию бота.
    Отправляет стартовую клаввиатуру.
    """
    bot.send_message(
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
@bot.message_handler()
def get_data_from_basic_keyboard(message) -> None:
    """
    Принимает данные из стртовой клавиатуры.
    Осуществляет связь со следующими функциями и клавиатурами.
    """
    if message.text == 'Провода':
        bot.send_message(message.chat.id, 'Введите номер провода')
        bot.register_next_step_handler(message, w.wires)
    elif message.text == 'Аппараты в шкафах':
        bot.send_message(
            message.chat.id,
            'Выберите тип вагона',
            reply_markup=kb.markup_type_car()
            )
    elif message.text == 'Все предохранители в шкафу':
        bot.send_message(
            message.chat.id,
            'Выберите тип вагона',
            reply_markup=kb.markup_fuses()
            )


@logger.catch
@bot.callback_query_handler(func=lambda _: True)
def all_query(call) -> None:
    """
    Принимает данные со всех инлайн кнопок,
    осуществляет связь со следующими функциями и клавиатурами.
    """
    if call.data == 'motor_car_for_devices':
        get_calldata_type_car(call.message, MotorCarDEvices)
    elif call.data == 'head_car_for_devices':
        get_calldata_type_car(call.message, HeadCarDEvices)
    elif call.data == 'trailer_car_for_devices':
        get_calldata_type_car(call.message, TrailerCarDEvices)
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
        get_calldata_fuses(call.message, HeadCarDEvices, 'шкаф №1')
    elif call.data == 'head_cab_2':
        get_calldata_fuses(call.message, HeadCarDEvices, 'шкаф №2')
    elif call.data == 'head_cab_4':
        get_calldata_fuses(call.message, HeadCarDEvices, 'шкаф №4')
    elif call.data == 'head_cab_5':
        get_calldata_fuses(call.message, HeadCarDEvices, 'шкаф №5')
    elif call.data == 'head_cab_m':
        get_calldata_fuses(
            call.message, HeadCarDEvices, 'кабина, за машинистом')
    elif call.data == 'motor_cab_1':
        get_calldata_fuses(call.message, MotorCarDEvices, 'шкаф №1 (ДВК)')
    elif call.data == 'motor_cab_2':
        get_calldata_fuses(call.message, MotorCarDEvices, 'шкаф №2 (РУМ)')
    elif call.data == 'motor_cab_4':
        get_calldata_fuses(call.message, MotorCarDEvices, 'шкаф №4 (АВ)')
    elif call.data == 'motor_cab_5':
        get_calldata_fuses(call.message, MotorCarDEvices, 'шкаф №5')
    elif call.data == 'trailer_cab_3':
        get_calldata_fuses(call.message, TrailerCarDEvices, 'шкаф №3')
    elif call.data == 'trailer_cab_4':
        get_calldata_fuses(call.message, TrailerCarDEvices, 'шкаф №4')


@logger.catch
def get_calldata_fuses(
    message,
    car: HeadCarDEvices | MotorCarDEvices | TrailerCarDEvices,
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
    TCFU[message.chat.id] = []
    TCFU[message.chat.id].append(car)
    TCFU[message.chat.id].append(cabinet)
    w.fuses_in_cabinets(message)


@logger.catch
def get_calldata_type_car(message, car: str) -> None:
    """
    Вспомогательная функция.

    Заносит данные от пользователя в словарь, что бы использовать их
    в функции devices_in_cabinets().

    Args:
        message: данные от телеграмм
        car: class, характеризует тип вагона,
             используется для взаимодействия с БД.
    """
    TCFU[message.chat.id] = car
    bot.send_message(message.chat.id, 'Введите название аппарата')
    bot.register_next_step_handler(message, w.devices_in_cabinets)
