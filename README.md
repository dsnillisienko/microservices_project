$$\text{Летняя практика "Микросервисные взаимодействия"}

Мой проект представляет собой магазин книг на микросервисах, упакованных в Docker Compose.

Для начала рассмотрим саму архитектуру:

$$\begin{array}{|l|c|l|c|}
  \hline
  \text{Сервис} & \text{Порт} & \text{Какую задачу решает}\\
  \hline
    \text{api_gateway} & 8000 & \text{Единая точка входа (прокси на другие сервисы)}\\
  \hline
  \text{user_service} & 8001 & \text{CRUD пользователей}\\
  \hline
  \text{book_service} & 8002 & \text{CRUD книг + остатки}\\
  \hline
  \text{order_service} & 8003 & \text{Оформление заказов}\\
  \hline
  \text{postgres} & 5432 & \text{PostgreSQL, одна БД `microservices`, схемы разные}\\
  \hline
\end{array}$$
