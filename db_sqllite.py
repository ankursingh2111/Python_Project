import sqlite3

def create_table():
    connect=sqlite3.connect("lite.db")
    conn=connect.cursor()
    conn.execute("CREATE TABLE STORE (ITEM TEXT, QUANTITY INTEGER, PRICE REAL)")
    connect.commit()
    connect.close()

def insert_table(item, quantity, price):
    connect=sqlite3.connect("lite.db")
    conn=connect.cursor()
    conn.execute("INSERT INTO STORE VALUES (?,?,?)",(item, quantity, price))
    connect.commit()
    connect.close()

def select_table():
    connect=sqlite3.connect("lite.db")
    conn=connect.cursor()
    conn.execute("SELECT * FROM STORE")
    rows=conn.fetchall()
    connect.close()
    return rows

def update_table(item, quantity, price):
    connect=sqlite3.connect("lite.db")
    conn=connect.cursor()
    conn.execute("UPDATE STORE SET QUANTITY=?, PRICE=? WHERE ITEM=?",(quantity, price, item))
    connect.commit()
    connect.close()

def delete_table(item):
    connect=sqlite3.connect("lite.db")
    conn=connect.cursor()
    conn.execute("DELETE FROM STORE WHERE ITEM=?",(item,))
    connect.commit()
    connect.close()

#insert_table("Wine Glass", 10, 11.5)
#insert_table("Coffee Cup", 12, 15.5)
#insert_table("Water_Glass", 20, 10.5)
print(select_table())
delete_table("Wine Glass")
print(select_table())
update_table("Water_Glass", 15, 14)
print(select_table())
