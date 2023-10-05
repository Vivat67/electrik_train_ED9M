"""
Добавление данных в БД
"""
from models import MotorCarDEvices, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    dev1 = MotorCarDEvices(
        name='UI',
        location='шкаф №4 (АВ)',
        description='Блок управления и защиты фазорасщепителя.'
    )
    dev2 = MotorCarDEvices(
        name='БТЗ',
        location='шкаф №4 (АВ)',
        description='Блок токовой защиты.\nУскоренное отключение ВВ.'
    )
    dev3 = MotorCarDEvices(
        name='КЗ',
        location='шкаф №4 (АВ)',
        description='Контактор защиты.\nВходит в цепь ЛК и ВВ.'
    )
    dev4 = MotorCarDEvices(
        name='ПСП',
        location='шкаф №4 (АВ)',
        description='Переключатель системы питания.'
                    '\nИспользуется при резервировании АРФ.'
    )
    dev5 = MotorCarDEvices(
        name='ПНФ',
        location='шкаф №4 (АВ)',
        description='Повторитель напряжения АРФ.'
    )
    dev6 = MotorCarDEvices(
        name='БУС',
        location='шкаф №4 (АВ)',
        description='Блок управления стабилизатором.'
    )
    dev7 = MotorCarDEvices(
        name='ПКР',
        location='шкаф №4 (АВ)',
        description='Промежуточный контактор АРФ.'
    )
    dev8 = MotorCarDEvices(
        name='ТР-9',
        location='шкаф №4 (АВ)',
        description='Тепловое реле АРФ.'
    )
    dev9 = MotorCarDEvices(
        name='ТР-10',
        location='шкаф №4 (АВ)',
        description='Тепловое реле АРФ.'
    )
    dev10 = MotorCarDEvices(
        name='КС',
        location='шкаф №4 (АВ)',
        description='Контактор стабилизатора.'
    )
    dev11 = MotorCarDEvices(
        name='АВ',
        location='шкаф №4 (АВ)',
        description='Главный автомат.'
    )
    dev12 = MotorCarDEvices(
        name='ПР-19',
        location='шкаф №4 (АВ)',
        description='Сетевой вольтметр кабины.'
    )
    dev13 = MotorCarDEvices(
        name='Пр-20',
        location='шкаф №4 (АВ)',
        description='Питание 220В блока UI. (2А)'
    )
    dev14 = MotorCarDEvices(
        name='ПР-23',
        location='шкаф №4 (АВ)',
        description='Питание блока БУС. (2А)'
    )
    dev15 = MotorCarDEvices(
        name='ПР-10',
        location='шкаф №4 (АВ)',
        description='Питание блока UI. (6А)'
    )
    dev16 = MotorCarDEvices(
        name='ПР-4',
        location='шкаф №4 (АВ)',
        description='Питание БТЗ. (15А)'
    )
    dev17 = MotorCarDEvices(
        name='ПР-15',
        location='шкаф №4 (АВ)',
        description='Освещение салона. (35А)'
    )
    dev18 = MotorCarDEvices(
        name='ПР-18',
        location='шкаф №4 (АВ)',
        description='Освещение салона. (35А)'
    )
    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10, dev11, dev12, dev13, dev14, dev15, dev16, dev17,
    #                  dev18
    #                 ])
    # session.commit()

from sqlalchemy import select

session = Session(engine)

staitment = select(MotorCarDEvices).where(MotorCarDEvices.name.in_(["ПР-18"]))

adt = session.scalar(staitment).description
print(adt)
