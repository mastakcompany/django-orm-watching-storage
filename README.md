# Пульт охраны банка

#### Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код верстки или посмотреть как реализованы запросы к БД.

#### Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников нашего банка.

## Как установить

1. Убедитесь, что у вас установлен Python 3.
2. Склонируйте данный репозиторий.
3. Установите зависимости:
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env в корневой папке проекта и укажите в нем следующие переменные окружения:

* `ENGINE` - движок базы данных, например, `django.db.backends.postgresql`.
* `HOST` - адрес сервера базы данных, например, `127.0.0.1`.
* `PORT` - порт сервера базы данных, например, `5432`.
* `NAME` - имя базы данных.
* `DJANGO_USER` - имя пользователя для подключения к базе данных.
* `PASSWORD` - пароль пользователя для подключения к базе данных.
* `SECRET_KEY` - секретный ключ для Django-приложения.
* `DEBUG` - режим отладки (`True` или `False`).

Пример содержимого файла `.env`:
```commandline
ENGINE=django.db.backends.postgresql
HOST=127.0.0.1
PORT=5432
NAME=my_database
DJANGO_USER=my_user
PASSWORD=my_password
SECRET_KEY=my_secret_key
DEBUG=True
```
5. Запустите командой `python main.py runserver`

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).