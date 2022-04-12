import fastapi
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles #No CSS being used currently
from fastapi.templating import Jinja2Templates

#Instantiation of application, similar to Flask
app = FastAPI()

#Connecting templates folder to application
templates = Jinja2Templates(directory="templates")

#Mounting CSS to the application. None used currently.
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#Runs application with ./main.py terminal command
if __name__ == '__main__':
    uvicorn.run(app) 