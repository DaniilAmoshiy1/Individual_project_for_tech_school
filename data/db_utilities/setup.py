from data.datamodel.model_base import SqlAlchemyBase
from .session import DemoSession


def reset_db():
    SqlAlchemyBase.metadata.drop_all(DemoSession.engine)


def setup_db():
    SqlAlchemyBase.metadata.create_all(DemoSession.engine)

