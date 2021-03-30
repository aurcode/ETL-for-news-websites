from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def createEngine(name):
    engine = create_engine('sqlite:///newspaper-{}.db'.format(name))
    Session = sessionmaker(bind=engine)
    return (engine, Session)

Base = declarative_base()
