# Stripe Ali

stripe.com/docs - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 

## Запуск с Docker

1. Склонировать репозиторий с Github.com:
````
https://github.com/Povarenskiy/stripe_api.git
````
2. В файле .evn заполнить необходимые данные по ключам
```
STRIPE_SECRET_KEY = '<your secret key>'
STRIPE_PUBLIC_KEY = '<your public key>'
```

3. Запустить контейнер 
````
docker-compose up
````
#  # docker exec -it stripe_api python manage.py createsuperuser


## Стандартные установка и запуск

1. Склонировать репозиторий с Github.com:
````
https://github.com/Povarenskiy/stripe_api.git
````

2. В директории проекта создать виртуальное окружение (venv/ — название виртуального окружения)
````
python -m venv venv
````

3. Активировать виртуальное окружение 
````
venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux и MacOS
````
4. В файле .evn заполнить необходимые данные по ключам
```
STRIPE_SECRET_KEY = '<your secret key>'
STRIPE_PUBLIC_KEY = '<your public key>'
```

5. Установка зависимостей
````
pip install -r requirements.txt
````

6. Создать и применить миграции в базу данных
````
python manage.py makemigrations
python manage.py migrate
````

7. Запустить сервер
````
python manage.py runserver
````

## Api

````http://127.0.0.1:8000/admin```` - панель админа

````http://127.0.0.1:8000/buy/{id}```` - возвращает Stripe Session Id для оплаты выбранного Item

````http://127.0.0.1:8000/item/{id}```` - страница с Item

````http://127.0.0.1:8000/order/{id}```` - страница с Order



## Техзадание 

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель Item с полями (name, description, price) 
- API с двумя методами:
  - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
  - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
- Пример реализации можно посмотреть в пунктах 1-3 тут
- Залить решение на Github, описать запуск в Readme.md
- Опубликовать свое решение чтобы его можно было быстро и легко протестировать. Решения доступные только в виде кода на Github получат низкий приоритет при проверке.

Бонусные задачи: 
-Запуск используя Docker
-Использование environment variables
-Просмотр Django Моделей в Django Admin панели
-Запуск приложения на удаленном сервере, доступном для тестирования
-Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
-Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
-Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
-Реализовать не Stripe Session, а Stripe Payment Intent.
