
# Fastapi CRUD

This is a simple CRUD project of fastapi using MongoDB cloud cluster as  database and pymongo package is used to connect to the MongoDB cluster.




## Usage/Examples
config/database.py for database connection using pymongo.
```python
from pymongo import MongoClient

conn = MongoClient(connection_string)

```

models/student.py includes a student class for accepting the request body

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    add: str
```

routes/student_route.py includes all the routing functions for the CRUD request.

schemas/student_serialise.py for serializing the Cursor objects to python native dict type.

```python
# serializer for one queryset object
def student_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "age": item["age"],
        "add": item["add"]
    }

# serializer for multiple queryset object 
def students_entity(items) -> list:
    return [student_entity(item) for item in items]
```

main.py is for adding all the routes to the fastapi app

```python
from fastapi import FastAPI
from routes.student_route import student

app = FastAPI()

app.include_router(student)

```

## Installation

install uvicorn server for running the fastapi app

```bash
  pip install uvicorn
```

Install pymongo for connecting mongodb

```bash
  pip install pymongo
```

Install pydantic for creating model for request body

 ```bash
  pip install pydantic
```


## Run Locally


Go to the project directory

```bash
  cd fastapiCrud
```


Start the server

```bash
  uvicorn main:app --reload
```

