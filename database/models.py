"""
В данном модуле создаются метаданные для БД.
"""
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import Session
from logger import logger


class Base(DeclarativeBase):
    pass


class Wires(Base):
    """
    Табличка 'Провода'
    """
    __tablename__ = 'wires'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return (
            f'Wires(id={self.id!r}, '
            f'name={self.name!r}, '
            f'description={self.description!r})'
        )


class CarDevices(Base):
    """
    Абстрактный класс.
    На его основе создаются классы для всех типов вагонов.
    """
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}(id={self.id!r}, '
            f'name={self.name!r}, '
            f'location={self.location}, '
            f'description={self.description!r})'
        )


class HeadCarDevices(CarDevices):
    """
    Табличка 'Головной вагон'
    """
    __tablename__ = 'head_car_devices'


class MotorCarDevices(CarDevices):
    """
    Табличка 'Моторный вагон'
    """
    __tablename__ = 'motor_car_devices'


class TrailerCarDevices(CarDevices):
    """
    Табличка 'Прицепной вагон'
    """
    __tablename__ = 'trailer_car_devices'


# Создание метаданных по заданному шаблону.
engine = create_engine('sqlite:///wires_devices.db', echo=True)
Base.metadata.create_all(engine)


class DataAccess:
    """
    Класс служит для извлечения данных из БД.
    """
    def __init__(self):
        self.session = Session(engine)

    @logger.catch
    def get_data_wires(self, wire_number: str) -> str | None:
        """
        Получаем данные о проводам из БД.

        Args:
            wire_number: наименование провода(его номер).

        Returns:
            wire: описание провода;
            None: такого провода нет в БД.
        """
        wires_data = select(Wires).where(Wires.name.in_([wire_number]))
        try:
            wire = self.session.scalar(wires_data).description
            return wire
        except AttributeError:
            print('Недопустимое значение')
            return None

    @logger.catch
    def get_data_devices(self, type_car, deviсe_name: str):
        """
        Получаем данные о аппаратах из БД.

        Args:
            type_car: тип вагона(для выбора таблички в БД);
            deviсe_name: наименование аппарата.

        Returns:
            [dev_des, dev_loc]: список, содержащий данные о аппарате
            (описание, место нахождения).
            [None, None]: такого аппарата нет в БД.
        """
        devices_data = select(
            type_car).where(type_car.name.in_([deviсe_name]))
        try:
            dev_des = self.session.scalar(devices_data).description
            dev_loc = self.session.scalar(devices_data).location
            return [dev_des, dev_loc]
        except AttributeError:
            print('Недопустимое значение')
            return [None, None]

    @logger.catch
    def get_data_fuses(self, type_car, cabinet):
        """
        Получаем данные о всех предохранителях в конкретном шкафу из БД.

        Args:
            type_car: тип вагона(для выбора таблички в БД);
            cabinet: наименование шкафа.

        Returns:
            fuses: данные о всех предохранителях в шкафу.
        """
        fuses_data = select(
            type_car).where(
            type_car.location.in_(
                [cabinet])).filter(
                    type_car.name.like('ПР-%'))
        fuses = ''
        for fuse in self.session.scalars(fuses_data):
            fuses = fuses + f'{fuse.name}: {fuse.description.lower()}\n'
        return fuses
