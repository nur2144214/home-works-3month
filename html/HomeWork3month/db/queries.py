# queries.py
CREATE_TABLE_product_details = """
CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    category TEXT,
    info_product TEXT


INSERT_product_details = """
    INSERT INTO products_details (productid, collection) VALUES (?, ?)
"""

CREATE_TABLE_collection_products = """
CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    colection TEXT
)
"""

INSERT_collection_product = """
    INSERT INTO collection (productid)
    VALUES (?, ?)
"""