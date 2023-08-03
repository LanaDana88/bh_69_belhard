from sqlalchemy import Column, INT





from sqlalchemy.orm import DeclarativeBase, declarative_base



class Base(DeclarativeBase):  #мета класс


class Category(Base):
    __tablename__ = 'category'

    id = Column(INT)






