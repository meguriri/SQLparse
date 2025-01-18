from generate.generate import generateSQL

def testSQL(row_sql,conn):
    sql = generateSQL(row_sql,conn)
    data = conn.execSQL(sql)
    return data