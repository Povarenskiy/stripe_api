# Stripe Ali

Пример интеграция платежной системы Stripe для оплаты отдельных товаро или заказа.

Функционал панели администратора:
- создание товаров
- выбор валюты товара
- создание заказа, в котором можно объединить несколько товаров
- добавление % налога и скидки к заказу


## Установка и запуск через Docker 

1. Клонировать репозиторий с Github.com:
````
https://github.com/Povarenskiy/stripe_api.git       # клонировать репозиторий
cd stripe_api                                       # перейти в дирректорию проекта
````
2. Два способа задать переменные окружения:

```
# В файле .evn заполнить необходимые данные по ключам
STRIPE_SECRET_KEY = '<your secret key>'
STRIPE_PUBLIC_KEY = '<your public key>'
```
или
```
# В docker-compose.yml в web добавить слой environment и указать ключи без кавычек 
web:
  environment:
    - STRIPE_SECRET_KEY=<your secret key>
    - STRIPE_PUBLIC_KEY=<your public key>

```
3. Запустить контейнер 
````
docker-compose up -d    # on windows
docker compose up -d    # on linux

````
4. В браузере перейта на 
````
http://localhost:8000/

````

### Панель администратора

1. Создать аккаунт администратора 
````
docker exec -it povarenskiy_stripe_api python manage.py createsuperuser
````
2. В браузере перейти в панель администратора
````
http://localhost:8000/admin/
````

## Api

````http://localhost:8000/buy/{id}```` - возвращает Stripe Session Id для оплаты выбранного Item

````http://localhost:8000/buy/order/{id}```` - возвращает Stripe Session Id для оплаты выбранного Order

````http://localhost:8000/item/{id}```` - страница с Item

````http://localhost:8000/order/{id}```` - страница с Order

