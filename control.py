from sqlalchemy.orm import sessionmaker
from properties import engine
from model import Message

Session = sessionmaker(bind=engine)
session = Session()

text='Hello, SQLite!'
query = session.query(Message)
results = query.filter(Message.text==text)
instance = results.first()
if instance is None:
  instance = Message(
    text=text, resume='Hi'
  )

#TODO exemplo com merge()

session.add(instance)
session.commit()
session.close()