# flash
fastapi, fast-api

# Prerequisite
* [Python3.10+](https://www.python.org/downloads/)

**Coding Standards**
* [PEP8](https://code.visualstudio.com/docs/python/linting)

# FastAPI CMD

Run the server
```
uvicorn main:app --reload
```
The command uvicorn main:app refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of main.py with the line `app = FastAPI()`.
* `--reload`: make the server restart after code changes. Only do this for development.

# Swagger
FastAPI have it's own swagger implementation

* [Swagger](http://127.0.0.1:8000/docs)
* [OpenAPI](http://127.0.0.1:8000/redoc)

# Debugger For VS-Code
Create a folder `.vscode` in the root directory and create a file `launch.json`
```
mkdir .vscode
cd .vscode
touch launch.json
```
Past this code in `.vscode/launch.json`
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```
# Packages And Uses

**[pydantic](https://docs.pydantic.dev/latest)**

Pydantic is a data validation and settings management library for Python. It provides a way to define data schemas, validate input data against these schemas, and automatically generate Python objects from validated data. It is commonly used in web frameworks like FastAPI and Flask to validate and serialize request and response data. Pydantic is built on top of Python's type annotations and provides additional features like field validation, data parsing and serialization, and custom data types.