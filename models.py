# declarative base class
from datetime import datetime
from sqlalchemy import String, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
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
    homephone: Mapped[str]
    dateofbirth: Mapped[datetime] = mapped_column(String(10))

class GoodsOrm(Base):
    __tablename__ = "goods"

    id: Mapped[int] = mapped_column(primary_key=True)
    supplyid: Mapped[str]
    productname: Mapped[str]
    technicalspecifications: Mapped[str]
    description: Mapped[str]
    image: Mapped[str] = mapped_column(String(100))
    purchasecost: Mapped[int]
    availability: Mapped[str]
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
    # Отношение "один ко многим" между Supplier и Supply
    # supplies = relationship('SupplyOrm', back_populates="supplier", cascade="all, delete-orphan")

class SupplyOrm(Base):
    __tablename__ = "supply"
    supplyid: Mapped[int] = mapped_column(primary_key=True)
    supplierid: Mapped[int] = mapped_column(ForeignKey("supplier.supplierid", ondelete="CASCADE"))
    supplydate: Mapped[datetime]
    # supplier = relationship("SupplierOrm", back_populates="supplies", foreign_keys=[supplierid])

# После определения всех моделей вызовите create_all
Base.metadata.create_all(sync_engine)
