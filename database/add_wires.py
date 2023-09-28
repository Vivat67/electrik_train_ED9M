from models import Wires, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    wire1 = Wires(
        name='1',
        description='Автоматический пуск ГК до 19 позиции'
    )
    wire2 = Wires(
        name='2',
        description='Реостатное торможение'
    )
    wire3 = Wires(
        name='3',
        description='Мановровый режим'
    )
    wire4 = Wires(
        name='4',
        description='Пониженная уставка торможения'
    )
    wire5 = Wires(
        name='5',
        description='Нет данных'
    )
    wire6 = Wires(
        name='6',
        description='Блинкеры'
    )
    wire7 = Wires(
        name='7',
        description='Восстонавление ВВ и защиты'
    )
    wire8 = Wires(
        name='8',
        description='Пониженная уставка торможения'
    )
    wire9 = Wires(
        name='9',
        description='Нет данных'
    )
    wire10 = Wires(
        name='10',
        description='Торможение прицепного вагона'
    )
    wire11 = Wires(
        name='11',
        description='Реверсор "Вперед"'
    )
    wire12 = Wires(
        name='12',
        description='Реверсор "Назад"'
    )
    wire13 = Wires(
        name='13',
        description='Вспомогательный компрессор'
    )
    wire14 = Wires(
        name='14',
        description='Нет данных'
    )
    wire15 = Wires(
        name='15',
        description='Цепи управления'
    )
    wire16 = Wires(
        name='16',
        description='Нет данных'
    )
    wire17 = Wires(
        name='17',
        description='Нет данных'
    )
    wire18 = Wires(
        name='18',
        description='Контроль дверей'
    )
    wire19 = Wires(
        name='19',
        description='Отключение ВВ'
    )
    wire20 = Wires(
        name='20',
        description='Включение БК'
    )
    wire21 = Wires(
        name='21',
        description='Нет данных'
    )
    wire22 = Wires(
        name='22',
        description='Питание защиты'
    )
    wire23 = Wires(
        name='23',
        description='Трансляция'
    )
    wire24 = Wires(
        name='24',
        description='Трансляция'
    )
    wire25 = Wires(
        name='25',
        description='Подьем токоприемника'
    )
    wire26 = Wires(
        name='26',
        description='Опускание токоприемника'
    )
    wire27 = Wires(
        name='27',
        description='Компрессор'
    )
    wire28 = Wires(
        name='28',
        description='АРФ'
    )
    wire29 = Wires(
        name='29',
        description='Блокировка ВБ'
    )
    wire30 = Wires(
        name='30',
        description='Цепи управления'
    )
    wire31 = Wires(
        name='31',
        description='Сигнализация "ЛК"'
    )
    wire32 = Wires(
        name='32',
        description='Сигнализация "ВВ"'
    )
    wire33 = Wires(
        name='33',
        description='Сигнализация "Вспомогательные цепи"'
    )
    wire34 = Wires(
        name='34',
        description='Сигнализация "Напряжение цепи"'
    )
    wire35 = Wires(
        name='35',
        description='Сигнализация "Боксование"'
    )
    wire36 = Wires(
        name='36',
        description='Вентиляция'
    )
    wire37 = Wires(
        name='37',
        description='Освещение'
    )
    wire38 = Wires(
        name='38',
        description='Нет данных'
    )
    wire39 = Wires(
        name='39',
        description='Обогрев маслоотделителя'
    )
    wire40 = Wires(
        name='40',
        description='Нет данных'
    )
    wire41 = Wires(
        name='41',
        description='Нет данных'
    )
    wire42 = Wires(
        name='42',
        description='Дотормаживание ЭПТ'
    )
    wire43 = Wires(
        name='43',
        description='Минус ЭПТ'
    )
    wire44 = Wires(
        name='44',
        description='Замещение'
    )
    wire45 = Wires(
        name='45',
        description='Перекрыша'
    )
    wire46 = Wires(
        name='46',
        description='Сигнал СОТ-Х'
    )
    wire47 = Wires(
        name='47',
        description='Торможение'
    )
    wire48 = Wires(
        name='48',
        description='Уставка РУ'
    )
    wire49 = Wires(
        name='49',
        description='Вентиль отпуска'
    )
    wire50 = Wires(
        name='50',
        description='Звонок'
    )
    wire51 = Wires(
        name='51',
        description='СОТ'
    )
    wire52 = Wires(
        name='52',
        description='Открытие правых дверей'
    )
    wire53 = Wires(
        name='53',
        description='Закрытие правых дверей'
    )
    wire54 = Wires(
        name='54',
        description='Открытие левых дверей'
    )
    wire55 = Wires(
        name='55',
        description='Закрытие левых дверей'
    )
    wire56 = Wires(
        name='56',
        description='Плюс АБ'
    )
    wire57 = Wires(
        name='57',
        description='Связь'
    )
    wire58 = Wires(
        name='58',
        description='Связь'
    )
    wire59 = Wires(
        name='59',
        description='Песочницы'
    )
    wire60 = Wires(
        name='60',
        description='Песочницы'
    )
    wire61 = Wires(
        name='61',
        description='Переменный ток, фаза С3'
    )
    wire62 = Wires(
        name='62',
        description='Переменный ток, фаза С1'
    )
    wire63 = Wires(
        name='63',
        description='Переменный ток, фаза С2'
    )
    wire64 = Wires(
        name='64',
        description='Уставка РУ'
    )
    wire65 = Wires(
        name='65',
        description='Питание ППС'
    )
    wire66 = Wires(
        name='66',
        description='Информатика(ЭВМ)'
    )
    wire67 = Wires(
        name='67',
        description='Освещение'
    )
    wire68 = Wires(
        name='68',
        description='Освещение'
    )
    wire69 = Wires(
        name='69',
        description='Нет данных'
    )
    wire70 = Wires(
        name='70',
        description='Пониженная уставка торможения'
    )
    wire71 = Wires(
        name='71',
        description='Киловольтметр'
    )

    # session.add_all([wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8,
    #                  wire9, wire10, wire11, wire12, wire13, wire14, wire15,
    #                  wire16, wire17, wire18, wire19, wire20, wire21, wire22,
    #                  wire23, wire24, wire25, wire26, wire27, wire28, wire29,
    #                  wire30,wire31, wire32, wire33, wire34, wire35, wire36,
    #                  wire37, wire38, wire39, wire40,wire41, wire42, wire43,
    #                  wire44, wire45, wire46, wire47, wire48, wire49, wire50,
    #                  wire51, wire52, wire53, wire54, wire55, wire56, wire57,
    #                  wire58, wire59, wire60,wire61, wire62, wire63, wire64,
    #                  wire65, wire66, wire67, wire68, wire69, wire70,wire71
    #                 ])
    # session.commit()
from sqlalchemy import select

session = Session(engine)

stmt = select(Wires).where(Wires.name.in_(["61"]))

for device in session.scalars(stmt):
    print(device.description)
