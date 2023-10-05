"""
В данном модуле создаются метаданные для БД.
"""
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


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
