from sqlalchemy import select
from models import sync_engine, Base, ClientsOrm
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
                {"fullname": "Cesaro Kalinovich", "adress": "9 Buena Vista Street", "phone": "969-458-6404"},
                {"fullname": "Cherin Reedick", "adress": "37 Homewood Drive", "phone": "866-443-8396"},
                {"fullname": "Raul Alderwick", "adress": "21837 Sauthoff Hill", "phone": "770-164-1827"},
                {"fullname": "Lauritz Brophy", "adress": "7365 Darwin Point", "phone": "865-915-7598"}
            ]

            clients_objects = [ClientsOrm(**client) for client in clients_data]
            session.add_all(clients_objects)
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

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
