from secao06.core.configs import settings
from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship


class ArtigoModel(settings.DBBaseModel):
    __tablename__ = 'artigos'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    titulo = Column(String(256))
    url_fonte = Column(String(256))
    descricao = Column(String(256))
    usuario_id = Column(INTEGER, ForeignKey('usuarios.id'))
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined')
