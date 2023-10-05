"""
В этом модуле собраны все клавиатуры используемые в боте.
"""
from telebot import types

from logger import logger


class KeyboardMixin:
    """
    Класc хранит клавиатуры.
    """
    @logger.catch
    def main_markup(self):
        """
        Стартовая клавиатура.
        """
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Все предохранители в шкафу')
        btn2 = types.KeyboardButton('Аппараты в шкафах')
        btn3 = types.KeyboardButton('Провода')
        markup.row(btn1)
        markup.row(btn2, btn3)
        return markup

    @logger.catch
    def markup_type_car(self):
        """
        Выбор типа вагона.
        Используется для функции вывода конкретного аппарата в шкафу.
        """
        markup_type_car = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Головной', callback_data='devices_head_car')
        btn2 = types.InlineKeyboardButton(
            'Моторный', callback_data='devices_motor_car')
        btn3 = types.InlineKeyboardButton(
            'Прицепной', callback_data='devices_trailer_car')
        markup_type_car.add(btn1, btn2, btn3)
        return markup_type_car

    @logger.catch
    def markup_fuses(self):
        """
        Выбор типа вагона.
        Используется для функции вывода всех предохранителей в шкафу.
        """
        fuses = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Головной', callback_data='fuses_head')
        btn2 = types.InlineKeyboardButton(
            'Моторный', callback_data='fuses_motor')
        btn3 = types.InlineKeyboardButton(
            'Прицепной', callback_data='fuses_trailer')
        fuses.add(btn1, btn2, btn3)
        return fuses

    @logger.catch
    def markup_cab_in_head(self):
        """
        Определение номера шкафа для головного вагона.
        """
        fuses = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'шкаф №1', callback_data='head_cab_1')
        btn2 = types.InlineKeyboardButton(
            'шкаф №2', callback_data='head_cab_2')
        btn4 = types.InlineKeyboardButton(
            'шкаф №4', callback_data='head_cab_4')
        btn5 = types.InlineKeyboardButton(
            'шкаф №5', callback_data='head_cab_5')
        btnm = types.InlineKeyboardButton(
            'кабина, за машинистом', callback_data='head_cab_m')
        fuses.add(btn1, btn2)
        fuses.add(btn4, btn5)
        fuses.add(btnm)
        return fuses

    @logger.catch
    def markup_cab_in_motor(self):
        """
        Определение номера шкафа для моторного вагона.
        """
        fuses = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'шкаф №1 (ДВК)', callback_data='motor_cab_1')
        btn2 = types.InlineKeyboardButton(
            'шкаф №2 (РУМ)', callback_data='motor_cab_2')
        btn4 = types.InlineKeyboardButton(
            'шкаф №4 (АВ)', callback_data='motor_cab_4')
        btn5 = types.InlineKeyboardButton(
            'шкаф №5', callback_data='motor_cab_5')
        fuses.row(btn1, btn2)
        fuses.row(btn4, btn5)
        return fuses

    @logger.catch
    def markup_cab_in_trailer(self):
        """
        Определение номера шкафа для прицепного вагона.
        """
        fuses = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'шкаф №3', callback_data='trailer_cab_3')
        btn2 = types.InlineKeyboardButton(
            'шкаф №4', callback_data='trailer_cab_4')
        fuses.add(btn1, btn2)
        return fuses
