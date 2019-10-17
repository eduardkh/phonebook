## Create a virtual environment and install django

```
pipenv install pep8 --dev
pipenv install autopep8 --dev
pipenv install django
pipenv install pillow
pipenv shell
```

## Create Project

```
django-admin startproject phonebook .
```

## Check the server for the first time

```
manage.py migrate
manage.py createsuperuser
manage.py runserver
```

## Create App

```
django-admin startapp phonebook_app
```

## Create super-user

```
manage.py createsuperuser
```
