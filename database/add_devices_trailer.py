"""
Добавление данных в БД
"""
from models import TrailerCarDEvices, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    dev1 = TrailerCarDEvices(
        name='ПР-6',
        location='шкаф №3',
        description='Отопление.'
    )
    dev2 = TrailerCarDEvices(
        name='ПР-5',
        location='шкаф №3',
        description='СНВ.'
    )
    dev3 = TrailerCarDEvices(
        name='ПР-8',
        location='шкаф №3',
        description='Управление компрессором.'
    )
    dev4 = TrailerCarDEvices(
        name='ПР-42',
        location='шкаф №3',
        description='ДВ 1, 2.'
    )
    dev5 = TrailerCarDEvices(
        name='ПР-43',
        location='шкаф №',
        description='ДВ 1, 2.'
    )
    dev6 = TrailerCarDEvices(
        name='ПР-2',
        location='шкаф №',
        description='Освещение.'
    )
    dev7 = TrailerCarDEvices(
        name='ПР-1',
        location='шкаф №',
        description='Освещение.'
    )
    dev8 = TrailerCarDEvices(
        name='ПР-7',
        location='шкаф №3',
        description='Дежурное освещение.'
    )
    dev9 = TrailerCarDEvices(
        name='ПР-12',
        location='шкаф №3',
        description='Управление компрессором.'
    )
    dev10 = TrailerCarDEvices(
        name='ПР-13',
        location='шкаф №3',
        description='Обогрев маслоотделителя.'
    )
    dev11 = TrailerCarDEvices(
        name='ПР-41',
        location='шкаф №3',
        description='ДВК.'
    )
    dev12 = TrailerCarDEvices(
        name='ПР-40',
        location='шкаф №3',
        description='ДВК.'
    )
    dev13 = TrailerCarDEvices(
        name='ПР-11',
        location='шкаф №4',
        description='Отопление 620В.'
    )
    dev14 = TrailerCarDEvices(
        name='ПР15',
        location='шкаф №4',
        description='+АБ.'
    )
    dev15 = TrailerCarDEvices(
        name='ПР-14',
        location='шкаф №4',
        description='-АБ.'
    )
    dev16 = TrailerCarDEvices(
        name='ПР-33',
        location='шкаф №4',
        description='Питание защиты.'
    )
    dev17 = TrailerCarDEvices(
        name='ПР-45',
        location='шкаф №4',
        description='Нет данных.'
    )
    dev18 = TrailerCarDEvices(
        name='ПР-46',
        location='шкаф № 4',
        description='Нет данных.'
    )

    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10, dev11, dev12, dev13, dev14, dev15, dev16, dev17,
    #                  dev18
    #                  ])
    # session.commit()

from sqlalchemy import select, update

session = Session(engine)

staitment = update(TrailerCarDEvices).where(
    TrailerCarDEvices.name.in_(['Пр-46'])).values(
        name='ПР-46', location='шкаф №4')
session.execute(staitment)
session.commit()
stmt = select(TrailerCarDEvices).where(TrailerCarDEvices.name.in_(['ПР-46']))
for device in session.scalars(staitment):
    print(device)
