from db import Conn

conn = Conn("postgres","xyy001019",
  "localhost","55435","postgres")

data = conn.execSQL("select column_name\
  from information_schema.columns where\
  table_schema='public' and table_name \
  = 'employee'")

print(data)

