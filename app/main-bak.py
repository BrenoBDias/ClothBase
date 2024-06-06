import psycopg2

print("Hello, World!")
connected = False
while not connected:
    try:
        conn = psycopg2.connect(
            host="postgres", database="clothbase", user="breno", password="breno"
        )


        cur = conn.cursor()
        cur.execute("SELECT * FROM custumer")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
        connected = True
    except:
        print("connection failled")





