import psycopg2
conn = psycopg2.connect("host=1ae9a6b242c4 dbname=postgres user=airflow")
cur = conn.cursor()
with open('/data/order_detail.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'order_detail', sep=',')
conn.commit()