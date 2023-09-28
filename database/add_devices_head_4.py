"""
Добавление данных в БД
"""
from models import HeadCarDEvices, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    dev1 = HeadCarDEvices(
        name='КО-1',
        location='шкаф №5',
        description='Контактор отопления.'
    )
    dev2 = HeadCarDEvices(
        name='КО-2',
        location='шкаф №5',
        description='Контактор отопления.'
    )
    dev3 = HeadCarDEvices(
        name='КО-3',
        location='шкаф №5',
        description='Контактор отопления.'
    )
    dev4 = HeadCarDEvices(
        name='КО-4',
        location='шкаф №5',
        description='Контактор отопления.'
    )
    dev5 = HeadCarDEvices(
        name='РПО',
        location='шкаф №5',
        description='Реле перегрузки отопления.'
    )
    dev6 = HeadCarDEvices(
        name='РНВ1',
        location='шкаф №5',
        description='Реле напряжения.'
    )
    dev7 = HeadCarDEvices(
        name='ПР-10',
        location='шкаф №5',
        description='Нет данных.'
    )
    dev8 = HeadCarDEvices(
        name='ПР-11',
        location='шкаф №5',
        description='Нет данных.'
    )
    dev9 = HeadCarDEvices(
        name='ПР-3',
        location='кабина, за машинистом',
        description='Двери.'
    )
    dev10 = HeadCarDEvices(
        name='ПР-18',
        location='кабина, за машинистом',
        description='Дежурное освещение.'
    )
    dev11 = HeadCarDEvices(
        name='ПР-17',
        location='кабина, за машинистом',
        description='Прожектор.'
    )
    dev12 = HeadCarDEvices(
        name='ПР-19',
        location='кабина, за машинистом',
        description='Сигналы.'
    )
    dev13 = HeadCarDEvices(
        name='ПР-21',
        location='кабина, за машинистом',
        description='Освещение салонов.'
    )
    dev14 = HeadCarDEvices(
        name='ПР-25',
        location='кабина, за машинистом',
        description='Электропечи.'
    )
    dev15 = HeadCarDEvices(
        name='ПР-44',
        location='кабина, за машинистом',
        description='Песочницы.'
    )
    dev16 = HeadCarDEvices(
        name='ПР-23',
        location='кабина, за машинистом',
        description='Обогрев масло отделителя.'
    )
    dev17 = HeadCarDEvices(
        name='ПР-24',
        location='кабина, за машинистом',
        description='Вентиляция.'
    )
    dev18 = HeadCarDEvices(
        name='ПР-71',
        location='кабина, за машинистом',
        description='Радиостанция.'
    )
    dev19 = HeadCarDEvices(
        name='ПР-70',
        location='кабина, за машинистом',
        description='Нет данных.'
    )

    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10, dev11, dev12, dev13, dev14, dev15, dev16, dev17,
    #                  dev18, dev19
    #                  ])
    session.commit()
from sqlalchemy import select

session = Session(engine)

stmt = select(HeadCarDEvices).where(HeadCarDEvices.name.in_(["ПР-70"]))

for device in session.scalars(stmt):
    print(device.description)
