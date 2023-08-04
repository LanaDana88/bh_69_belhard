from datetime import datetime
from typing import Any

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    ForeignKey,
    TIMESTAMP,
    TEXT,
    create_engine,
    CheckConstraint,
    select,
    update,
    delete,
    and_,
    any_,
    all_,
    or_
)

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, declared_attr, Session
from sqlalchemy.sql.functions import count
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from pydantic import BaseModel, PositiveInt, Field, PostgresDsn, ConfigDict
from pydantic_settings import BaseSettings
from dotenv import load_dotenv



class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_engine(url='postgresql://kama:888_kama@127.0.0.1:5432/lana_dana')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class Category(Base):
    #__tablename__ = 'category'# делаем генератор, для заголовков по генерации ариьутов (у нас на основании имене класаа, прпишем в Base model
    ___table_args__ = (
        CheckConstraint('char_length(name) >= 4')
    )

    #id = Column(INT, primary_key=True) #повторяющийся код, удаляем и добавляем в базовую модель для наследовая
    name = Column(VARCHAR(64), unique=True, nullable=False)

    product = relationship(argument='product', back_populates='category')


class Product(Base):
    #__tablename__ = 'product'
    #id = Column(INT, primary_key=True)

    title = Column(VARCHAR(24), unique=True, nullable=False)
    description = Column(VARCHAR(140),  nullable=False)
    category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)

    category = relationship(argument='category', back_populates='product')


# print(Base.metadata.create_all(bind=Base.engine))
#print(Base.metadata.tables)

with Base.session() as session: # type: Session
    category1 = Category(name='Apple Jus')
    category2 = Category(name='Latte')
    session.add_all((category1, category2))

    session.commit()
    session.refresh(category1)
    session.refresh(category2)
    print(category1.id, category2.id)

with Base.session() as session:
    category1 = session.get(Category, 6)
    print(category1.name)
