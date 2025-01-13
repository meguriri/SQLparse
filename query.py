
q0 = "SELECT empid,name,dept FROM employee WHERE dept='sales' AND name='ava';"

q1 = "SELECT click,pctr,dat FROM t1 WHERE uin='u1' and docid='d1';"

q2 = "SELECT SUM(click) FROM t1 WHERE age='1' and subcategory='diet';"

q3 = "SELECT SUM(click) FROM t1 WHERE category='Film';"

q4 = "select column_name\
  from information_schema.columns where\
  table_schema='public' and table_name \
  = 'employee'"