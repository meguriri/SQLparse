from db import Conn
from sql import q1,q2,q3,getInvertedIndex
from config import opt
from generate import Graph,generateSQL
from test import testSQL

if __name__ == '__main__':
    conn = Conn(opt.username,opt.password,opt.host,opt.port,opt.database)
    index = getInvertedIndex("t1",conn)
    g = Graph(index)
    # generateSQL(g,q1,conn)
    test_data = testSQL(g,q2,conn)
    print(test_data)