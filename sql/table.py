from itertools import combinations
from .query import index_q,table_q,meta_colums_q

# 获取需要的每个子表的列名，返回一个字典
def getColumnDict(tables,conn):
    table2Colnmns = {}
    for table in tables:
        columns = getColumnsName(table,conn)
        table2Colnmns[table] = columns
    return table2Colnmns

# 获取子表的列名
def getColumnsName(tableName,conn):
    columns = conn.execSQL(meta_colums_q.format(table_name=tableName))
    return set(columns['column_name'])

# 获取需要的表名 table_columns是每个子表有的列名，columns是查询需要的列名
def getNeedtables(columns, table_columns):
    tables = list(table_columns.items())
    min_table_set = None
    # 遍历全部长度的子集
    for r in range(1, len(tables) + 1):
        # 生成所有r个表的组合
        for combo in combinations(tables, r):
            # print(combo)
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
    
    return set(table for table, _ in min_table_set) if min_table_set else set()

# 获取倒排索引
def getInvertedIndex(raw_table_name,conn):
    index = {}
    data = conn.execSQL(index_q.format(
            raw_table_name =  raw_table_name, #TODO(多表连接有bug)
        ))
    for i,row in data.iterrows():
        index[row['colum_name']] = row['table_names']
    return index

# 获取大表的全部子表,当有‘*’的时候，会用到
def getAllSubTables(raw_table,conn):
    data = conn.execSQL(table_q.format(
            table_name =  raw_table,
        ))
    return set(data['sub_table_names'][0])
