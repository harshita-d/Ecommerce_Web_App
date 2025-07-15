# Eccomerce Web App

## Backend Setup

### Installation

- install Docker Desktop for macos
- install GIT
- Clone Repo
- docker compose build       # build images
- docker compose up -d       # start services in detached mode


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