from db import Conn
from query import q0,table_q,colum_q
from config import opt
from sql import getTokens,getQueryTabName,getConditions,getQueryColName

def generateSQL(row_sql,conn):
    statement = getTokens(row_sql)
    colums=getQueryColName(statement.tokens)
    table_name=getQueryTabName(statement.tokens)
    conditions=getConditions(statement.tokens)
    # print(colums)
    # print(table_name)
    # print(conditions)
    tables = []
    for colum in colums:
        data = conn.execSQL(colum_q.format(
            colum_name = colums[0],
            raw_table_name =  ",".join(table_name),
        ))
        tables.extend(data['table_names'].tolist()[0])

    tables = list(set(tables))
    print(tables)
    # 查询join关系

    # 生成新的SQL
    newSQL = ""
    return newSQL
    

if __name__ == '__main__':
    conn = Conn(opt.username,opt.password,opt.host,opt.port,opt.database)
    # data = conn.execSQL(colum_q.format(colum_name='uid'))
    r_sql = "SELECT userid FROM t1 WHERE age=22;"
    generateSQL(r_sql,conn)