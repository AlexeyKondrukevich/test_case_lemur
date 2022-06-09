## <h1 align="center"> Тестовое задание "Сайт компании, занимающейся акватерапией" </h1>
>"Water could make you better" 

![](https://img.shields.io/badge/Developed%20by-Kondr-blue)

## Описание
Данный проект представляет собой сайт компании с возможностью записи на сеанс.  


### Используемые технологии:

* Python 3.8
* Django 2.2
* Немного СSS
* Немного JS
* Немного HTML
* И сколько-то PHP

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlexeyKondrukevich/test_case_lemur.git
```

```
cd test_case_lemur
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
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
cd test_case
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

