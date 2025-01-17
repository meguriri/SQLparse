from generate.generate import generateSQL

def testSQL(g,row_sql,conn):
    sql = generateSQL(g,row_sql,conn)
    data = conn.execSQL(sql)
    return data