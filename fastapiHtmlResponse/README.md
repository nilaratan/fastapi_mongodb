
# Fastapi HTML Response

This is a simple fastapi project for returning a HTML response




## Usage/Examples
main.py for HtML response.
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="htmldirectory")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    user = "tanmaya"
    return templates.TemplateResponse("demo.html",{"request": request, "user":user})

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


## Run Locally


Go to the project directory

```bash
  cd fastapiHtmlResponse
```


Start the server

```bash
  uvicorn main:app --reload
```

