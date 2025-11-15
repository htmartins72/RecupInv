import time
import sqlite3
start_time = time.perf_counter_ns()
try:
    with sqlite3.connect('20251115142128_ekanbanBD.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT id,QT_Inventariada FROM InventoryDetails where picado = 1")
        rows = cur.fetchall()
        for row in rows:
            print(row)
except sqlite3.Error as e:
    print(e)
end_time = time.perf_counter_ns()
elapsed_time = (end_time-start_time)/1000000
print(f'{elapsed_time} Seconds')

import pandas as pd
import sqlite3
start_time = time.perf_counter_ns()
# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("20251115142128_ekanbanBD.db")
df = pd.read_sql_query("SELECT id,QT_Inventariada FROM InventoryDetails where picado = 1", con)

# Verify that result of SQL query is stored in the dataframe
print(df.all)

con.close()
end_time = time.perf_counter_ns()
elapsed_time = (end_time-start_time) /1000000
print(f'{elapsed_time}')