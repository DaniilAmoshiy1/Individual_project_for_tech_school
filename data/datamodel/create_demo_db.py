from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.exc import IntegrityError

from data.datamodel.model_base import SqlAlchemyBase
from data.db_utilities.session import DemoSession

class User(SqlAlchemyBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    age: Mapped[int] = mapped_column(Integer)

# Произошла проблема из за которой пришлось сделать создание здесь
SqlAlchemyBase.metadata.create_all(DemoSession.engine)

def create_user(name: str, age: int):
    with DemoSession().get_session() as session:
        try:
            new_user = User(name=name, age=age)
            session.add(new_user)
            session.commit()
        except IntegrityError:
            session.rollback() # Отменяем падение
            print(f"Пользователь {name} уже существует, пропускаем...")

user_1 = create_user('Даня', 19)
user_2 = create_user('Артём', 16)
user_3 = create_user('Саня', 16)

