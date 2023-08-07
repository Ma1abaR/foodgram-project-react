# Foodgram - социальная сеть о кулинарии
### Делитесь рецептами и пробуйте новые
---

### Возможности сервиса:
- делитесь своими рецептами
- смотрите рецепты других пользователей
- добавляйте рецепты в избранное
- быстро формируйте список покупок, добавляя рецепт в корзину
- следите за своими друзьями и коллегами

### Технологии:
- Django 
- Python 
- Docker 

### Установка и запуск проекта: 
1. Склонируйте репозиторий: 
```
git clone https://github.com/ma1abar/foodgram-project-react.git
```
2. Подготовьте сервер:
```
scp docker-compose.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
scp .env <username>@<host>:/home/<username>/
```
3. Установите Docker и Docker Compose: 
```
sudo apt install docker.io 
sudo apt install docker-compose
```
4. Соберите контейнер и выполните миграции:
```
sudo docker-compose up -d --build
sudo docker-compose exec backend python manage.py migrate
```
5. Создайте суперпользователя и соберите статические файлы: 
```
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
6. Загрузите данные о ингредиентах и тегах из файлов json: 
```
sudo docker-compose exec backend python manage.py loadmodels --path 'recipes/data/ingredients.json'
sudo docker-compose exec backend python manage.py loadmodels --path 'recipes/data/tags.json'
```
7. Проект развернут на сервере: http://cookfoodeat.myftp.org
8. Суперпользователь:
```
email: extrimiti@yandex.ru
password: ppp0633856
```

### Проект выполнил студент Яндекс Практикума
### [Artur](https://github.com/Ma1abaR)
