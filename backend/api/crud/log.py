"""
CRUD for logs
"""
import datetime
import psycopg2

def Log(db_session, log):
    cur = db_session.cursor()

    cur.execute('INSERT INTO Tlog (date, log) VALUES (%s, %s)', (f"{datetime.datetime.now().strftime("%x %X")}", f"{log}"))


