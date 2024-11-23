import sqlite3
from db import queries
import aiosqlite

db = sqlite3.connect('store.sqlite3.db')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')
        cursor.execute(queries.CREATE_TABLE_product_details)
        cursor.execute(queries.CREATE_TABLE_collection_products)


async def sql_insert_store_to_product_details(productid, category, infoproduct):
    cursor.execute(
        queries.INSERT_product_details,
        (productid, category, infoproduct)
    )
    db.commit()

async def sql_insert_store_to_collection_products(productid, collection):
    cursor.execute(
        queries.INSERT_collection_products,
        (productid, collection)
    )
    db.commit()

def get_db_connection():
    connect = sqlite3.connect('db/store.sqlite3.db')
    connect.row_factory = sqlite3.Row
    return connect

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
        SELECT * FROM collection_products s
        INNER JOIN product_details sd ON s.productid = sd.productid
        """).fetchall()
    conn.close()
    return products


def delete_product(product_id):
    connect = get_db_connection()
    connect.execute('DELETE FROM STORE WHERE product_id = ?', (product_id,))
    connect.commit()
    connect.close()