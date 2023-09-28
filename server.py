from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import Wires, engine
from logger import logger
from main import bot


class Worker:

    # TCFU = {}
    @logger.catch
    def wires(message):
        wire_number = message.text
        session = Session(engine)
        stmt = select(Wires).where(Wires.name.in_([wire_number]))
        wire = session.scalar(stmt).description
        bot.send_message(message.chat.id, wire)

    @logger.catch
    def devices_in_cabinets(message):
        from bot import TCFU
        user = TCFU[message.chat.id]
        devises = message.text.upper()
        session = Session(engine)
        stmt = select(
            user).where(user.name.in_([devises]))
        devises = session.scalar(stmt)
        bot.send_message(
            message.chat.id,
            f'Находится: {devises.location}\n{devises.description}')

    @logger.catch
    def fuses_in_cabinets(message):
        from bot import TCFU
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

    # def get_calldata_fuses(message, car, cabinet):
    #     Worker.TCFU[message.chat.id] = []
    #     Worker.TCFU[message.chat.id].append(car)
    #     Worker.TCFU[message.chat.id].append(cabinet)
    #     fuses_in_cabinets(message)

    # def get_calldata_type_car(message, car):
    #     from bot import TCFU
    #     TCFU[message.chat.id] = car
    #     bot.send_message(message.chat.id, 'Введите название аппарата')
    #     bot.register_next_step_handler(message, devices_in_cabinets)
