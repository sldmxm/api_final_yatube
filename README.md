# API для социальной сеть микроблогов
API для проекта "[Социальная сеть микроблогов](https://github.com/sldmxm/yatube_final)", который позволяет публиковать посты с картинками, првязывать их к группам и авторам, комментировать, редактировать и удалять.
Еще пользователи серивиса могут подписываться друг на друга.

Написан для практического изучения Django REST.

## Технологии в проекте
- Python
- Django
- DRF
- Unittest
- PostgreSQL
- Gunicorn
- nginx
  
## Примеры API-запросов
* Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

    `GET /api/v1/posts/` 


* Добавление новой публикации в коллекцию публикаций. 

    `POST api/v1/posts/`
    
    `{
        "text": "string",
        "image": "string",
        "group": 0
}`


* Получение, замена, редактирование, удаление публикации по id.

  `GET, PUT, PATCH, DELETE  /api/v1/posts/{id}/` 

Полная документация по API [доступна](http://127.0.0.1:8000/redoc/) после запуска проекта.

## Установка и запуск
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/sldmxm/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3.8 -m venv venv
```

```
. venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
