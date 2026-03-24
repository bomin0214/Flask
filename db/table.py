from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:0000@localhost:3306/flask_db")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

Base.metadata.create_all(engine)