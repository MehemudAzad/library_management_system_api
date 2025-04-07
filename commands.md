# Commands

django-admin startproject project

./manage.py runserver

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

## If we want to delete the current database

rm db.sqlite3  # or drop the database if using PostgreSQL/MySQL                                 ─╯
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

python manage.py makemigrations                                                          ─╯
python manage.py migrate
