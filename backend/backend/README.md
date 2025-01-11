# Django concepts

## migrations

  - `makemigrations` creates migration files based on changes made in models. these migration files act as a blueprint for how django change the database schema to match our model changes. 
    - with every make migrations it creates new migration files by comparing current state of model with last migration file.
    - It does not afffect the database direclty, 
  - `migrate` applies the migration files to database. 
    - we can also reverse back migration with ``` python manage.py <appname> <migrationname> ```

## Object-Releational-Mapping(ORM)

  - `ORM` allows developer to interact with the `database` using `Python` Code rather than writing SQL queries directly. 
  - django ORM `abstracts` the database layer, means it can easily `switch` between `databases` like from SQLite to PostgresSQL without needing to `rewrite` `quesries`.
  - `RAW SQL` is database specific like queries for PostgreSQL may not work on MySQL without modification. on the other hand Django ORM generates quesries that work across multiple databases 
  - Django's automatic schema syncronization refers to the process where ORM is combined with migration framework , means our database is always in sunc with model definations in our django application.

## Objects in Model

  - An object in a model refers to an instance of a model class. An instance refers to an object created from a class that holds data for a particluar row in DB table. 
  - A `class` is a blueprint that defines the structure and behavior of objects.
  - An `instance` is an concrete occurrence of that class with its own data. 
  - 
