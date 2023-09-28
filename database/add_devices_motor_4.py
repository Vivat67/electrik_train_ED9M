from models import MotorCarDEvices, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    dev1 = MotorCarDEvices(
        name='ПРТ',
        location='шкаф №5',
        description='Промежуточное реле торможения.'
                    '\nПри отказе реостатного тормоза.'
    )
    dev2 = MotorCarDEvices(
        name='РЭТ',
        location='шкаф №5',
        description='Промежуточное реле.'
                    '\nСрабатывает при замещении РТ в момент остановки.'
    )
    dev3 = MotorCarDEvices(
        name='РКТ-1',
        location='шкаф №5',
        description='Реле контроля тока ТЭД.'
    )
    dev4 = MotorCarDEvices(
        name='РКТ-2',
        location='шкаф №5',
        description='Реле контроля тока ТЭД.'
    )
    dev5 = MotorCarDEvices(
        name='ПРЗ',
        location='шкаф №5',
        description='Промежуточное реле защиты.\nВходит в цепь ЛК.'
                    '\nСрабатывает при разностном боксовании и при превышении тока якоря ТЭД в режиме РТ.'
    )
    dev6 = MotorCarDEvices(
        name='РВ',
        location='шкаф №5',
        description='Промежуточное реле в цепи БРТ.'
    )
    dev7 = MotorCarDEvices(
        name='ПРБ',
        location='шкаф №5',
        description='Промежуточное реле боксования.\nСтоит в цепи БРУ, БРТ.'
                    '\n Останавливает ГК и ТК при срабатывании РБ.'
    )
    dev8 = MotorCarDEvices(
        name='РВТ-1',
        location='шкаф №5',
        description='Реле времени торможения.'
    )
    dev9 = MotorCarDEvices(
        name='РВТ-2',
        location='шкаф №5',
        description='Реле времени торможения.'
    )
    dev10 = MotorCarDEvices(
        name='РВТ-3',
        location='шкаф №5',
        description='Реле времени торможения.'
    )
    dev11 = MotorCarDEvices(
        name='ПР-25',
        location='шкаф №5',
        description='Блок РТ.'
    )
    # session.add_all([dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9,
    #                  dev10, dev11
    #                 ])
    # session.commit()


from sqlalchemy import select

session = Session(engine)

stmt = select(MotorCarDEvices).where(MotorCarDEvices.name.in_(["РВТ-2"]))

adt = session.scalar(stmt).description
print(adt)
