from sqlalchemy import select, func
from models import sync_engine, Base, ClientsOrm, EmployeeOrm, OrdersOrm, GoodsOrm, SupplierOrm, SupplyOrm
from database import session_factory


class SyncORM:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_clients():
        with session_factory() as session:
            clients_data = [
                {"fullname": "Nerissa Warby", "adress": "8789 Doe Crossing Road", "phone": "514-837-7917"},
                {"fullname": "Bernadette Butt", "adress": "3 Merrick Circle", "phone": "655-715-5320"},
                {"fullname": "Bryna O'Currigan", "adress": "726 Northview Center", "phone": "678-990-7445"},
                {"fullname": "Ephrem Berr", "adress": "96 Grayhawk Place", "phone": "255-531-2102"},
                {"fullname": "Cesaro Kalinovich", "adress": "9 Buena Vista Street", "phone": "969-458-6404"}
            ]

            clients_objects = [ClientsOrm(**client) for client in clients_data]
            session.add_all(clients_objects)
            # flush отправляет запрос в базу данных
            # После flush каждый из клиентов получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def insert_employee():
        with session_factory() as session:
            employee_data = [
                {"lastname": "Estevan", "firstname": "Bob", "middlename": "Nikolaevich",
                 "jobtitle": "Financial Analyst", "address": "97 Banding Road", "homephone": "800-830-6207",
                 "dateofbirth": "1972-06-28"},
                {"lastname": "Nickolai", "firstname": "Bob", "middlename": "Nikolaevich",
                 "jobtitle": "Graphic Designer", "address": "48 8th Pass", "homephone": "483-756-0349",
                 "dateofbirth": "1998-12-12"},
                {"lastname": "Garrott", "firstname": "Jasmine", "middlename": "Stepanovich",
                 "jobtitle": "Software Engineer", "address": "3229 Shoshone Trail", "homephone": "627-224-7346",
                 "dateofbirth": "1982-01-25"},
                {"lastname": "Barbabra", "firstname": "Hannah", "middlename": "Alexandrovich",
                 "jobtitle": "HR Coordinator", "address": "75735 Springview Court", "homephone": "684-158-0207",
                 "dateofbirth": "1990-05-15"},
                {"lastname": "Geraldine", "firstname": "Charlie", "middlename": "Vladimirovich",
                 "jobtitle": "Financial Analyst", "address": "401 Troy Park", "homephone": "516-530-1350",
                 "dateofbirth": "1990-05-15"}
            ]

            employee_objects = [EmployeeOrm(**employee) for employee in employee_data]
            session.add_all(employee_objects)
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def insert_goods():
        with session_factory() as session:
            goods_data = [
                {"supplyid": "S67890", "productname": "T-shirt", "technicalspecifications": "striped T-shirt",
                 "description": "Striped T-shirt with advanced design",
                 "image": "http://dummyimage.com/236x100.png/5fa2dd/ffffff", "purchasecost": 12.99,
                 "availability": "In stock", "quantity": 35, "sellingprice": 19.99},
                {"supplyid": "S54321", "productname": "Sunglasses", "technicalspecifications": "aviator sunglasses",
                 "description": "Aviator sunglasses with UV protection",
                 "image": "http://dummyimage.com/160x100.png/5fa2dd/ffffff", "purchasecost": 8.50,
                 "availability": "Out of stock", "quantity": 45, "sellingprice": 12.50},
                {"supplyid": "S11111", "productname": "Notebook", "technicalspecifications": "leather notebook",
                 "description": "Genuine leather notebook with embossed cover",
                 "image": "http://dummyimage.com/209x100.png/cc0000/ffffff", "purchasecost": 5.75,
                 "availability": "In stock", "quantity": 50, "sellingprice": 8.75},
                {"supplyid": "S24680", "productname": "Phone case", "technicalspecifications": "marble phone case",
                 "description": "Marble phone case with sleek finish",
                 "image": "http://dummyimage.com/193x100.png/5fa2dd/ffffff", "purchasecost": 15.25,
                 "availability": "In stock", "quantity": 45, "sellingprice": 15.25},
                {"supplyid": "S13579", "productname": "Water bottle",
                 "technicalspecifications": "insulated water bottle",
                 "description": "Insulated water bottle with double-wall construction",
                 "image": "http://dummyimage.com/213x100.png/5fa2dd/ffffff", "purchasecost": 3.99,
                 "availability": "In stock", "quantity": 50, "sellingprice": 5.99}
            ]

            goods_objects = [GoodsOrm(**goods) for goods in goods_data]
            session.add_all(goods_objects)
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def insert_orders():
        with session_factory() as session:
            orders_data = [
                {"employeeid": 5, "productid": 4, "placementdate": "2023-11-11", "executiondate": "2023-10-15",
                 "clientid": 1},
                {"employeeid": 4, "productid": 3, "placementdate": "2023-09-30", "executiondate": "2023-06-21",
                 "clientid": 2},
                {"employeeid": 3, "productid": 1, "placementdate": "2023-12-11", "executiondate": "2023-08-31",
                 "clientid": 3},
                {"employeeid": 2, "productid": 5, "placementdate": "2023-09-19", "executiondate": "2023-06-14",
                 "clientid": 4},
                {"employeeid": 1, "productid": 2, "placementdate": "2023-10-13", "executiondate": "2023-05-12",
                 "clientid": 5}
            ]

            orders_objects = [OrdersOrm(**orders) for orders in orders_data]
            session.add_all(orders_objects)
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def insert_supplier():
        with session_factory() as session:
            supplier_data = [
                {"suppliername": "Emerald City Imports", "supplierrepresentative": "Emily Johnson",
                 "contactphonenumber": "294-430-2508", "address": "3 Vidon Hill"},
                {"suppliername": "Silver Star Trading Co.", "supplierrepresentative": "Jessica Lee",
                 "contactphonenumber": "920-682-1986", "address": "582 Hansons Hill"},
                {"suppliername": "Emerald City Imports", "supplierrepresentative": "Kevin Brown",
                 "contactphonenumber": "151-209-2956", "address": "1 Dixon Center"},
                {"suppliername": "ABC Suppliers", "supplierrepresentative": "Laura Garcia",
                 "contactphonenumber": "127-155-6409", "address": "732 Lakeland Drive"},
                {"suppliername": "ABC Suppliers", "supplierrepresentative": "Jessica Lee",
                 "contactphonenumber": "824-304-8524", "address": "77 Graedel Park"}
            ]

            supplier_objects = [SupplierOrm(**supplier) for supplier in supplier_data]
            session.add_all(supplier_objects)
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()
    @staticmethod
    def insert_supply():
        with session_factory() as session:
            supply_data = [
                {"supplierid": 3, "supplydate": "2023-06-20"},
                {"supplierid": 5, "supplydate": "2023-06-13"},
                {"supplierid": 4, "supplydate": "2023-06-02"},
                {"supplierid": 2, "supplydate": "2023-10-12"},
                {"supplierid": 1, "supplydate": "2024-02-24"}
            ]
            supply_object = [SupplyOrm(**sypply) for sypply in supply_data]
            session.add_all(supply_object)
            session.flush()
            session.commit()

    @staticmethod
    def inner_join_query():
        with session_factory() as session:
            # Выполняем inner join между таблицами orders, clients и products
            result = (
                session.query(OrdersOrm, ClientsOrm)
                .join(ClientsOrm, OrdersOrm.clientid == ClientsOrm.id)
                .all()
            )

            # Выводим результат на экран
            for order, client in result:
                print(f"Order ID: {order.order_id}, Client: {client.fullname}")

    @staticmethod
    def complex_query():
        with session_factory() as session:
            # Выполняем inner join между таблицами orders и clients
            query = (
                session.query(
                    OrdersOrm.clientid,
                    ClientsOrm.fullname,
                    func.sum(GoodsOrm.quantity).label("total_quantity")
                )
                .join(ClientsOrm, OrdersOrm.clientid == ClientsOrm.id)
                .join(GoodsOrm, OrdersOrm.productid == GoodsOrm.id)
                .filter(OrdersOrm.placementdate >= '2023-01-01')  # Пример WHERE условия
                .group_by(OrdersOrm.clientid, ClientsOrm.fullname)  # Пример GROUP BY
                .order_by(func.sum(GoodsOrm.quantity).desc())  # Пример ORDER BY
                .distinct()  # Пример DISTINCT
            )

            # Получаем итерируемый результат
            results = query.all()

            # Выводим результат на экран
            for result in results:
                print(f"Client: {result.fullname}, Client ID:{result.clientid},Total Quantity: {result.total_quantity}")


    @staticmethod
    def select_clients():
        with session_factory() as session:
            query = select(ClientsOrm)
            result = session.execute(query)
            clients = result.all()
            print(f"{clients=}")

    @staticmethod
    def update_clients(id: int = 2, new_fullname: str = "Ainslie Boother"):
        with session_factory() as session:
            worker_lexi = session.get(ClientsOrm, id)
            worker_lexi.fullname = new_fullname
            # refresh нужен, если мы хотим заново подгрузить данные модели из базы.
            # Подходит, если мы давно получили модель и в это время
            # данные в базе данныхмогли быть изменены
            session.commit()

    @staticmethod
    def print_clients():
        with session_factory() as session:
            clients = session.query(ClientsOrm).all()
            for client in clients:
                print(f"ID: {client.id}, Full Name: {client.fullname}, Address: {client.adress}, Phone: {client.phone}")