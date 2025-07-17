-- создаём БД и пользователя для демо
CREATE DATABASE microservices;
CREATE USER practice WITH PASSWORD 'practice';
GRANT ALL PRIVILEGES ON DATABASE microservices TO practice;
