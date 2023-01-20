import pandas as pd
from sqlalchemy import create_engine
import psycopg2

df = pd.read_csv('/Users/nugrohom/Documents/project-3/data/users_w_postal_code.csv', sep=',')


##> {dialect}+{driver}://{user}:{password}@{host}:{port}/{database}
#host=localhost dbname=postgres user=postgres password=1234

engine = create_engine('postgresql://postgres:1234@127.0.0.1:5432/postgres')
df.to_sql("from_file_table", engine)