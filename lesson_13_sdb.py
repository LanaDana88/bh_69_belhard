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

    def __repr__(self):
        return self.name

class Product(Base):
    #__tablename__ = 'product'
    #id = Column(INT, primary_key=True)

    title = Column(VARCHAR(24), unique=True, nullable=False)
    description = Column(VARCHAR(140),  nullable=False)
    category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)

    category = relationship(argument='category', back_populates='product')

    def __repr__(self):
        return self.title

# print(Base.metadata.create_all(bind=Base.engine))
# print(Base.metadata.tables)

#FacadeDict({'category': Table('category', MetaData(), Column('name', VARCHAR(length=64), table=<category>, nullable=False), Column('id', INTEGER(), table=<category>, primary_key=True, nullable=False), schema=None), 'product': Table('product', MetaData(), Column('title', VARCHAR(length=24), table=<product>, nullable=False), Column('description', VARCHAR(length=140), table=<product>, nullable=False), Column('category_id', INTEGER(), ForeignKey('category.id'), table=<product>, nullable=False), Column('id', INTEGER(), table=<product>, primary_key=True, nullable=False), schema=None)})

# Process finished with exit code 0
# with Base.session() as session: # type: Session
#     category1 = Category(name='Apple Jus')
#     category2 = Category(name='Latte')
#     session.add_all((category1, category2))
#
#     session.commit()
#     session.refresh(category1)
#     session.refresh(category2)
#     print(category1.id, category2.id)

# with Base.session() as session:
#     category1 = session.get(Category, 6)
#     print(category1.name)
#
# with Base.session() as session:
#     objects = session.scalars(
#         select(Category)
#         .order_by(Category.name.desc())
#         .filter(Category.id.in_([6.7]))
#         .limit(2)
#         .offset(3)
#     )

# with Category.session() as session:
#     session.execute(
#         update(Category)
#         .filter_by(name='Молоко')
#         .values(name='Latte')
#     )
#     session.commit()
#
#
# with Category.session() as session:
#     session.execute(
#         delete(Category)
#         .filter(or_(Category.id > 10, Category.id < 5))
#     )
#     session.commit()

#
# with Category.session() as session:
#     c = session.scalar(select(count(Category.id)))
#     print(c)

# Traceback (most recent call last):
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\lesson_13_sdb.py", line 74, in <module>
#     category1 = Category(name='Apple Jus')
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<string>", line 4, in __init__
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\state.py", line 561, in _initialize_instance
#     manager.dispatch.init(self, args, kwargs)
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\event\attr.py", line 487, in __call__
#     fn(*args, **kw)
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4390, in _event_on_init
#     instrumenting_mapper._check_configure()
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2386, in _check_configure
#     _configure_registries({self.registry}, cascade=True)
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4198, in _configure_registries
#     _do_configure_registries(registries, cascade)
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4239, in _do_configure_registries
#     mapper._post_configure_properties()
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2403, in _post_configure_properties
#     prop.init()
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\interfaces.py", line 578, in init
#     self.do_init()
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\relationships.py", line 1633, in do_init
#     self._setup_entity()
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\sqlalchemy\orm\relationships.py", line 1870, in _setup_entity
#     raise sa_exc.ArgumentError(
# sqlalchemy.exc.ArgumentError: relationship 'product' expects a class or a mapper argument (received: <class 'sqlalchemy.sql.schema.Table'>)
#
# Process finished with exit code 1



