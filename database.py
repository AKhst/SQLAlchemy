# This is a sample Python script.
from sqlalchemy.orm import sessionmaker
from models import engine
from models import ClientsOrm  # Импортируем модель из файла models.py

# Создаем фабрику сеансов
Session = sessionmaker(bind=engine)

# Создаем объект сеанса
session = Session()

# Создаем объект клиента
clients = ClientsOrm(fullname="Odelinda Grzelewski", adress="7 Everett Park", phone="363-492-2952")

# Добавляем объект в сеанс
session.add(clients)

# Фиксируем изменения в базе данных
session.commit()
