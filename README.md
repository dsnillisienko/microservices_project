$$\text{Летняя практика "Микросервисные взаимодействия"}$$

Мой проект представляет собой магазин книг на микросервисах, упакованных в Docker Compose.

Для начала рассмотрим саму архитектуру:

$$
\begin{array}{|l|c|l|c|c|}
  \hline
  \text{Сервис} & \text{Порт} & \text{Какую задачу решает} & \text{Ссылка} & \text{Данные} \\
  \hline
  \texttt{api\_gateway} & 8000 & \text{Единая точка входа (прокси на другие сервисы)} & \texttt{http://localhost:8000/docs} & \text{в зависимости от сервиса} \\
  \hline
  \texttt{user\_service} & 8001 & \text{CRUD пользователей} & \texttt{http://localhost:8001/docs} & \texttt{\{ "name": "string", "email": "user@example.com" \}} \\
  \hline
  \texttt{book\_service} & 8002 & \text{CRUD книг + остатки} & \texttt{http://localhost:8002/docs} & \texttt{\{ "title": "string", "author": "string", "price": 0, "stock": 0 \}} \\
  \hline
  \texttt{order\_service} & 8003 & \text{Оформление заказов} & \texttt{http://localhost:8003/docs} & \texttt{\{ "user\_id": 0, "book\_id": 0, "quantity": 0 \}} \\
  \hline
  \texttt{postgres} & 5432 & \text{PostgreSQL, одна БД "microservices", схемы разные} & \text{---} & \text{---} \\
  \hline
\end{array}
$$

Как работать с проектом:

Клонируем репозиторий и переходим в директорию microservices_project

Запускаем проект: для этого пишем в терминале 'docker compose up --build'

Открываем браузер и переходим в нужный нам сервис(ссылки написаны выше в таблице выше). Можно поработать как с отедльным сервисом (порты 8001, 8002, 8003), так и со всеми вместе через единую точку входа (порт 8000). 

Для регистрации нового пользователя/сохранения книги(пополнение на складе)/регистрации заказа:

$\text{---}$ отдельно через каждый сервис

В POST нажимаем Try it out и заполняем тело запроса, после чего жмем Execute.

$\text{---}$ через единую точку входа

- В POST нажимаем Try it out

- service = path = название выбранного сервиса(users/books/orders)

- Заполняем тело запроса в зависимости от сервиса(т.е прописываем данные для выбранного сервиса согласно таблице выше)

Для проверки сохранения пользователя/книги/заказа:

$\text{---}$ отдельно через каждый сервис

- в браузере: В GET нажимаем Try it out, а далее Execute

- через терминал : srv=users/books/orders
docker run --rm --network microservices_project_default \
  -e PGPASSWORD=postgres \
  postgres:15 psql -h postgres -U postgres -d microservices \
  -c '\pset border 2' -c "SELECT * FROM $srv;"

$\text{---}$ через единую точку входа

- в браузере: В GET нажимаем Try it out, service = path = название выбранного сервиса(users/books/orders), далее нажимаем Execute

- через терминал: мы можем проверить не только сервисы по отдельности, как написано выше, но и все сразу:  docker run --rm --network microservices_project_default \
  -e PGPASSWORD=postgres \
  postgres:15 psql -h postgres -U postgres -d microservices \
  -c '\pset border 2' \
  -c 'SELECT * FROM users;' \
  -c 'SELECT * FROM books;' \
  -c 'SELECT * FROM orders;'

Для завершения прописываем в командной строке docker compose down