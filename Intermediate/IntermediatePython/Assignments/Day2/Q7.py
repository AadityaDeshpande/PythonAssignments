import sqlite3

conn = sqlite3.connect('test')

cursor = conn.cursor()

cursor.execute("Drop TABLE users")

cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,phone TEXT, email TEXT unique, password TEXT)")

values=(1,'Ravi Verma','9923849335','ravi_verma@gmail.com','tough@password!!')

cursor.execute("insert into users values (?,?,?,?,?)",values)

result = cursor.execute("select * from users")

print ("Result = ", list(result))

search = input("Enter a name to search: ")

search = search.rstrip()

result = list(cursor.execute("select * from users where name == ?",(search,)))

if len( result ) != 0:
    print ("Result = ", (result))
else:
    print("Record Not Found")

conn.commit()

conn.close()
