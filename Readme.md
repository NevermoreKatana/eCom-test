# web-app-eCom
Данный репозиторий создан для прохождения тестового задания от eCom 2023

# Установка зависимостей
````shell
make install
````

# Запуск контейнера MongoDB
````shell
make docker-mdb
````
# Запуск сервера
````shell
make start-server
````
# Запуск тестов
````shell
make test
````

# Дополнительно 

- http://127.0.0.1:8000/get_form - ссылка для работы с API
- Формат x-www-form-urlencoded
- Пример данных 
````json
{
    "user_name": "",
    "order_date": "",
    "phone_number": "",
    "user_name": ""
}
````