#
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69> alembic uprade head
# usage: alembic [-h] [--version] [-c CONFIG] [-n NAME] [-x X] [--raiseerr] [-q]
#                {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates,merge,rev
# ision,show,stamp,upgrade}
#                ...
# alembic: error: argument {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates
# ,merge,revision,show,stamp,upgrade}: invalid choice: 'uprade' (choose from 'branches', 'check', 'current', 'down
# grade', 'edit', 'ensure_version', 'heads', 'history', 'init', 'list_templates', 'merge', 'revision', 'show', 'st
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69>  alembic uprade head
# usage: alembic [-h] [--version] [-c CONFIG] [-n NAME] [-x X] [--raiseerr] [-q]
#                {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates,merge,rev
# ision,show,stamp,upgrade}
#                ...
# alembic: error: argument {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates
# ,merge,revision,show,stamp,upgrade}: invalid choice: 'uprade' (choose from 'branches', 'check', 'current', 'down
# grade', 'edit', 'ensure_version', 'heads', 'history', 'init', 'list_templates', 'merge', 'revision', 'show', 'st
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69>  alembic uprade head
# usage: alembic [-h] [--version] [-c CONFIG] [-n NAME] [-x X] [--raiseerr] [-q]
#                {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates,merge,rev
# ision,show,stamp,upgrade}
#                ...
# alembic: error: argument {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates
# ,merge,revision,show,stamp,upgrade}: invalid choice: 'uprade' (choose from 'branches', 'check', 'current', 'down
# grade', 'edit', 'ensure_version', 'heads', 'history', 'init', 'list_templates', 'merge', 'revision', 'show', 'st
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69>  alembic uprade head
# usage: alembic [-h] [--version] [-c CONFIG] [-n NAME] [-x X] [--raiseerr] [-q]
#                {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates,merge,rev
# ision,show,stamp,upgrade}
#                ...
# alembic: error: argument {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates
# ,merge,revision,show,stamp,upgrade}: invalid choice: 'uprade' (choose from 'branches', 'check', 'current', 'down
# grade', 'edit', 'ensure_version', 'heads', 'history', 'init', 'list_templates', 'merge', 'revision', 'show', 'st
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69>  alembic uprade head
# usage: alembic [-h] [--version] [-c CONFIG] [-n NAME] [-x X] [--raiseerr] [-q]
#                {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates,merge,rev
# ision,show,stamp,upgrade}
#                ...
# alembic: error: argument {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates
# ,merge,revision,show,stamp,upgrade}: invalid choice: 'uprade' (choose from 'branches', 'check', 'current', 'down
# grade', 'edit', 'ensure_version', 'heads', 'history', 'init', 'list_templates', 'merge', 'revision', 'show', 'st
# amp', 'upgrade')
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69> alembic downgrade -1
# FacadeDict({'category': Table('category', MetaData(), Column('id', INTEGER(), table=<category>, primary_key=True
# , nullable=False), Column('name', VARCHAR(length=64), table=<category>, nullable=False), schema=None), 'product'
# : Table('product', MetaData(), Column('id', INTEGER(), table=<product>, primary_key=True, nullable=False), Colum
# n('title', VARCHAR(length=24), table=<product>, nullable=False), Column('description', VARCHAR(length=140), tabl
# e=<product>, nullable=False), Column('category_id', INTEGER(), ForeignKey('category.id'), table=<product>, nulla
# ble=False), schema=None)})
# Traceback (most recent call last):
#   File "<frozen runpy>", line 198, in _run_module_as_main
#   File "<frozen runpy>", line 88, in _run_code
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Scripts\alembic.exe\__main__.py", line 7, in <module>
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\alembic\config.py", line 632, in main
#     CommandLine(prog=prog).main(argv=argv)
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\alembic\config.py", line 626, in main
#     self.run_cmd(cfg, options)
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\alembic\config.py", line 603, in run_
# cmd
#     fn(
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\alembic\command.py", line 431, in dow
# ngrade
#     script.run_env()
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\alembic\script\base.py", line 582, in
#  run_env
#     util.load_python_file(self.dir, "env.py")
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\alembic\util\pyfiles.py", line 94, in
#  load_python_file
#     module = load_module_py(module_id, path)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\venv\Lib\site-packages\alembic\util\pyfiles.py", line 110, i
# n load_module_py
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
#   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\alembic\env.py", line 81, in <module>
#     run_migrations_online()
#   File "C:\Users\Admin\PycharmProjects\python_bh_69\alembic\env.py", line 62, in run_migrations_online
#     configuration['sqlalchemy.url'] = Base.engine.url
#     ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
# TypeError: 'tuple' object does not support item assignment
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69> alembic revision
# Generating C:\Users\Admin\PycharmProjects\python_bh_69\alembic\versions\e96192a0b3ef_.py ...  done
# (venv) PS C:\Users\Admin\PycharmProjects\python_bh_69>
