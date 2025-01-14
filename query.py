
q0 = "SELECT empid,name,dept FROM employee WHERE dept='sales' AND name='ava';"

q1 = "SELECT click,pctr,dat FROM t1 WHERE uin='u1' and docid='d1';"

q2 = "SELECT SUM(click) FROM t1 WHERE age='1' and subcategory='diet';"

q3 = "SELECT SUM(click) FROM t1 WHERE category='Film';"

table_q = "SELECT sub_table_names FROM meta_table WHERE table_name='{table_name}';"

colum_q = "SELECT table_names FROM meta_colum WHERE colum_name='{colum_name}' AND raw_table_name='{raw_table_name}';"