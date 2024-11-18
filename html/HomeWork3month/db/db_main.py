import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3.db')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_collection_products)
    cursor.execute(queries.CREATE_TABLE_product_details)
    db.commit()

async def sql_insert_store_to_collection_products(productid, collection):
    cursor.execute(
        queries.INSERT_collection_product,
        (productid, collection)
    )
    db.commit()

async def sql_insert_store_to_product_details(productid, category, info_product):
    cursor.execute(
        queries.INSERT_product_details,
        (productid, category, info_product)
    )
    db.commit()
