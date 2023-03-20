# kpi_report
Django project with templates. Calculating KPI

<h2>Первичная настройка системы</h2>

<p>Установка виртуального окружения</p>
python -m venv venv

Устанока зависимостей
pip install -r reqirements.txt

<h2>Настройка Django и создание базы данных и необходимых маграций для старта</h2>    
-python manage.py makemigrations

-python manage.py migrate

-python manage.py collectstatic

<h1>Старт сервера</h1>
python manage.py runserver
