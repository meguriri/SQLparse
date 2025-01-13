from db import Conn
from query import q0
from config import opt

conn = Conn(opt.username,opt.password,opt.host,opt.port,opt.database)
data = conn.execSQL(q0)

print(data)