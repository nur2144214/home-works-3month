# SQL-запросы для создания таблиц и вставки данных

CREATE_TABLE_product_details = """
CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    category TEXT,
    info_product TEXT
)
"""

INSERT_product_details = """
INSERT INTO product_details (productid, category, info_product) VALUES (?, ?, ?)
"""

CREATE_TABLE_collection_products = """
CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    collection TEXT
)
"""

INSERT_collection_product = """
INSERT INTO collection_products (productid, collection) VALUES (?, ?)
"""
