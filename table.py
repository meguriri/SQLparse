
def getColumnName(tableName,conn):
    query="""
    select column_name\
    from information_schema.columns where\
    table_schema='public' and table_name \
    = '
    """
    columns = conn.execSQL(query+tableName+"'")
    return columns



