
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///project.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_pic(link):
	pic=Doggo(link=link)
	session.add(pic)
	session.commit()
def get_all():
	doggoes=session.query(Doggo).all()
	return doggoes