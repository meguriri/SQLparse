from sql import generate_sql,colum_q,getTokens,getQueryTabName,getConditions,getQueryColName, getColumnDict,getNeedtables,getAllSubTables,getInvertedIndex
from .graph import Graph

def generateSQL(row_sql,conn):
    statement = getTokens(row_sql)# 获取sql的token
    columns=getQueryColName(statement.tokens)# 获取查询的列
    table_name=getQueryTabName(statement.tokens)# 获取大表的名
    conditions=getConditions(statement.tokens)# 获取查询条件
    index = getInvertedIndex(table_name[0],conn)# 获取倒排索引
    g = Graph(index) # 建图
    tables = []
    new_conditions = []
    new_columns = []
    joins = ""
    need_columns = set() # 需要的列
    if len(columns)>0: # 查询的列不是'*'
        for column in columns: #根据查询的列获取子表
            if isinstance(column,str): #是列的情况
                new_columns.append('"'+column+'"')
                need_columns.add(column)
            else: #是函数的情况
                new_columns.append(f"{column['func']}(\"{column['param']}\")")
                need_columns.add(column['param'])
            data = conn.execSQL(colum_q.format( # 获取需要的子表
                colum_name = column if isinstance(column,str) else column['param'],  
                raw_table_name =  ",".join(table_name),
            ))
            tables.extend(data['table_names'].tolist()[0])
        for con in conditions: #根据查询条件获取子表
            new_conditions.append(' '+con['column']+con['predicate']+con['value'])
            need_columns.add(con['column'])
            data = conn.execSQL(colum_q.format( # 获取需要的子表
                colum_name = con['column'],
                raw_table_name =  ",".join(table_name),
            ))
            tables.extend(data['table_names'].tolist()[0])
        tables = set(tables) # 需要的子表转换为set，去重
        colsDict = getColumnDict(tables,conn) # 获取每个子表的所有列
        tables=getNeedtables(need_columns,colsDict) # 筛选得到最终需要的表
    else: # 查询是'*'的情况
        tables = getAllSubTables(table_name[0],conn) #获取大表的全部子表
        for con in conditions: #生成新的查询条件
            new_conditions.append(' '+con['column']+con['predicate']+con['value'])
    first_table = "" # 第一个表
    new_conditions=' AND'.join(new_conditions) #新的查询条件补充AND
    if len(tables) > 1: #需要的表数量大于1，需要join
        path=g.find_join_path(tables) # 获得join的路径
        first_table = path[0][0]
        for p in path:
            joins += f"JOIN {p[1]} ON {p[0]}.{p[2]}={p[1]}.{p[2]} " # 生成JOIN字符串
    else:
        first_table = next(iter(tables))
    newSQL = generate_sql.format(
        columns = ','.join(new_columns) if len(columns)!=0 else '*',
        tables = first_table,
        joins = joins,
        where = 'WHERE' if new_conditions!='' else '', #判断是否需要WHERE
        conditions = new_conditions, 
    )
    print(newSQL)
    return newSQL