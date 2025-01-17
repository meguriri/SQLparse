from sql import generate_sql,colum_q,getTokens,getQueryTabName,getConditions,getQueryColName, getColumnDict,getNeedtables

def generateSQL(g,row_sql,conn):
    statement = getTokens(row_sql)
    columns=getQueryColName(statement.tokens)
    table_name=getQueryTabName(statement.tokens)
    conditions=getConditions(statement.tokens)
    tables = []
    new_conditions = []
    new_columns = []
    joins = ""
    need_columns = set()
    for column in columns:
        if isinstance(column,str):
            new_columns.append('"'+column+'"')
            need_columns.add(column)
        else:
            new_columns.append(f"{column['func']}(\"{column['param']}\")")
            need_columns.add(column['param'])
        data = conn.execSQL(colum_q.format(
            colum_name = column if isinstance(column,str) else column['param'],  
            raw_table_name =  ",".join(table_name),
        ))
        tables.extend(data['table_names'].tolist()[0])
    for con in conditions:
        new_conditions.append(' '+con['column']+con['predicate']+con['value'])
        need_columns.add(con['column'])
        data = conn.execSQL(colum_q.format(
            colum_name = con['column'],
            raw_table_name =  ",".join(table_name),
        ))
        tables.extend(data['table_names'].tolist()[0])
    tables = set(tables)
    colsDict = getColumnDict(tables,conn)
    tables=getNeedtables(need_columns,colsDict)
    first_table = ""
    new_conditions=' AND'.join(new_conditions)
    if len(tables) > 1:
        path=g.find_join_path(tables)
        first_table = path[0][0]
        for p in path:
            joins += f"JOIN {p[1]} ON {p[0]}.{p[2]}={p[1]}.{p[2]} "
    else:
        first_table = next(iter(tables))
    newSQL = generate_sql.format(
        columns = ','.join(new_columns),
        tables = first_table,
        joins = joins,
        conditions = new_conditions,
    )
    print(newSQL)
    return newSQL