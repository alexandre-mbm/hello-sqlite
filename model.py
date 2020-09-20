from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy import Integer, String

class Message(Base):
  __tablename__ = 'messages'
  id = Column(Integer, primary_key=True, autoincrement=True)
  text = Column(String, unique=True)
  resume = Column(String)

from properties import engine
Base.metadata.create_all(engine)
