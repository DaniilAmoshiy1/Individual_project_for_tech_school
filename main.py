from data.db_utilities.setup import setup_db

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount(
    '/static',
    StaticFiles(directory='static'),
    name='static'
)

templates = Jinja2Templates(directory='templates')

setup_db()

@app.get("/", response_class=HTMLResponse)
async def index(request):
    return templates.TemplateResponse('index.html', {"request": request})
