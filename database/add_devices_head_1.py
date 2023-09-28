"""
Добавление данных в БД
"""
from models import HeadCarDEvices, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    dev1 = HeadCarDEvices(
        name='БК',
        location='шкаф №1',
        description='Батарейный контактор.'
    )
    dev2 = HeadCarDEvices(
        name='РТВ',
        location='шкаф №1',
        description='Реле сигнализации отопления.'
    )
    dev3 = HeadCarDEvices(
        name='РН-2',
        location='шкаф №1',
        description='Реле переключения питания АЛСН.'
    )
    dev4 = HeadCarDEvices(
        name='ТРП',
        location='шкаф №1',
        description='Трансформатор раздельного питания АЛСН.'
    )
    dev5 = HeadCarDEvices(
        name='ДЛС',
        location='шкаф №1',
        description='Дроссель питания АЛСН.'
    )
    dev6 = HeadCarDEvices(
        name='ЛС-5',
        location='шкаф №1',
        description='Светодиод включения V1В.'
    )
    dev7 = HeadCarDEvices(
        name='ЛС-4',
        location='шкаф №1',
        description='Светодиод контроля изоляции - 30 провод.'
    )
    dev8 = HeadCarDEvices(
        name='ЛС-3',
        location='шкаф №1',
        description='Светодиод контроля изоляции - 15 провод.'
    )
    dev9 = HeadCarDEvices(
        name='ЛС-2',
        location='шкаф №1',
        description='Светодиод выпременителя 50в.'
    )
    dev10 = HeadCarDEvices(
        name='КТ',
        location='шкаф №1',
        description='Питание RSB.'
    )
    dev11 = HeadCarDEvices(
        name='РКД',
        location='шкаф №1',
        description='Реле охранной сигнализации кабины.'
    )
    dev12 = HeadCarDEvices(
        name='ПР-4',
        location='шкаф №1',
        description='Звонок.'
    )
    dev13 = HeadCarDEvices(
        name='ПР-7',
        location='шкаф №1',
        description='Дежурное освещение.'
    )
    dev14 = HeadCarDEvices(
        name='ПР-20',
        location='шкаф №1',
        description='Буферные фонари.'
    )
    dev15 = HeadCarDEvices(
        name='ПР-34',
        location='шкаф №1',
        description='15 провод.'
    )
    dev16 = HeadCarDEvices(
        name='ПР-9',
        location='шкаф №1',
        description='ЭПТ.'
    )
    dev17 = HeadCarDEvices(
        name='ПР-31',
        location='шкаф №1',
        description='Питание ЭПТ, АЛСН 50В.'
    )
    dev18 = HeadCarDEvices(
        name='ПР-39',
        location='шкаф №1',
        description='Питание ЭПТ, АЛСН 50В.'
    )
    dev19 = HeadCarDEvices(
        name='ПР-33',
        location='шкаф №1',
        description='Питание защиты.'
    )
    dev20 = HeadCarDEvices(
        name='ПР-14',
        location='шкаф №1',
        description='Заряд АБ "ГВ"(+-)'
    )
    dev21 = HeadCarDEvices(
        name='ПР-15',
        location='шкаф №1',
        description='Заряд АБ "ГВ"(+-)'
    )
    dev22 = HeadCarDEvices(
        name='ПР-36',
        location='шкаф №1',
        description='Заряд АБ "ПВ".'
    )
    dev23 = HeadCarDEvices(
        name='ПР-38',
        location='шкаф №1',
        description='Обогрев бака туалета.'
    )
    dev24 = HeadCarDEvices(
        name='ПР-56',
        location='шкаф №1',
        description='Обогрев бака от внешенего источника.'
    )
    dev25 = HeadCarDEvices(
        name='ПР-48',
        location='шкаф №1',
        description='Радиооповещение.'
    )
    dev26 = HeadCarDEvices(
        name='Пр-49',
        location='шкаф №1',
        description='Дополнительное обогрев кабины.'
    )
    dev27 = HeadCarDEvices(
        name='ПР-47',
        location='шкаф №1',
        description='Питание АЛСН 220В.'
    )
    dev28 = HeadCarDEvices(
        name='ПР-55',
        location='шкаф №1',
        description='Стеклообогрев.'
    )
    dev29 = HeadCarDEvices(
        name='ПР-45',
        location='шкаф №1',
        description='Питание ТТ1.'
    )
    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10, dev11, dev12, dev13, dev14, dev15, dev16,
    #                  dev17,dev18, dev19, dev20, dev21, dev22, dev23, dev24,
    #                  dev25, dev26, dev27, dev28, dev29
    #                  ])
    # session.commit()

#Здесь и везде далее вспомогательный блок для проверки добавленных данных.
from sqlalchemy import select

session = Session(engine)

stmt = select(HeadCarDEvices).where(HeadCarDEvices.name.in_(["ПР-55"]))

res = session.scalar(stmt).description
print(res)

for device in session.scalars(stmt):
    print(device.description)
