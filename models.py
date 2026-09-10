from database import Base
from sqlalchemy import Column,String,Integer,Boolean


class Heroes(Base):
    __tablename__ = "heroes"
    id = Column(Integer,autoincrement=True,index=True,primary_key=True )
    name= Column(String)
    title= Column(String)
    power= Column(String)
    role=Column(String)
    image= Column(String)
    rarity= Column(Integer)
    active= Column(Boolean)
