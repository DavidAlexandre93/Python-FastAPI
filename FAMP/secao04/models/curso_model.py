from secao04.core.configs import settings
from sqlalchemy import Column, INTEGER, String


class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'

    id: int = Column(INTEGER, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(INTEGER)
    horas: int = Column(INTEGER)
