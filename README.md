Мой проект представляет собой магазин книг на микросервисах, упакованных в Docker Compose.

* Для начала рассмотрим саму архитектуру:

| Сервис          | Порт | Описание                                | Документация                     | Пример данных |
|-----------------|------|-----------------------------------------|-----------------------------------|---------------|
| `api_gateway`   | 8000 | Единая точка входа (прокси на другие сервисы) | `http://localhost:8000/docs`      | зависит от сервиса |
| `user_service`  | 8001 | CRUD пользователей                      | `http://localhost:8001/docs`      | `{ "name": "string", "email": "user@example.com" }` |
| `book_service`  | 8002 | CRUD книг + управление остатками        | `http://localhost:8002/docs`      | `{ "title": "string", "author": "string", "price": 0, "stock": 0 }` |
| `order_service` | 8003 | Оформление заказов                      | `http://localhost:8003/docs`      | `{ "user_id": 0, "book_id": 0, "quantity": 0 }` |
| `postgres`      | 5432 | PostgreSQL (одна БД "microservices", разные схемы) | --- | --- |

* Как работать с проектом:

 - Клонируем репозиторий и переходим в директорию microservices_project

 - Запускаем проект: для этого пишем в терминале 'docker compose up --build'

 - Открываем браузер и переходим в нужный нам сервис(ссылки написаны выше в таблице выше). Можно поработать как с отедльным сервисом (порты 8001, 8002, 8003), так и со всеми вместе через единую точку входа (порт 8000). 

* Для регистрации нового пользователя/сохранения книги(пополнение на складе)/регистрации заказа:

  - отдельно через каждый сервис

    - В POST нажимаем Try it out и заполняем тело запроса, после чего жмем Execute.

  - через единую точку входа

    - В POST нажимаем Try it out

    - service = path = название выбранного сервиса(users/books/orders)

    - Заполняем тело запроса в зависимости от сервиса(т.е прописываем данные для выбранного сервиса согласно таблице выше)

* Для проверки сохранения пользователя/книги/заказа:

  - отдельно через каждый сервис

    - в браузере: В GET нажимаем Try it out, а далее Execute

    - через терминал : srv=users/books/orders
docker run --rm --network microservices_project_default \
  -e PGPASSWORD=postgres \
  postgres:15 psql -h postgres -U postgres -d microservices \
  -c '\pset border 2' -c "SELECT * FROM $srv;"

  - через единую точку входа

    - в браузере: В GET нажимаем Try it out, service = path = название выбранного сервиса(users/books/orders), далее нажимаем Execute

    - через терминал: мы можем проверить не только сервисы по отдельности, как написано выше, но и все сразу:  docker run --rm --network microservices_project_default \
  -e PGPASSWORD=postgres \
  postgres:15 psql -h postgres -U postgres -d microservices \
  -c '\pset border 2' \
  -c 'SELECT * FROM users;' \
  -c 'SELECT * FROM books;' \
  -c 'SELECT * FROM orders;'

* Для завершения прописываем в командной строке docker compose down