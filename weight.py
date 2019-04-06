import argparse
import datetime
import sqlite3

import pandas

parser = argparse.ArgumentParser(description='Weight now!')
parser.add_argument("weight", type=float)
try:
    weight = parser.parse_args().weight
except:
    weight=None
with sqlite3.connect("C:\\Users\jembi\PycharmProjects\weight\weight") as conn:
    cursor = conn.cursor()
    if weight:
        cursor.execute("CREATE TABLE IF NOT EXISTS weight (date DATE PRIMARY KEY, weight REAL)")
        now = datetime.datetime.now()
        cursor.execute(f"INSERT INTO weight (date, weight) VALUES (?,?)", (now, weight))
    print(pandas.read_sql_query("SELECT * FROM weight", con=conn))