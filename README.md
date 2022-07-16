 ## Приложение «Продуктовый помощник»

 ![workflow](https://github.com/HelloAgni/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

 Cайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

docker compose up -d

docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py collectstatic --noinput
