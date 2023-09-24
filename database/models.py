from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Wires(Base):
    __tablename__ = 'wires'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return f'Wires(id={self.id!r}, name={self.name!r}, description={self.description!r})'


class HeadCarDEvices(Base):
    __tablename__ = 'head_car_devices'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return f'HeadCarDEvices(id={self.id!r}, name={self.name!r}, location={self.location!r}, description={self.description!r})'


class MotorCarDEvices(Base):
    __tablename__ = 'motor_car_devices'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return f'MotorCarDEvices(id={self.id!r}, name={self.name!r}, location={self.location}, description={self.description!r})'


class TrailerCarDEvices(Base):
    __tablename__ = 'trailer_car_devices'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]

    def __repr__(self) -> str:
        return f'TrailerCarDEvices(id={self.id!r}, name={self.name!r}, location={self.location}, description={self.description!r})'


engine = create_engine('sqlite:///wires_devices.db', echo=True)
Base.metadata.create_all(engine)
