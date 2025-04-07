# Commands

--> creating virtual environment venv(like node modules when working with expressjs)
python3 -m venv venv
--> inorder to activate tthe virtual environment
source venv/bin/activate

--> to get started with the project(including a (.) after the (project .) doesn't create the extra project folder, but its a good practice to create it and keep things organized
django-admin startproject project
--> for creating the api folder inside project. Make sure to update the settings
python manage.py startapp api

update the settings file in core whenever needed

--> if downloaded from another repository
pip install -r requirements.txt

--> this updates the requirements.txt file or creates if does not have any
pip freeze > requirements.txt

## Database operations

### If we want to delete the current database

rm db.sqlite3  # or drop the database if using PostgreSQL/MySQL
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

python manage.py makemigrations
python manage.py migrate
--> for running the server
python manage.py runserver




extras

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())