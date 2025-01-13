## sqlparse

### token
sqlparse 中的 Token 类型有以下顶级分类：
|  **分类**   | **描述**  |
|  ----  | ----  |
|`Keyword`	|SQL 的关键字，例如 SELECT, FROM, WHERE。|
|`Name`	|标识符（例如表名、列名、别名）。|
|`Literal`	|字面值（例如字符串、数字、布尔值）。|
|`Operator`	|运算符，例如 `=`, `<`, `>`, `+`, `-`。|
|`Text`	|其他文本（例如空格、换行符等）。|
|`Punctuation`	|标点符号（例如 `,`, `;`, `(`, `)`）。|
|`Wildcard`	|通配符，例如 `*`。|
|`Comment`	|注释（例如 -- 注释 或 `/*` 注释 `*/`）。|
|`Comparison`	|比较运算符（例如 `=`, `<`, `>`，部分是 Operator 的子类型）。|

在顶级分类下，sqlparse 还细化了许多子分类，用来描述不同的 SQL 元素。以下是一些常用的子分类：

####  Keyword（关键字）
关键字分为多种子类型，用于区分 SQL 的不同部分：

* `Keyword.DML`：数据操作语言关键字，例如 SELECT, INSERT, UPDATE, DELETE。
* `Keyword.DDL`：数据定义语言关键字，例如 CREATE, ALTER, DROP。
* `Keyword.TCL`：事务控制语言关键字，例如 COMMIT, ROLLBACK, SAVEPOINT。
* `Keyword.CTE`：公用表表达式关键字，例如 WITH。
其他：如 FROM, WHERE, JOIN 等普通关键字。

#### Name（标识符）
标识符用于命名 SQL 的实体，如表名、列名、别名等：

* `Name`：普通的标识符（如 users 表名）。
* `Name.Builtin`：内置函数或系统对象（如 COUNT, MAX）。
* `Name.Function`：函数名（如 SUM, AVG）。
* `Name.Placeholder`：占位符（如 ? 或 :param）。
#### Literal（字面值）
字面值表示具体的数据值：

* `Literal.String.Single`：单引号字符串（如 'hello'）。
* `Literal.String.Symbol`：符号字符串（如 "column_name"）。
* `Literal.Number.Integer`：整数（如 123）。
* `Literal.Number.Float`：浮点数（如 3.14）。
* `Literal.Number.Hexadecimal`：十六进制数字（如 0x1A）。
#### Operator（运算符）
* `Operator.Comparison`：比较运算符（如 =, <, >, !=）。
* `Operator.Logical`：逻辑运算符（如 AND, OR, NOT）。
* `Operator.Arithmetic`：算术运算符（如 +, -, *, /）。
#### Text（文本）
* `Text.Whitespace`：空格或换行符（如 ' ' 或 '\n'）。
* `Text.Whitespace.Newline`：明确的换行符。
* `Text.Error`：无法解析的未知内容。
#### Punctuation（标点符号）
标点符号在 SQL 中的用途：

* 逗号（,）：分隔列或语句。
* 分号（;）：结束语句。
* 括号（(, )）：用于分组。
#### Wildcard（通配符）
* `Wildcard`：通配符，例如 *。
#### Comment（注释）
* `Comment.Single`：单行注释（如 -- 注释）。
* `Comment.Multiline`：多行注释（如 /* 注释 */）。