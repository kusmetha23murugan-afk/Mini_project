import sqlite3
import calc


conn = sqlite3.connect("EBILL.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EBILL1")
cursor.execute("CREATE TABLE EBILL1 (con_id INTEGER PRIMARY KEY, name VARCHAR(100), units INTEGER,days INTEGER, amount FLOAT);")

id_list=[]
a = True
while a:
    conid = int(input("Enter Consumer ID: ").strip())
    if conid not in id_list:
        name = input("Enter consumer Name: ").strip()
        units = int(input("Enter Consumed units: "))
        days=int(input("Enter the no. of days delayed: "))
        amount = calc.fine(calc.calc_amount(units),days)

        op = int(input("Enter option 1.Add consumer 2.exit: "))
        cursor.execute("INSERT INTO EBILL1 (con_id, name, units,days, amount) VALUES (?, ?, ?, ?, ?)", (conid, name, units,days, amount))
        conn.commit()
        id_list.append(conid)
        if op == 2:
            a = False
    else:
        print("Same consumer id is enterded. Try another one.")

cursor.execute("SELECT * FROM EBILL1")
rows = cursor.fetchall()
for row in rows:
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Consumer ID  : {row[0]}")
        print(f"Consumer Name: {row[1]}")
        print(f"Units        : {row[2]}")
        print(f"Days delayed : {row[3]}")
        print(f"Amount       :{row[4]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~")

conn.close()
