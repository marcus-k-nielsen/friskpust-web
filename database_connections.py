import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

def database_connect():
    con = psycopg2.connect(
        os.getenv("DATABASE_CON_STRING"))
    cur = con.cursor()
    return con, cur

def database_close_connection(con, cur):
    cur.close()
    con.close()