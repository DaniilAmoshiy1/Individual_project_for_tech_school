from data.config import DB_CONNECTION_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DemoSession:
    engine = create_engine(DB_CONNECTION_URL, echo=True)

    @classmethod
    def get_session(cls):
        session_class = sessionmaker(bind=cls.engine)
        session = session_class()
        session.commit()
        return session
