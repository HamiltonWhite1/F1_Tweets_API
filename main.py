import fastapi
import uvicorn
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models 
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles #No CSS being used currently
from fastapi.templating import Jinja2Templates

#Instantiation of application, similar to Flask
app = FastAPI()

#Connecting templates folder to application
templates = Jinja2Templates(directory="templates")

#Mounting CSS to the application. None used currently.
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tweets", response_class=HTMLResponse)
async def read_tweet(db: Session=Depends(get_db)):
    tweets = db.query(models.Tweet).limit(10).all()
    for tweet in tweets:
        print(tweet.user['screen_name'])
    return "hello"

#Runs application with ./main.py terminal command
if __name__ == '__main__':
    uvicorn.run(app) 