from sqlalchemy.orm import Session
from models import engine

from models import HeadCarDEvices

with Session(engine) as session:
    dev1 = HeadCarDEvices(
        name='ТР',
        location='шкаф №2',
        description='Нет данных.'
    )
    dev2 = HeadCarDEvices(
        name='ДР',
        location='шкаф №2',
        description='Нет данных.'
    )
    dev3 = HeadCarDEvices(
        name='КСН',
        location='шкаф №2',
        description='Нет данных.'
    )
    dev4 = HeadCarDEvices(
        name='РНС',
        location='шкаф №2',
        description='Нет данных.'
    )
    dev5 = HeadCarDEvices(
        name='РО',
        location='шкаф №2',
        description='Реле отпуска ЭПТ.'
    )
    dev6 = HeadCarDEvices(
        name='РПТ',
        location='шкаф №2',
        description='Нет данных.'
    )
    dev7 = HeadCarDEvices(
        name='РТ',
        location='шкаф №2',
        description='Реле торможения ЭПТ.'
    )
    dev8 = HeadCarDEvices(
        name='РКБ',
        location='шкаф №2',
        description='Нет данных.'
    )
    dev9 = HeadCarDEvices(
        name='РКО',
        location='шкаф №2',
        description='Реле контроля отпуска ЭПТ.'
    )
    dev10 = HeadCarDEvices(
        name='РКТ',
        location='шкаф №2',
        description='Реле контроля торможения ЭПТ.'
    )
    dev11 = HeadCarDEvices(
        name='РЗ',
        location='шкаф №2',
        description='Оключение при "КЖ" локомотивного светофора.'
    )
    dev12 = HeadCarDEvices(
        name='РОСБ',
        location='шкаф №2',
        description='Обогрев боковых стекл.'
    )
    dev13 = HeadCarDEvices(
        name='КОСЛ',
        location='шкаф №2',
        description='Обогрев лобовых стекл.'
    )
    dev14 = HeadCarDEvices(
        name='ПР-51',
        location='шкаф №2',
        description='Кондиционер.'
    )
    dev15 = HeadCarDEvices(
        name='ПР-52',
        location='шкаф №2',
        description='Обогрев.'
    )
    dev16 = HeadCarDEvices(
        name='ПР-50',
        location='шкаф №2',
        description='Кондиционер.'
    )
    dev17 = HeadCarDEvices(
        name='Q-100',
        location='шкаф №2',
        description='Питание КВ-С.'
    )

    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10,dev11, dev12, dev13, dev14, dev15, dev16, dev17
    #                  ])
    # session.commit()
from sqlalchemy import select

session = Session(engine)

stmt = select(HeadCarDEvices).where(HeadCarDEvices.name.in_(["ПР-50"]))

for device in session.scalars(stmt):
    print(device.description)
