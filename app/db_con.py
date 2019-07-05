import psycopg2
import os

# url = "dbname='saf_api'
#  host='localhost' port='5432' user='postgres' password='postgres'"

db_url = os.getenv('DATABASE_URL')


def connection():
    conn = psycopg2.connect(db_url)
    conn.autocommit = True
    return conn


def create_tables():
    curr = connection().cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)


def destroy_tables():
    pass


def tables():
    db1 = """CREATE TABLE IF NOT EXISTS payments (
        BillRefNumber varchar PRIMARY KEY NOT NULL,
        ShortCode character varying(1000) NOT NULL,
        Amount numeric NOT NULL,
        Msisdn numeric NOT NULL,
        CommandID character varying(1000) NOT NULL
        );"""

    queries = [db1]
    return queries