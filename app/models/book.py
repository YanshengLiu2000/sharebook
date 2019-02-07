
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

# from sharebook import app

db=SQLAlchemy()

class Book(db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(50), nullable=False)
    author=Column(String(30),default='Zhazha')
    binding=Column(String(20))
    publisher=Column(String(50))
    price=Column(String(20))
    pages=Column(Integer)
    puddate=Column(String(20))
    isbn=Column(String(15), nullable=False,unique=True)
    summary=Column(String(1000))
    image=Column(String(50))

    def __repr__(self):
        return '<Book: {}>'.format(self.title)

