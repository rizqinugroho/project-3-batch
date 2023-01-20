import psycopg2
import csv
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")

#menggunakan kursor
cur = conn.cursor()
cur.execute('Select * from public.employee')

#menampilkan hasil
one = cur.fetchone()
all = cur.fetchall()
print(one)

#create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id integer PRIMARY KEY,
    email text,
    name text,
    address text
)
""")

##Sebelum di commit table belum akan terbuat, maka lakukan commit
conn.commit()

with open('/Users/nugrohom/Documents/project-3/data/users.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO users VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
            row
        )
conn.commit()
##inserting data
#cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (10, 'hello@dataquest.io', 'Some Name', '123 Fake St.'))
#conn.commit()