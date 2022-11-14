import sqlite3

conn = sqlite3.connect('PTA_local_stock.db')
print ("Opened database successfully")

conn.execute('''INSERT INTO STOCK (ID,NAME,COLOUR,QTY,PRICE) VALUES (0001, 'Cap Screw','Silver', 100,  12.00 )''')
print("YES1")

"""
conn.execute("INSERT INTO STOCK (ID,NAME,COLOUR,QTY,PRICE) \
      VALUES (0002, 'Washer','Silver', 100,  2.00 )")
print("YES2")

conn.execute("INSERT INTO STOCK (ID,NAME,COLOUR,QTY,PRICE) \
      VALUES (0003, 'T-Bolt','Silver', 50,  22.00 )")
print("YES3")

conn.execute("INSERT INTO STOCK (ID,NAME,COLOUR,QTY,PRICE) \
      VALUES (0004, 'Flange Nut','Silver', 200,  10.00 )")
print("YES4")

conn.execute("INSERT INTO STOCK (ID,NAME,COLOUR,QTY,PRICE) \
      VALUES (0005, 'PDU','BLACK', 10,  800.00 )")
print("YES5")
conn.execute("INSERT INTO STOCK (ID,NAME,COLOUR,QTY,PRICE) \
      VALUES (0006, 'LED','RED', 100,  1.00 )")
print("YES6")
conn.execute("INSERT INTO STOCK (ID,NAME,COLOUR,QTY,PRICE) \
      VALUES (0007, 'battery','BLACK', 10,  1800.00 )")
print("YES7")
"""

#conn.commit()
print ("Records created successfully")
conn.close()