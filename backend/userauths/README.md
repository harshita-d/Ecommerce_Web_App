# Custom User Model

## User Model

  - 
  - Changing `USERNAME_FIELD` to `email` makes the email address the primary identifier for authentication instead of `username`.
  - `REQUIRED_FIELDS` attribute of a custom user model is a list of field names that are required when creating `superuser`.
  - Django's superuser creation process expects at least one field other than the `USERNAME_FIELD` to be explicitly marked as required. 
  - if we don't define `REQUIRED_FIELDS` and our `USERNAME_FIELD` is set to `email`, superuser will be created with only an email and a password. which might cause some issue with third-party packages which assumes the presence of `username`.
  - `AbstractUser` is a pre-built full featured User Model provided by django. it includes all the fields and methods of default User models like `username`, `email`, `first_name`, `last_name` with field for authentication and permissions.
    - We use `AbstractUser` when we need a custom user model but still want most of the default user functionality without having to build ourselves.
  - `AbstractBaseUser` class provides only the core functionlaity required for `authentication` like password handling and authentication token, rest we have to define all fields like email, username etc, and implement some functions.  
    - `AbstractBaseUser` is used when we nee complete control over the structure and behavior of the user model 
  - `null=True` affects the `database` level, allowing the fields to store `null` values if no data is provided.
  - `blank=True` affects from `validation`, making the field optional. 
  - `__str__` method is used to return human readable string representation of the object. this is particlulary usefull where info is shown to identify the objects.
    - when we view records in admin panel, django call `__str__` method to display each record.
    - when view an object in console, django displays `__str__` output.
    - if we do not define `__str__` method, django uses default `__repr__` method, which return something not useful.
  - the `save` method is an in built method in models, it allows `overriding` the save method to add `custom` behavior before or after saving the `instance`. 
    - the `super` is used to call the save method of the parent class of the User model. This ensures django's built in behavior for saving a model instance is executed after any custom logic defined in the overridden save method.

