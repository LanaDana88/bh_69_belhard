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



class Settings(BaseModel):
    engine = create_engine(url='postgresql://kama:888_kama@127.0.0.1:5432/lana_dana')
    session = sessionmaker(bind=engine)

class Categori(Base):
    __tablename__ = 'Categories'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), unique=True, nullable=False)

    products = relationship(argument='Product', back_populates='Categori')
class Product(Base):
    __tablename__ = 'Products'

    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(24), unique=True, nullable=False)
    description = Column(VARCHAR(140),  nullable=False)
    category_id = Column(INT, ForeignKey(column='Categori.id', ondelete='RESTRICT'), nullable=False)

    catigories = relationship(argument='Categori', back_populates='Product')

print(Base.metadata.create_all(bind=Base.engine))
#
# alembic==1.11.1
# alembic==1.11.1
# alembic==1.11.1
# annotated-types==0.5.0
# anyio==3.7.1
# certifi==2023.7.22
# dnspython==2.4.0
# email-validator==2.0.0.post2
# emailvalidator==0.3
# greenlet==2.0.2
# h11==0.14.0
# httpcore==0.17.3
# idna==3.4
# Mako==1.2.4
# MarkupSafe==2.1.3
# psycopg2==2.9.6
# psycopg2-binary==2.9.6
# pydantic==2.0.3
# pydantic-settings==2.0.2
# pydantic_core==2.3.0
# python-dotenv==1.0.0
# PyYAML==6.0.1
# sniffio==1.3.0
# SQLAlchemy==2.0.19
# typing_extensions==4.7.1
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69>


#
# C:\Users\Admin\PycharmProjects\python_bh_69\venv\Scripts\python.exe C:\Users\Admin\PycharmProjects\python_bh_69\lesson_13_sdb.py
# Traceback (most recent call last):
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\lesson_13_sdb.py", line 33, in <module>
#     class Settings(BaseModel):
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\pydantic\_internal\_model_construction.py", line 97, in __new__
#     private_attributes = inspect_namespace(
#                          ^^^^^^^^^^^^^^^^^^
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\pydantic\_internal\_model_construction.py", line 339, in inspect_namespace
#     raise PydanticUserError(
# pydantic.errors.PydanticUserError: A non-annotated attribute was detected: `engine = Engine(postgresql://kama:***@127.0.0.1:5432/lana_dana)`. All model fields require a type annotation; if `engine` is not meant to be a field, you may be able to resolve this error by annotating it as a `ClassVar` or updating `model_config['ignored_types']`.
#
# For further information visit https://errors.pydantic.dev/2.0.3/u/model-field-missing-annotation
#
# Process finished with exit code 1

