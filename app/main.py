import psycopg2

print("Hello, world")

connected = False
while not connected:
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="clothbase",
            user="breno",
            password="breno")
        connected = True
    except: print(ConnectionRefusedError)

cur = conn.cursor()

cur.execute("SELECT * FROM custumer")

rows = cur.fetchall()

for row in rows:
    print(row)
    
cur.close()
conn.close()


# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))



# loop = True
# while loop:
#     if input("want to print some shit?").lower() == "y":
#         cur.execute("SELECT * FROM test;")
#         cur.fetchone()(1, 100, "abc'def")
#     else:
#         loop = False

# conn.commit()

# cur.close()
# conn.close()