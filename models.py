# declarative base class
from datetime import datetime
from sqlalchemy import String, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from config import connection_string

sync_engine = create_engine(url=connection_string, echo=True)


class Base(DeclarativeBase):
    pass


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


class GoodsOrm(Base):
    __tablename__ = "goods"

    id: Mapped[int] = mapped_column(primary_key=True)
    supplyid: Mapped[str]
    productname: Mapped[str]
    technicalspecifications: Mapped[str]
    description: Mapped[str]
    image: Mapped[str] = mapped_column(String(100))
    purchasecost: Mapped[int]
    availability: Mapped[datetime]
    quantity: Mapped[int]
    sellingprice: Mapped[float]


class OrdersOrm(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(primary_key=True)
    employeeid: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    productid: Mapped[int] = mapped_column(ForeignKey("goods.id"))
    placementdate: Mapped[datetime]
    executiondate: Mapped[datetime]
    clientid: Mapped[int] = mapped_column(ForeignKey("clients.id"))


class SupplierOrm(Base):
    __tablename__ = "supplier"
    supplierid: Mapped[int] = mapped_column(primary_key=True)
    suppliername: Mapped[str]
    supplierrepresentative: Mapped[str]
    contactphonenumber: Mapped[str]
    address: Mapped[str]


class SupplyOrm(Base):
    __tablename__ = "supply"
    supplyid: Mapped[int] = mapped_column(primary_key=True)
    supplierid: Mapped[str] = mapped_column(ForeignKey("supplier.supplierid"))
    supplydate: Mapped[datetime]


# После определения всех моделей вызовите create_all
Base.metadata.create_all(sync_engine)
