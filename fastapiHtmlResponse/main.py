from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI()

templates = Jinja2Templates(directory="htmldirectory")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    user = "tanmaya"
    return templates.TemplateResponse("demo.html",{"request": request, "user":user})