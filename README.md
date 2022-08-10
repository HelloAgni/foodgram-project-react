 ## Продуктовый помощник - foodgram

 ![workflow](https://github.com/HelloAgni/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

---

 Приложение, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «cписок покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд. Есть возможность выгрузить файл (.txt) с перечнем и количеством необходимых ингредиентов для рецептов.

 ***Для работы с проектом необходимо выполнить действия, описанные ниже.***

 ```bash
git clone <project>
cd foodgram-project-react/infra/
# сделайте копию файла <.env.example> в <.env>
cp .env.example .env
 ```

**Docker**
 ```bash
docker compose up -d
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --noinput
# Для заполнения базы Тегами и ингредиентами выполните:
docker-compose exec backend python manage.py import_tags
docker-compose exec backend python manage.py import_ingredients
# Для заполнения базы пользователями и рецептами выполните:
docker-compose exec backend python manage.py data_test
```
***Тестовый пользователь и администратор***

Если выполнены все импорты в базу данных:
```bash
# Админ зона
http://localhost/admin
Login: admin
Password: admin777

# Тестовый пользователь
http://localhost/
Email: zelik1@yandex.ru
Password: Qwerty999

# Документация
http://localhost/redoc
```
**POSTMAN**  
Для полноценного использования API необходимо выполнить регистрацию пользователя и получить токен. Инструкция для ***Postman:***

Получить токен для тестового пользователя если выполнены все импорты:  
POST http://localhost/api/auth/token/login/
```json
{
    "email": "zelik1@yandex.ru",
    "password": "Qwerty999"
}
```
Без импортов, регистрируем нового пользователя  
POST http://localhost/api/users/
```json
{
    "email": "abcde@yandex.ru",
    "username": "User101",
    "first_name": "Вася",
    "last_name": "Иванов",
    "password": "Qwerty777"
}
```
Получаем токен  
POST http://localhost/api/auth/token/login/
```json
{
    "password": "Qwerty777",
    "email": "abcde@yandex.ru"
}
```
Response status 200 OK ✅
```json
{
    "token": "eyJ0e..........."
}
```
Полученный токен вставляем Postman -> закладка Headers -> Key(Authorization) -> Value (Ваш токен в формате: Token da6ee....)  

***Технологии:***  
Python 3.9, Django 3.2, DRF 3.13, Nginx, Docker, Docker-compose, Postgresql, Github Actions.  
<!-- 
***Cервер:***  
http://redsunset.ddns.net/  
http://redsunset.ddns.net/api/docs/ -->

***Превью***  
<img src="https://github.com/HelloAgni/foodgram-project-react/blob/master/backend/media/recipes/images/preview.jpg" alt="img" width="600" height='350'>
