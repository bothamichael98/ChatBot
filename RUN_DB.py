import sqlite3

conn = sqlite3.connect('PTA_local_stock.db')
print ("Open database")

conn.execute('''CREATE TABLE STOCK(ID INT PRIMARY KEY     NOT NULL,
                      NAME           TEXT    NOT NULL,
                      COLOUR         TEXT    NOT NULL,
                      QTY            INT     NOT NULL,
                      PRICE         REAL);''')

print ("Tabel created")

conn.close()