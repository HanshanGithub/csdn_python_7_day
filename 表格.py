import pandas as pd
# 1：读取指定行
# 读取指定的单行，数据会存在列表里面
# 这个会直接默认读取到这个Excel的第一个表单
filename = "D:/AmStorage/My_File/SCDN_test/file/grade.xlsx"
df2 = pd.read_excel(filename, sheet_name='操作系统')
df = pd.read_excel(filename)
# 0表示第一行 这里读取数据并不包含表头，要注意哦！
data = df.loc[0].values
print("读取指定行的数据：\n{0}".format(data))
 
# 读取指定的多行，数据会存在嵌套的列表里面 
# 读取指定多行的话，就要在loc[]里面嵌套列表指定行数
data = df.loc[[1,2]].values
print("读取指定行的数据：\n{0}".format(data))
 
# 读取指定的行列 
# 读取第一行第二列的值，这里不需要嵌套列表
data = df.iloc[1,2]
print("读取指定行的数据：\n{0}".format(data))

# 读取指定的多行多列值 
# 读取第一行第二行的title以及data列的值，这里需要嵌套列表
data = df.loc[[1,2],['期中成绩','期末成绩']].values
print("读取指定行的数据：\n{0}".format(data))

# 获取所有行的指定列 
# 读所有行的title以及data列的值，这里需要嵌套列表
data=df.loc[:,['期中成绩','期末成绩']].values
print("读取指定行的数据：\n{0}".format(data))
 
# 获取行号并打印输出 
print("输出行号列表",df.index.values)
 
# 获取列名并打印输出 
print("输出列标题",df.columns.values)
 
# 获取指定行数的值
# 这个方法类似于head()方法以及df.values方法
print("输出值",df.sample(3).values)

# 获取指定列的值
print("输出值\n",df['期末成绩'].values)

# 关闭文件

