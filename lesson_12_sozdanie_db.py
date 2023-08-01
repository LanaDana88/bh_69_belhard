from sqlite3 import connect

conn = connect('db.sqlite3')
cur = conn.cursor()

from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor

import psycopg2


with connect('postgresql://kama:888_kama@127.0.0.1:5432/lana_dana') as conn:
    with conn.cursor() as cur:
        cur.execute('''
        create table if not exists statuses(
        id INTEGER primary key,
        name Varchar(10) unique not null
        );
        
        create table if not exists users(
        id INTEGER Primary key, 
        name varchar(24) not null, 
        email varchar(24) unique not null
        );
        
        create table if not exists categories(
        id INTEGER Primary key, 
        name VARCHAR(24) unique not null
        );
        
        create table if not exists products(
        id INTEGER Primary key, 
        title VARCHAR(36) not null, 
        description VARCHAR(140), 
        category_id integer not null,
        foreign key (category_id) references categories(id) on delete cascade
        );      
        
        create table if not exists orders(
        id INTEGER Primary key,
        user_id INTEGER not null,
        foreign key (user_id) references users(id) on delete cascade, 
        status_id INTEGER not null, 
        foreign key (status_id) references statuses(id) on delete cascade 
        );
        
        create table if not exists order_items(
        id INTEGER Primary key, 
        tutle VARCHAR(36) not null, 
        description VARCHAR(140), 
        category_id INTEGER not null, 
        foreign key (category_id) references categories(id) on delete cascade 
        );    
''');
        conn.commit()

