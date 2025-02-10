
from ..database import Base
from sqlalchemy import Column, DateTime, Integer, VARCHAR

class Log(Base):

    __tablename__ = 'TLog' 

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, nullable= False)
    log = Column(VARCHAR(200), nullable= False)


# depois de criar a classe, entrar no venv e rodar o comando
# 'poetry run alembic revision --autogenerate -m "[mensagem]"'
# para criar a revisão e 
# 'poetry run alembic upgrade head para comitar no banco de dados'
