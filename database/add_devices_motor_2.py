from sqlalchemy.orm import Session
from models import engine

from models import MotorCarDEvices

with Session(engine) as session:
    dev1 = MotorCarDEvices(
        name='РНВ',
        location='шкаф №2 (РУМ)',
        description='Реле напряжения вентиляции.'
    )
    dev2 = MotorCarDEvices(
        name='РНТ',
        location='шкаф №2 (РУМ)',
        description='Реле насоса трансформатора.\nВходит в цепь ЛК.'
    )
    dev3 = MotorCarDEvices(
        name='РВЗ',
        location='шкаф №2 (РУМ)',
        description='Реле востановления защиты.\nВходит в цепь ВВ.'
    )
    dev4 = MotorCarDEvices(
        name='РТВ',
        location='шкаф №2 (РУМ)',
        description='Реле тепла и вентиляции.'
    )
    dev5 = MotorCarDEvices(
        name='РБС',
        location='шкаф №2 (РУМ)',
        description='Реле блинкера схемы.'
    )
    dev6 = MotorCarDEvices(
        name='РБМ',
        location='шкаф №2 (РУМ)',
        description='Реле блинкера масла.'
    )
    dev7 = MotorCarDEvices(
        name='БСМЭ',
        location='шкаф №2 (РУМ)',
        description='Блок сигнализации срабатывания блинкеров.\n'
                    'Vh-1, Vh-2 - светодиоды блинкеров масла и схемы.\n'
                    ' Sb-1, Sb-2 - кнопки востановления блинкеров.'
    )
    dev8 = MotorCarDEvices(
        name='ПТРС',
        location='шкаф №2 (РУМ)',
        description='Промежуточное реле температуры салона.\n'
                    'Входит в цепь 26 провода.'
    )
    dev9 = MotorCarDEvices(
        name='РПЗ',
        location='шкаф №2 (РУМ)',
        description='Промежуточное реле защиты ТЭД.\nВходит в цепь ЛК.\n'
                    'Притянуто если в норме АВУ, РНТ, РБМ.'
    )
    dev10 = MotorCarDEvices(
        name='ПВВ-1',
        location='шкаф №2 (РУМ)',
        description='Промежуточное реле ВВ'
    )
    dev11 = MotorCarDEvices(
        name='ПВВ-2',
        location='шкаф №2 (РУМ)',
        description='Промежуточное реле.\nЗащищает ВВ от звонковой работы.'
    )
    dev12 = MotorCarDEvices(
        name='РПВВ-1',
        location='шкаф №2 (РУМ)',
        description='Промежуточное реле для для ППВ-1.'
    )
    dev13 = MotorCarDEvices(
        name='РОП',
        location='шкаф №2 (РУМ)',
        description='Реле опуска пантогрофа'
    )
    dev14 = MotorCarDEvices(
        name='ПР-22',
        location='шкаф №2 (РУМ)',
        description='Обогрев ВВ.'
    )
    dev15 = MotorCarDEvices(
        name='ТР-7',
        location='шкаф №2 (РУМ)',
        description='Тепловое реле насоса трансформатора.'
    )
    dev16 = MotorCarDEvices(
        name='ТР-8',
        location='шкаф №2 (РУМ)',
        description='Тепловое реле насоса трансформатора.'
    )
    dev17 = MotorCarDEvices(
        name='КНТ',
        location='шкаф №2 (РУМ)',
        description='Контактор насоса трансформатора.\nВходит в цепь ЛК.'
    )
    dev18 = MotorCarDEvices(
        name='КВК',
        location='шкаф №2 (РУМ)',
        description='Контактор вспомогательного компрессора.'
    )
    dev19 = MotorCarDEvices(
        name='РББ',
        location='шкаф №2 (РУМ)',
        description='Реле блокировок безопасности.\nВходит в цепь 26 провода.'
    )
    dev20 = MotorCarDEvices(
        name='ПР-8',
        location='шкаф №2 (РУМ)',
        description='Вспомогательный компрессор(15А).'
    )
    dev21 = MotorCarDEvices(
        name='ПР-5',
        location='шкаф №2 (РУМ)',
        description='Питание РРУ(6А).'
    )
    dev22 = MotorCarDEvices(
        name='ПР-9',
        location='шкаф №2 (РУМ)',
        description='Дежурное освещение(6А).'
    )
    dev23 = MotorCarDEvices(
        name='ПР-7',
        location='шкаф №2 (РУМ)',
        description='Сигнализация(6А).'
    )
    dev24 = MotorCarDEvices(
        name='ПР-3',
        location='шкаф №2 (РУМ)',
        description='Питание РОП, ПВВ-1, ППВ-2, ВВ, РПЗ(6А).'
    )
    dev25 = MotorCarDEvices(
        name='ПР-13',
        location='шкаф №2 (РУМ)',
        description='Двигатели вентиляции салона.'
    )
    dev26 = MotorCarDEvices(
        name='ПР-14',
        location='шкаф №2 (РУМ)',
        description='Двигатели вентиляции салона'
    )
    dev27 = MotorCarDEvices(
        name='ПР-11',
        location='шкаф №2 (РУМ)',
        description='Двигательнасоса трансформатора.'
    )
    dev28 = MotorCarDEvices(
        name='ПР-12',
        location='шкаф №2 (РУМ)',
        description='Двигатель насоса трансформатора.'
    )
    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10, dev11, dev12, dev13, dev14, dev15, dev16, dev17,
    #                  dev18, dev19, dev20, dev21, dev22, dev23, dev24, dev25,
    #                  dev26, dev27, dev28
    #                 ])
    # session.commit()
from sqlalchemy import select

session = Session(engine)

stmt = select(MotorCarDEvices).where(MotorCarDEvices.name.in_(["ПР-11"]))

for device in session.scalars(stmt):
    print(device.description)
