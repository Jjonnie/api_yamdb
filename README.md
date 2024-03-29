# API_YAMDB
## Учебный проект на курсе Python-разработчик Яндекс-Практикума.

### Концепция проекта
Данный проект является работой студентов, в котором главной целью было отточить навыки проектирования, создания и отладки API на базе архитектуры REST с использованием Django Rest Framework.


### В ходе проекта:

  * были изучены теоретические основы разработки проектов API на базе REST;
  * отработаны навыки составления разных типов запросов (GET, POST, PUT и т.д.) к различным таблицам (Title, Genre, Review, Comment) базы данных;
  * изучены практические приёмы решения различных прикладных задач (валидация, кастомизация модели User и т.д.);
  * получены навыки командрой работы в Git.


### Описание проекта:

Проект YaMDb - это платформа для сбора и хранения отзывов пользоватей на произведения разных категорий, таких как книги, фильмы или музыка. Пользователи могут оставлять текстовые отзывы и ставить оценки произведениям в диапазоне от 1 до 10. Администраторы могут добавлять произведения, категории и жанры. Пользователи могут оставлять комментарии к отзывам. В проекте реализован функционал для усреднения оценок и формирования рейтинга для каждого произведения.


### Примеры запросов и ответов:

### GET: /api/v1/titles/{title_id}/reviews/ ###
*200:* 
```JSON
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "text": "string",
      "author": "string",
      "score": 1,
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
```
### POST: /api/v1/titles/{title_id}/reviews/ ###
*400:* 
```JSON
{
  "field_name": [
    "string"
  ]
}
```
### POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/ ###
*201:*
```JSON
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```

## Полный список эндпоинтов: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
### *ПРЕДВАРИТЕЛЬНО УБЕДИТЕСЬ, ЧТО ПРОЕКТ ЗАПУЩЕН*

### Как запустить проект ###
* Клонировать репозиторий и перейти в него в командной строке: 
```bash
git clone https://github.com/Jjonnie/api_yamdb/
```
```bash
cd api_yamdb
```
* Cоздать и активировать виртуальное окружение: 
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
* Установить зависимости из файла requirements.txt:

```bash
python -m pip install --upgrade pip 
```
```bash
pip install -r requirements.txt 
```
* Выполнить миграции:
```bash
python manage.py migrate 
```
* Запустить проект:
```bash
python manage.py runserver
```
* Запустить скрипт для загрузки тестовых данных:
```bash
python manage.py runscript load_csv_to_db
```

### Авторы: 
### Александр Новиков, @alexander_novikov
### Шульман Евгений, @jonnie.gray
### Илья Корепанов, @ikorepanov
