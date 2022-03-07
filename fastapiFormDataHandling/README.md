# Fastapi handling form data

This is a simple fastapi program for handling form data




## Usage/Examples
main.py for handling the form data.
```python
from fastapi import FastAPI, Request, Form, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="htmldir")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/formdata")
async def posting_data(name: str = Form(...), age: int = Form(...), myfile: UploadFile = Form(...)):
    print(myfile.filename)
    content = await myfile.read()
    return {"name": name, "age": age, "file_content":content}

```


## Installation

install uvicorn server for running the fastapi app

```bash
  pip install uvicorn
```


Install jinja2 for rendering the html page from restapi

 ```bash
  pip install jinja2
```

Install python-multipart for handling form data

 ```bash
  pip install python-multipart
```
## Run Locally


Go to the project directory

```bash
  cd fastapiFormDataHandling

```


Start the server

```bash
  uvicorn main:app --reload
```
