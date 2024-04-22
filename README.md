## API для Yatube 2:
В данном проекте реализована функциональность Rest API на базе Django Rest API. С помощью данного API можно получать доступ к постам, комментариям, группам и подпискам пользователей в соответствии с правами доступа (например, пользователь не может отредактировать чужой пост или комментарий). С полной функциональностью данного проекта можно ознакомиться по следующему эндпоинту (если проект запущен на локальной машине):
```
http://127.0.0.1:8000/redoc/
```
Данный проект использует следующий стек: Python, Django, DjangoORM, Django Rest API, JSON, SQLite

Из проекта исключёны фронтенд и view-функции

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
* Если у вас Linux/macOS
```
source env/bin/activate
```
* Если у вас windows
```
source env/scripts/activate
```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
### Примеры запросов и ответов

Получить список постов (метод  GET)
```
.../api/v1/posts/
```
ответ (код 200)
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Добавить комментарий к посту (метод POST)
```
.../api/v1/posts/{post_id}/comments/
```
ответ (код 201)
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
ответ (код 400)
```
{
  "text": [
    "Обязательное поле."
  ]
}
``` 
Подробнее о всех методах API написано в документации.
Связь с автором: abramian.vl@phystech.edu