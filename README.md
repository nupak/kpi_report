# kpi_report
Django project with templates. Calculating KPI

<h2>Первичная настройка системы</h2>

<p>Установка виртуального окружения</p>
python -m venv venv

<p>Устанока зависимостей</p>
pip install -r reqirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic

python manage.py runserver
