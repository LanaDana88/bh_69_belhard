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
        date_created timestamp default (now()), 
        category_id integer not null, 
        foreign key (category_id) references category(id) on delete cascade
    )
''')

conn.commit()

cur.execute('''
    create  index if not exists category_id_index on product (category_id);
''')

conn.commit()



