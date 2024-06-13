import psycopg2

def Connect():
    connected = False
    tries = 0
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
            connected = True
            return conn
        except:
            if tries % 20 == 0:
                print("Connection Failed")
            tries +=1
