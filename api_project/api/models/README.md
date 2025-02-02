

this directory contains the models for the database structure.
Each class is a table that NEEDS to be imported to database.py AND by the __init__.py file to update the metadata of the base class.


remember to activate the virtual env before trying to migrate the database
```
$.\.venv\Scripts\activate
```

to create a revision with alambic, run
```
$poetry run alembic revision --autogenerate -m "[message]"
```

to update the database, run
```
$ poetry run alembic upgrade head
```