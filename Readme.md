## Create a virtual environment and install django

```bash
pipenv install pep8 --dev
pipenv install autopep8 --dev
pipenv install django
pipenv install pillow
pipenv shell
```

## Create Project

```bash
django-admin startproject phonebook .
```

## Check the server for the first time

```bash
manage.py migrate
manage.py createsuperuser
manage.py runserver
```

## Create App

```bash
django-admin startapp phonebook_app
```

## Create super-user

```bash
manage.py createsuperuser
```

## shell commands

> play with some shell commands

`manage.py shell`

```bash
>>> from phonebook_app.models import *

>>> Contact.objects.create(first_name="new shell name", last_name="new shell Lname", notes="notes")
>>> c = Contact.objects.filter(first_name__icontains='new shell name')[0]
>>> Phone.objects.create(phone="03-3333333", contact=c)
>>> Email.objects.create(email="1234@gmail.com", contact=c)
##or##
>>> c = Contact(first_name='John', last_name='Smith', notes='notes')
>>> c.save()
>>> p = Phone(phone="03-6666666", contact=c)
>>> p.save()
>>> c = Contact.objects.filter(first_name__icontains='John')[0]
>>> e = Email(email="123@gmail.com", contact=c)
>>> e.save()

>>> Contact.objects.all()
```

## fix vulnerabilities

```bash
# check for vulnerabilities
osv-scanner -r .
# find outdated packages
pip3 list --outdated
# update packages
pip3 list --outdated --format=json | jq -r ".[] | .name+\"==\"+.latest_version" | xargs -n1 pip3 install -U
# save packages to requirements.txt
pip3 freeze > requirements.txt
# check the app is working
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8080
```
