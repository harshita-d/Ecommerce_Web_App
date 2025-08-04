# Django Concepts

## Project vs App

- `Project`: 
    - A Django `project` is the `container` that holds the `configuration` and `settings` for your web application(s).
    - The project provides the `environment` and `foundation` where `multiple apps` can exist and `interact`.

- `App`
    - A Django `app` is a self-contained `module` within a `project` that encapsulates a specific `piece` of `functionality` or `feature`.

> `apps` are `reusable` across projects, whereas `projects` are `unique` to a specific site.

> `manage.py` is a `command-line utility` for running `commands` like `migrations`, `server startup`, and creating new apps.
 
>  Django `project` cannot function without an `app` because apps encapsulate the actual functionality of the project, such as handling requests, managing data models, etc. Without at least one app, the project would have no functionality to execute.

> A Django app can be resude in multiple projects by 
    - creating an app and inside a project
    - create setup.py file inside project directory
        ```
        from setuptools import setup, find_packages
        setup(
            name="myapp",
            version="1.0.0",
            packages=find_packages(),
            include_package_data=True,
            install_requires=[
                "Django>=3.2",  # Specify Django version compatibility
            ],
        )
        ```
    - Package the app (e.g., using setuptools) and upload it to PyPI 
    - add the app to INSTALLED_APPS in settings.py
    - add it in urls.py


## Commands:
    - ```docker compose exec web python manage.py startapp vendor```
    - ``` docker compose exec app python manage.py makemigrations ```
    - ```docker compose exec app python manage.py migrate```



