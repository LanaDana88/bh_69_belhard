from sqlite3 import connect

conn = connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
    create table if not exists category (
        id INTEGER primary key autoincrement, 
        name Varchar (32) not null unique        
    );
''')
conn.commit()


cur.execute('''
    create table if not exists product (
        id INTEGER primary key autoincrement, 
        name varchar (128) not null, 
        descr varchar (4096), 
        price decimal (8, 2) not null check (price > 0), 
        is_published boolean default (true), 
        category_id integer not null, 
        foreign key (category_id) references category(id) on delete cascade
    )
''')

conn.commit()

cur.execute('''
    create  index if not exists category_id_index on product (category_id);
''')
cur.execute('''
    create  index if not exists is_published_index on product (is_published);
''')
conn.commit()


# zapolnyem tablicu

# cur.execute('''
#     insert into category (name) values (?);
#
# ''',  ("Coffe", ))
# conn.commit()
#
# cur.execute('''
#     select * from category where id >= 1 ;
# ''')
# print(cur.fetchall())
# conn.commit()

# cur.execute('''
#     update category set name = ? where id = 1 ;
# ''', ('Кофе', ))
# conn.commit()

# cur.execute('''
#     DELETE from category where name like '%a' ;
# ''')
# conn.commit()
#

from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor


# products = [
#     ('Cappuccino', 5.5, 1),
#     ('Latte', 6.5, 1),
#     ('Mokko', 4.5, 1),
#     ('Americano', 3.55, 1),
#     ('Shokko', 4.75, 1),
# ]
#
# cur.executemany('''
#     INSERT INTO product (name, price, category_id) VALUES (?, ?, ?);
# ''', products)
#
# conn.commit()
#
# cur.execute('''
#     insert into category (name) values (?);
# ''', ('Tea', ))
# conn.commit()

cur.execute('''
    select t.name, p.name,  p.price 
    from category t
    left join product p on t.id = p.category_id
''')

print(cur.fetchall())

cur.execute('''
    select t.name, p.name,  p.price 
    from category t
    right join product p on t.id = p.category_id
''')

print(cur.fetchall())
