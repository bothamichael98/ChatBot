import os
import shutil
import sqlite3
import yaml
conn = sqlite3.connect('PTA_local_stock.db')
print ("Opened database successfully")

"""
conn.execute('''CREATE TABLE STOCK
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         COLOUR         TEXT    NOT NULL,
         QTY            INT     NOT NULL,
         PRICE         REAL);''')

         """


cursor = conn.execute("SELECT ID,NAME,COLOUR,QTY,PRICE from STOCK")


tmp_file_ID="catagory:\n- Stock\nconversations:\n"
tmp_file_Price="catagory:\n- Stock\nconversations:\n"

for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("COLOUR = ", row[2])
   print("QTY = ", row[3])
   print("PRICE = R", row[4])
   tmp_file_ID=tmp_file_ID+"- - Do you have a "+row[1]+"\n"+"  - Yes, We have " + str(row[3])+" "+row[1]+"s in stock\n"
   tmp_file_ID = tmp_file_ID + "- - What colour is the " + row[1] + "\n" + "  - The colour is " +row[2] + "\n"
   tmp_file_ID = tmp_file_ID + "- - What is the price of a " + row[1] + "\n" + "  - The price is R" +str(row[4]) + "0 each\n"
print ("Operation done successfully")


with open(r'C:\Users\Michael Botha\Desktop\TEMP_ID.txt','w')as file:
   file.write(tmp_file_ID)
#with open(r'C:\Users\Michael Botha\Desktop\TEMP_PRICE.txt', 'w') as file:
#   file.write(tmp_file_Price)
os.rename(r'C:\Users\Michael Botha\Desktop\TEMP_ID.txt',r'C:\Users\Michael Botha\Desktop\ID.yml')
shutil.copyfile(r'C:\Users\Michael Botha\Desktop\ID.yml',r'C:\Users\Michael Botha\PycharmProjects\TUTChatbot\venv\Lib\site-packages\chatterbot_corpus\data\english\ID.yml')
#os.remove(r'C:\Users\Michael Botha\Desktop\TEMP_ID.txt')
#os.remove(r'C:\Users\Michael Botha\Desktop\TEMPYML_ID.yml')

#os.rename(r'C:\Users\Michael Botha\Desktop\TEMP_PRICE.txt',r'C:\Users\Michael Botha\Desktop\PRICE.yml')
#shutil.copyfile(r'C:\Users\Michael Botha\Desktop\PRICE.yml',r'C:\Users\Michael Botha\PycharmProjects\TUTChatbot\venv\Lib\site-packages\chatterbot_corpus\data\english\PRICE.yml')
#os.remove(r'C:\Users\Michael Botha\Desktop\TEMP_PRICE.txt')
#os.remove(r'C:\Users\Michael Botha\Desktop\TEMPYML_PRICE.yml')
conn.close()