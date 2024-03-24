# This is a sample Python script.
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from config import connection_string

engine = create_engine(
    connection_string,
    echo=True
    # pool_size=5,
    # max_overflow=10
)
with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res=}")


# declarative base class
class Base(DeclarativeBase):
    pass


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class ClientsOrm(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str]
    adress: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str]


class EmployeeOrm(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str]
    firstname: Mapped[str]
    middlename: Mapped[str]
    jobtitle: Mapped[str]
    address: Mapped[str]
    homephone: Mapped[int]
    dateofbirth: Mapped[datetime]
    adress: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str]


Base.metadata.create_all(engine)
