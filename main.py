# Импортирование библиотек/классов/функций
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data.db_utilities.setup import setup_db
from data.datamodel.create_demo_db import seed_users
from data.db_utilities.session import DemoSession
from data.datamodel.create_demo_db import User

setup_db()
seed_users()

app = FastAPI()

# Подключение статических файлов (CSS, JS, изображения)
app.mount(
    '/static',
    StaticFiles(directory='static'),
    name='static'
)

# Настройка движка шаблонов Jinja2
templates = Jinja2Templates(directory='templates')


# Главная страница: получение списка пользователей и рендеринг HTML
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Запрос к БД через SQLAlchemy для получения всех пользователей
    with DemoSession.get_session() as session:
        users_list = session.query(User).all()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"users": users_list}
    )
