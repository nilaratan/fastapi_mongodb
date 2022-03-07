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