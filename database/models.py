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
        return f'Wires(id={self.id!r}, name={self.name!r}, description={self.description!r})'


class HeadCarDEvices(Base):
    """
    Табличка 'Головной вагон'
    """
    __tablename__ = 'head_car_devices'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return f'HeadCarDEvices(id={self.id!r}, name={self.name!r}, location={self.location!r}, description={self.description!r})'


class MotorCarDEvices(Base):
    """
    Табличка 'Моторный вагон'
    """
    __tablename__ = 'motor_car_devices'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return f'MotorCarDEvices(id={self.id!r}, name={self.name!r}, location={self.location}, description={self.description!r})'


class TrailerCarDEvices(Base):
    """
    Табличка 'Прицепной вагон'
    """
    __tablename__ = 'trailer_car_devices'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return f'TrailerCarDEvices(id={self.id!r}, name={self.name!r}, location={self.location}, description={self.description!r})'


# Создание метаданных по заданному шаблону.
engine = create_engine('sqlite:///wires_devices.db', echo=True)
Base.metadata.create_all(engine)
