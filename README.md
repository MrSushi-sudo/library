Тестовое API Библеотеки

URL Авторов: "http://127.0.0.1:8000/api/authors/"


URL Книг:"books": "http://127.0.0.1:8000/api/books/"

При запуске отредиректит на /api/

Админка /admin/ доступна, на всякий случай

Окружение и пакеты:

1) python -m venv venv

2) venv\Scripts\activate

3) pip install -r requirements.txt

4) Либо настроить в пайчарме settings - Python Interpreter

Запуск тестов: python manage.py test

Собрать контейнер: docker build -t libary .

Запуск к примеру на 8000: docker run -p 8000:8000 libary
