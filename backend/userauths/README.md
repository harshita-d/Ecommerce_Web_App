# Custom User Model

## User Model

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

- if get `inconsistencyerror` while `migrations` than comment out `'jazzmin','django.contrib.admin'` from setting file and again run the commands and also in urls.py comment `admin.site.url `

## Signals

- signals are a way of allowing decoupled applications to get notified when certain actions occur elsewhere in the framework.
- They implement the observer pattern, so that “senders” emit notifications and any number of “receivers” can listen and react.
- `Senders`: A sender is any piece of code that emits (“sends”) a signal. In most cases you’ll use one of Django’s built-in signals, such as pre_save, post_save, pre_delete, post_delete, etc.
- `Receivers`: A receiver is simply a function (or any callable) that takes some specific arguments and performs work when it’s called.
- `Connecting`: You register (connect) a receiver to a signal with:

```python
from django.db.models.signals import post_save
post_save.connect(my_receiver, sender=MyModel)
```

- New User Creation
  - You call User.objects.create_user(...) or user.save() on an unsaved User.
  - Django saves the User to the database.
  - It then emits the post_save signal.
  - create_user_profile is called with created=True.
  - Inside it, `Profile.objects.create(user=instance)` runs, making a new row in the Profile table linked by the OneToOneField (or ForeignKey) to that User.
- Subsequent Saves

  - When you edit and save the same User again, Django emits post_save with created=False.
  - create_user_profile sees created=False and does nothing.
  - save_user_profile runs and calls instance.profile.save(), ensuring any changes on the profile side (or related signals) propagate.

- `Ready function`:
  - Django only auto-imports certain well-known modules (like your app’s models.py), not every file you happen to have in your package.
  - Your signals.py lives “off to the side” and won’t ever be executed unless something actually imports it.
  - in your AppConfig’s ready() method: Signals get hooked up exactly once, right after all models are loaded but before any requests are handled.

## Memory allocation

- Module Loading & Class Creation

  - `Bytecode Compilation`
    - When Python first imports your .py file, it compiles it to bytecode—this allocates memory for code objects (functions, class definitions, the module body).
  - `Executing the class Statement`
    - A new class object of type ModelBase is created on the heap via `type.__call__`.
    - Memory is allocated for its namespace dictionary `(User.__dict__)`, which holds entries for:
      - Field descriptors `("username" → <CharField object>)`,
      - Methods `("save" → function object)`,
      - Constants `("USERNAME_FIELD" → "email")`, etc.
    - At the end of this step, the module’s globals gain a reference to that class object.
    ```python
    module globals ──> User (class object)
                    └─ User.__dict__ ──> {"username": CharField, …}
    ```

- Instantiating an Object
  ```python
  u = User(email="a@b.com", username="alice")
  ```
  - Allocate Instance Memory `(__new__)`
    - `User.__new__` (usually inherited from object) calls into the allocator, carving out a block of memory on the heap sized for a User instance.
    - This block includes space for:
      - A pointer to its type object `(User)`,
      - A pointer to its `instance dictionary` (initially NULL or a pointer to an empty dict),
      - Any `__slots__` storage if defined.
  - Initialize the Instance `(__init__)`
    - Python then calls `User.__init__(self, …)`.
    - The first time you assign to any attribute on self, Python ensures an empty `self.__dict__` is created (allocating a small hash table).
    - Each self.attr = value stores entries in that hash table, which may resize (rehash) as it grows.
    ```python
    User() ──> allocate instance ──> u
            └─ u.__dict__ initially empty
    ```
    - Setting Attributes
    ```python
    u.full_name = "alice"
    ├─ Descriptor? → CharField.__set__(u, "alice")
    └─ else → u.__dict__["full_name"] = "alice"
    ```
