import os
import sqlite3
from time import sleep

conn = sqlite3.connect("example.db")

cur = conn.cursor()
"""
cur.execute(''' CREATE TABLE person (
                fname text,
                age integer
            )''')
"""
def createTable():
    out = False
    while not out:
        tableName = input("Create a table:\n>> ").replace(" ","")
        if checkTable(tableName) == True:
            cur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName} (
                            term text, definition text )""")
            out = True
            break
        else:
            print("Table already exists.Please create another one.")
            continue

# Check if table already exists
def checkTable(table):
    listTables = cur.execute(f"SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{table}';").fetchall()
    if listTables == []:
        # Table can be created
        return True
    else:
        return False

# List all the tables in the database
def getAllTables():
    cnt = 1
    listTables = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';").fetchall()
    if listTables == []:
        print("No Table available")
    else:
        for i in listTables:
            print(f"Table {cnt}: {i[0]}")
            cnt += 1

def dropTable(table):
    cur.execute(f"DROP TABLE IF EXISTS {table}")

def insertTD():
    table = input("Input name of the table:\n>> ")
    with conn:
        cur.execute(f"INSERT INTO {table} VALUES ('Carry Flag', 'Indicates an overflow condition for arithmetic operations') ")

#dropTable("try")
#createTable()
#insertTD()
if __name__ == '__main__':
    print("This the main")
    getAllTables()
    sleep(0.5)


# Check if table exists
'''
theTable = 'person'
print(f'Check if {theTable} TABLE exists in the database: ')
listOfTables = cur.execute(f""" SELECT name FROM sqlite_master
                                WHERE type = 'table' AND name = {theTable};
""").fetchall()

if listOfTables == []:
    print("Table not found..")
else:
    print("Table found..")
'''

# Checks all tables
'''
lastList = []
cnt = 1
listTables = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'; ").fetchall()
print(listTables)

for i in (list(listTables[cnt - 1])):
    print(f"Table {cnt}: {i}")
    cnt += 1 
'''


#with conn:
    #cur.execute("INSERT INTO try VALUES ('Strings', 'Words')")
thisPerson = "try"
#cur.execute(f"SELECT * FROM {thisPerson} WHERE term = 'Strings'")

# This is to get all the values on the Table
#cur.execute(f"SELECT * FROM {thisPerson}")
#print(cur.fetchall())
#cur.execute(f"SELECT * FROM trying")
#print(cur.fetchall())


conn.commit()
conn.close()


