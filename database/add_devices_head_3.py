from models import HeadCarDEvices, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    dev1 = HeadCarDEvices(
        name='РВК',
        location='шкаф №4',
        description='Реле времени включения кондиционера.'
    )
    dev2 = HeadCarDEvices(
        name='ПТВ-1',
        location='шкаф №4',
        description='Отопление вагона.'
    )
    dev3 = HeadCarDEvices(
        name='ПТРС',
        location='шкаф №4',
        description='Пожарная сигнализация.'
    )
    dev4 = HeadCarDEvices(
        name='РК',
        location='шкаф №4',
        description='Нет данных.'
    )
    dev5 = HeadCarDEvices(
        name='ПРТ',
        location='шкаф №4',
        description='Нет данных.'
    )
    dev6 = HeadCarDEvices(
        name='КМК',
        location='шкаф №4',
        description='Контактор мотор-компрессора.'
    )
    dev7 = HeadCarDEvices(
        name='ПНФ',
        location='шкаф №4',
        description='Контакторзапуска АРФ.'
    )
    dev8 = HeadCarDEvices(
        name='ПРК',
        location='шкаф №4',
        description='Промежуточное реле компркессора.'
    )
    dev9 = HeadCarDEvices(
        name='ПТВ-2',
        location='шкаф №4',
        description='Отопление вагона'
    )
    dev10 = HeadCarDEvices(
        name='ОС',
        location='шкаф №4',
        description='Контактор освещения.'
    )
    dev11 = HeadCarDEvices(
        name='ТР-7',
        location='шкаф №4',
        description='ДВК.'
    )
    dev12 = HeadCarDEvices(
        name='ТР-8',
        location='шкаф №4',
        description='ДВК.'
    )
    dev13 = HeadCarDEvices(
        name='ТР-3',
        location='шкаф №4',
        description='ДВ1.'
    )
    dev14 = HeadCarDEvices(
        name='ТР-4',
        location='шкаф №4',
        description='ДВ1.'
    )
    dev15 = HeadCarDEvices(
        name='ТР-5',
        location='шкаф №4',
        description='ДВ2.'
    )
    dev16 = HeadCarDEvices(
        name='ТР-6',
        location='шкаф №4',
        description='ДВ2.'
    )
    dev17 = HeadCarDEvices(
        name='ПР-6',
        location='шкаф №4',
        description='Отопление салона.'
    )
    dev18 = HeadCarDEvices(
        name='ПР-5',
        location='шкаф №4',
        description='Сигнализация неисправности вагона.'
    )
    dev19 = HeadCarDEvices(
        name='ПР-42',
        location='шкаф №4',
        description='ДВ1, 2.'
    )
    dev20 = HeadCarDEvices(
        name='ПР-43',
        location='шкаф №4',
        description='ДВ1, 2'
    )
    dev21 = HeadCarDEvices(
        name='ПР-2',
        location='шкаф №4',
        description='Освещение салона.'
    )
    dev22 = HeadCarDEvices(
        name='ПР-1',
        location='шкаф №4',
        description='Освещение салона.'
    )
    dev23 = HeadCarDEvices(
        name='ПР-12',
        location='шкаф №4',
        description='Включение ГК.'
    )
    dev24 = HeadCarDEvices(
        name='ПР-13',
        location='шкаф №4',
        description='Обогрев масло-отделителя.'
    )
    dev25 = HeadCarDEvices(
        name='ПР-41',
        location='шкаф №4',
        description='Двигатель мотор-компрессора.'
    )
    dev26 = HeadCarDEvices(
        name='ПР-40',
        location='шкаф №4',
        description='Двигатель мотор-компрессора.'
    )

    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10, dev11, dev12, dev13, dev14, dev15, dev16, dev17,
    #                  dev18, dev19, dev20,dev21, dev22, dev23, dev24, dev25,
    #                  dev26
    #                  ])
    # session.commit()
from sqlalchemy import select

session = Session(engine)

stmt = select(HeadCarDEvices).where(HeadCarDEvices.name.in_(["ПР-40"]))

for device in session.scalars(stmt):
    print(device.description)
