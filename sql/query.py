q1 = "SELECT click,pctr,\"date\" FROM t1 WHERE userid='u1' and docid='d1';"

q2 = "SELECT sex,age,device FROM t1 WHERE age='22' and subcategory='Drama';"

q3 = "SELECT SUM(click) FROM t1 WHERE category='Film';"

table_q = "SELECT sub_table_names FROM meta_table WHERE table_name='{table_name}';"

colum_q = "SELECT colum_name,table_names FROM meta_colum WHERE colum_name='{colum_name}' AND raw_table_name='{raw_table_name}';"

index_q = "SELECT colum_name,table_names FROM meta_colum WHERE raw_table_name='{raw_table_name}' AND array_length(table_names,1) >= 2;"

generate_sql = "SELECT {columns} FROM {tables} {joins} WHERE {conditions};"