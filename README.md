# Eccomerce Web App

## Backend Setup

### Installation

- `Create Virtual Env`
```
python3 -m venv venv
```

- `Activate Virtual Env`
```
source venv/bin/activate
```

- `Install Django`
```
python3 -m pip install django 
```

### Create Django project

- `Create Django Project`
  ```
  django-admin stratproject backend .
  ```

- `Install Requirements`
  ```
  pip install djangorestframework==3.14.0 djangorestframework-simplejwt==5.2.2 PyJWT==2.6.0
  ```

- `Create Requirement.txt`
  ```
  pip freeze > requirements.txt
  ```

- `Create Django app`
  ```
  python3 manage.py startapp app_name
  ```
  - Add the app in INSTALLED_APPS inside setting.py

- `Run Django Project`
  ```
  python manage.py runserver
  ```

### django-jazzmin
  - use to customize admin
  ```
  pip install django-jazzmin
  pip freeze > requirements.txt
  ```
### Create Superuser
  ```
  python3 manage.py createsuperuser
  ```

### Custom User Model



## Frontend Setup

### Installation

- `Create React App`
  ```
  npx create-react-app frontend --use-npm
  ```