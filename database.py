# This is a sample Python script.
from sqlalchemy.orm import sessionmaker
from models import sync_engine
from models import ClientsOrm  # Импортируем модель из файла models.py

# Создаем фабрику сеансов
session_factory = sessionmaker(bind=sync_engine)

# Создаем объект сеанса
session = session_factory()
