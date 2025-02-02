SchoolJournal API

Описание:
SchoolJournal API — это RESTful API для управления школьным журналом. Проект использует SQLAlchemy для работы с базой данных и обеспечивает удобный способ взаимодействия с данными учеников, учителей и оценок.

Требования:

Python 3.11
SQLAlchemy
PostgreSQL
Flask

Установка:

1.Клонируйте репозиторий:

git clone https://github.com/velialogiatour/SchoolJournal_API.git

cd SchoolJournal_API

2.Создайте виртуальное окружение и установите зависимости:

python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows

3.Настройте конфигурационный файл config.py, указав URL вашей базы данных:

DATABASE_URL = "postgresql://user:password@localhost:5432/SchoolDB"

Запуск

1.Примените миграции базы данных (если используются Alembic или Flask-Migrate):

flask db upgrade

2.Запустите приложение:

python app.py

API будет доступен по адресу http://127.0.0.1:5000/

Основные возможности API

1.Ученики: добавление, редактирование, удаление и просмотр информации об учениках

2.Учителя: управление данными учителей

3.Оценки: выставление и редактирование оценок

4.Классы: организация учеников по классам
