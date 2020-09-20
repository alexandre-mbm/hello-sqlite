from sqlalchemy import create_engine

dialect = 'sqlite:///'
root = '/data/data/com.termux/files'
dir = '/home/python/software/hello-sqlite/'
filename = 'data.db'

database = dialect + root + dir + filename
engine = create_engine(database)