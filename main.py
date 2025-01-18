from db import Conn
from sql import q1,q2,q3,q4
from config import opt
from test import testSQL

if __name__ == '__main__':
    conn = Conn(opt.username,opt.password,opt.host,opt.port,opt.database)
    test_data = testSQL(q1,conn)
    print(test_data)