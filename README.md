[![workflow](https://github.com/Kors557/foodgram-project-react/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/Kors557/foodgram-project-react/actions/workflows/main.yml)

# Дипломный проект — сайт Foodgram, «Продуктовый помощник».
Онлайн-сервис и API для него. На этом сервисе пользователи 
могут публиковать рецепты, подписываться на публикации других 
пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

## Установка проекта на боевом сервере
Форкнуть репозиторий:
```
git clone git@github.com:Kors557/foodgram-project-react.git
```
Зайти на Git-Settings-Secrets-Action и заполнить следующие параметры:
```
DB_ENGINE - тип Базы Данных
DB_HOST - контейнер БД
DB_NAME - имя БД
DB_PORT - порт БД
POSTGRES_USER - пользователь в БД
POSTGRES_PASSWORD - пароль пользователя в БД
DOCKER_PASSWORD - пароль к докерхаб
DOCKER_USERNAME - логин к докерхаб
HOST - адрес боевого сервера
USER - логин к боевому серверу
PASSPHRASE - пароль боевого сервера, если есть
SSH_KEY - приватный ключ локальной машины
TELEGRAM_TO - ваш ID в Telegram мессенджере
TELEGRAM_TOKEN - токен
```

Проект разоваричвается после выполнения команды `git push` в репозиторий GitHub.

В разделе GitHub Actions можно отследить все стадии развертывания проекта 
согласно инструкциям workflow файла.

Установите docker.io командой `sudo apt install docker.io ` и docker-compose 
командой `sudo apt install docker-compose`

После успешного workflow, запустить следующие команды:

`sudo docker-compose exec backend python manage.py createsuperuser` и
создаем суперпользователя.

Копируем статику `sudo docker-compose exec web python manage.py collectstatic --no-input`.

Копируем из csv файла тэги `sudo docker-compose exec web python manage.py load_tags.py`.

Копируем из csv файла ингредиенты `sudo docker-compose exec web python manage.py load_ingredients.py`.

**Автор:**

[Корсаков Александр.](https://github.com/Kors557)