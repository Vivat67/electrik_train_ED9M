from sqlalchemy.orm import Session
from models import engine

from models import MotorCarDEvices

with Session(engine) as session:
    klp_o = MotorCarDEvices(
        name='КЛП-О',
        location='шкаф №1 (ДВК)',
        description='клапан опускания пантогрофа.'
    )
    klp_p = MotorCarDEvices(
        name='КЛП-П',
        location='шкаф №1 (ДВК)',
        description='клапан поднятия пантогрофа.'
    )
    ptv_2 = MotorCarDEvices(
        name='ПТВ-2',
        location='шкаф №1 (ДВК)',
        description='Промежуточное реле температуры салона.'
                    '\nОтключает печи в цепи КО-1.'
    )
    ptv_1 = MotorCarDEvices(
        name='ПТВ-1',
        location='шкаф №1 (ДВК)',
        description='Премежуточное реле термоавтоматики.'
                    '\nОтключает ТЭНы калорифера в цепи КО-2.'
    )
    os = MotorCarDEvices(
        name='ОС',
        location='шкаф №1 (ДВК)',
        description='Контактор освещения салона.'
    )
    kv_1 = MotorCarDEvices(
        name='КВ-1',
        location='шкаф №1 (ДВК)',
        description='Контактор включения вентиляции калорифера.'
    )
    tr_3 = MotorCarDEvices(
        name='ТР-3',
        location='шкаф №1 (ДВК)',
        description='Тепловое реле двигателя вентилятора ДВ-1.'
    )
    tr_4 = MotorCarDEvices(
        name='ТР-4',
        location='шкаф №1 (ДВК)',
        description='Тепловое реле двигателя вентилятора ДВ-1.'
    )
    tr_5 = MotorCarDEvices(
        name='ТР-5',
        location='шкаф №1 (ДВК)',
        description='Тепловое реле двигателя вентилятора ДВ-2.'
    )
    tr_6 = MotorCarDEvices(
        name='ТР-6',
        location='шкаф №1 (ДВК)',
        description='Тепловое реле двигателя вентилятора ДВ-2.'
    )
    avu = MotorCarDEvices(
        name='АВУ',
        location='шкаф №1 (ДВК)',
        description='Автоматический выключатель управления.\nВходит в цепь ЛК.'
    )
    avt = MotorCarDEvices(
        name='АВТ',
        location='шкаф №1 (ДВК)',
        description='Автоматический выключатель реостатного торможения.'
                    '\nВходит в цепь ЛК в режиме реостатного торможения.'
    )
    pr_16 = MotorCarDEvices(
        name='ПР-16',
        location='шкаф №1 (ДВК)',
        description='Предохранитель освещения вагона.(6А)'
    )
    pr_17 = MotorCarDEvices(
        name='ПР-17',
        location='шкаф №1 (ДВК)',
        description='Предохранитель освещения вагона.(6А)'
    )
    pr_6 = MotorCarDEvices(
        name='ПР-6',
        location='шкаф №1 (ДВК)',
        description='Предохранитель отопления.(6А)'
    )
    # session.add_all([klp_o, klp_p, ptv_2, ptv_1, os, kv_1, tr_3, tr_4, tr_5,
    #                  tr_6, avu, avt, pr_16, pr_17, pr_6
    #                 ])
    # session.commit()


from sqlalchemy import select

session = Session(engine)

stmt = select(MotorCarDEvices).where(MotorCarDEvices.name.in_(["ПР-17"]))

adt = session.scalar(stmt).description
print(adt)
