import sqlparse
from sqlparse.sql import IdentifierList,Identifier,Where,Comparison,Function
from sqlparse.tokens import Keyword, DML
from query import q0,q1,q2

def getTokens(sql):
  p = sqlparse.parse(sql)
  return p[0]

def getQueryColName(tokens):
  columns = []
  select_found = False
  for token in tokens:
    # 检查 SELECT
    if token.ttype == DML and token.value.upper() == "SELECT":
        select_found = True
    elif select_found:
      # 如果是列名列表
      if isinstance(token, IdentifierList):
        for identifier in token.get_identifiers():
          if isinstance(identifier, Function):
            func = {}
            for tok in identifier.tokens:
              if tok.value.startswith('('):
                func['param'] = tok.value.strip('()')
              else:
                func['func'] = tok.value
            columns.append(func) 
            # # 函数调用，保留完整表示
            # columns.append(str(identifier))  # 转换为完整字符串
          elif isinstance(identifier, Identifier):
            # 普通标识符
            columns.append(identifier.get_real_name() or identifier.value)
      # 如果是单独的列名或函数
      elif isinstance(token, Identifier):
        columns.append(token.get_real_name() or token.value)
      elif isinstance(token, Function):
        # 函数调用，保留完整表示
        func = {}
        for tok in token.tokens:
          if tok.value.startswith('('):
            func['param'] = tok.value.strip('()')
          else:
            func['func'] = tok.value
        columns.append(func)  
      # 遇到 FROM 就停止解析
      elif token.ttype == Keyword and token.value.upper() == "FROM":
        break
  return columns

def getQueryTabName(tokens):
  columns = []
  from_found = False
  for token in tokens:
    if token.ttype == Keyword and token.value.upper() == "FROM":
      from_found = True
    elif from_found:
      if isinstance(token, IdentifierList):
        for identifier in token.get_identifiers():
          columns.append(identifier.get_real_name() or identifier.value)
      elif isinstance(token, Identifier):
        columns.append(token.get_real_name() or identifier.value)
  return columns

def getConditions(tokens):
  conditions = []  # 用于存储条件的列表
  where_found = False  # 标记是否找到 WHERE 子句
  for token in tokens:
    # 检查 WHERE 子句
    if isinstance(token, Where):
      where_found = True
      for sub_token in token.tokens:
        # 检查子 Token 是否为 Comparison 对象（即条件表达式）
        if isinstance(sub_token, Comparison):
          # 解析 Comparison 对象
          comparison_tokens = sub_token.tokens
          column = None
          predicate = None
          value = None
          # 遍历 Comparison 的子 token
          for comp_token in comparison_tokens:
            if isinstance(comp_token, Identifier):  # 列名
              column = comp_token.value.strip()
            elif comp_token.ttype in sqlparse.tokens.Operator.Comparison:  # 运算符
              predicate = comp_token.value.strip()
            elif comp_token.ttype in sqlparse.tokens.Literal:  # 值
              value = comp_token.value.strip()
            # 将条件对象添加到列表
          if column or predicate or value:
            conditions.append({
              'column': column,
              'predicate': predicate,
              'value': value
            })
  return conditions

if __name__ == "__main__":
  # sql = "SELECT name,age FROM users,course WHERE age > 30 and name = 'alice';"
  statement = getTokens(q2)

  print(getQueryColName(statement.tokens))
  print(getQueryTabName(statement.tokens))
  print(getConditions(statement.tokens))