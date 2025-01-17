from itertools import combinations
from .query import index_q

def getColumnDict(tables,conn):
    table2Colnmns = {}
    for table in tables:
        columns = getColumnsName(table,conn)
        table2Colnmns[table] = columns
    return table2Colnmns

def getColumnsName(tableName,conn):
    query=f"""
    select column_name\
    from information_schema.columns where\
    table_schema='public' and table_name \
    = '{tableName}';
    """
    columns = conn.execSQL(query)
    return set(columns['column_name'])

def getNeedtables(columns, table_columns):
    tables = list(table_columns.items())
    # 寻找最小表集合的变量
    min_table_set = None
    # 生成所有可能的表组合，首先从1个表开始，逐渐增加表的数量
    for r in range(1, len(tables) + 1):
        # 生成所有r个表的组合
        for combo in combinations(tables, r):
            # 合并当前组合中所有表的列
            combined_columns = set()
            for table, cols in combo:
                combined_columns.update(cols)
            # 检查是否所有需要的列都被覆盖
            if columns.issubset(combined_columns):
                # 如果覆盖了所有需要的列，更新最小表集合
                if min_table_set is None or len(combo) < len(min_table_set):
                    min_table_set = combo
        # 如果找到了覆盖所有列的组合，就可以提前退出
        if min_table_set is not None:
            break
    # 返回最小的表集合
    return set(table for table, _ in min_table_set) if min_table_set else set()


def getInvertedIndex(raw_table_name,conn):
    index = {}
    data = conn.execSQL(index_q.format(
            raw_table_name =  raw_table_name,
        ))
    for i,row in data.iterrows():
        index[row['colum_name']] = row['table_names']
    return index




