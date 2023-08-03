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
    engine = create_engine(url='postgresql://kama:888_kama@127.0.0.1:5432/lana_dana')
    session = sessionmaker(bind=engine)


class Category(Base):
    __tablename__ = 'category'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), unique=True, nullable=False)

    product = relationship(argument='Product', back_populates='Category')


class Product(Base):
    __tablename__ = 'Products'

    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(24), unique=True, nullable=False)
    description = Column(VARCHAR(140),  nullable=False)
    category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)

    category = relationship(argument='Category', back_populates='Product')


print(Base.metadata.create_all(bind=Base.engine))
