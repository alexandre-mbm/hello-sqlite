from sqlalchemy import create_engine

url = 'https://www.clubedohardware.com.br/discover/575.xml/?member=435193&key=70f17e1599fea3a744c19502ff5b612b'
database = 'sqlite:////data/data/com.termux/files/home/python/software/cdh-scout/data.db'

engine = create_engine(database)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Message(Base):
  __tablename__ = 'unread_foruns'
  
  #id = Column(Integer, primary_key=True, autoincrement=True)
  #link = Column(String, unique=True)
  link = Column(String, primary_key=True)
  title = Column(String)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

link='jghj'
query = session.query(Message)
results = query.filter(Message.link==link)
instance = results.first()
if instance is None:
  instance = Message(
    link=link, title='hff'
  )

session.add(instance)
session.commit()
session.close()
