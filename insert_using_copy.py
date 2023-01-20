import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")

cur = conn.cursor()


#create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    email text,
    name text,
    phone text,
    postal_code text
)
""")
conn.commit()

with open('/Users/nugrohom/Documents/project-3/data/users_w_postal_code.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'users', sep=',', columns=('email', 'name','phone', 'postal_code'))

conn.commit()

