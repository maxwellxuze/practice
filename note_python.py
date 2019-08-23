#note of numpy、panda、《Python数据分析》: 
import numpy as np
import panda as pd

#基础
'''
range(stop)
range(start, stop[, step])
start：计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop：计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
#循环
for i in range(5) #0,1,2,3,4
for i in range(3,10,2) # 3,5,7,9

#条件
if : #注意条件后面加冒号
elif:
else:


a=np.array([[1,2,3],[4,5,6]])
a.shape #矩阵大小
a[0:5,:]  a[0:5] #前5行
a[-5:] #后5行
a**3 #a3次方

'''
 a[:-1]表示从0到倒数第二行
 a[-1]最后一行
 a[1:]从1到最后一行
 a[1：-1]从1行到倒数第二行
 即：右边为开区
 '''
 
 a[[2,3,6,5]] #数组a中第2,3,6,5行
 a[[2,3],[4,5]]#数组中[2,3],[3,5]行元素
 
 #区别DateFrame与Series********************************************************
 #Series只传入一个字典，则索引为原字典的键！！！！
 #Series只有索引，没有columns.

 series1 = Series({'':VALUE,...},index=['','',''])
 #DateFrame由多个series组成的列，共用一个索引index
 
 
 pd.null(obj2)#检测空值
 frame = DateFrame({'Name':{1:'tim',2:'tom'}})#'Name'为列，内层键为索引
 
 
 
 #读取文件*******************************************************
 pd.read_csv('path',skiprows=[1,2,4]) #跳过行
 pd.read_csv('path',names=['a','b','c','d']) #定义列名称
 pd.read_csv('path',names=['a','b','c','d',index_col='d')  #将指定列放到索引位置
 pd.read_table('path',sep=',') #指定分隔符，可使用正则表达式
 
 #输出文件 to_csv、from_csv
 date.to_csv('path') #输出,分割csv格式***************************
 date.to_csv('path',index=False,clo=['b','c','e'],na_rep='NULL') #不输出索引，输出指定列，空值指定名称
 
 
 #数据整理*******************************************************
 data.drop_duplicates('k1') #对k1列去重
 #使用map进行映射
 date.replace([99,100],np.nan) #将99，100替换为NAN
 date.replace({99:'a',100:'b'}) #使用字典替换
 date.rename(index=str.title,columns=str.upper) #更改名称
 
 pd.cut(ages,bins,labels=['a','b']) #bins=[20,40,60,100] 划分区间及定义区间名称
 pd.qcut(date,4) #按4分位数切割
 
 'date' in val #寻找val中的'date'字符串
 
 
 #matplotlib*******************************************************
 #如果为plot()命令提供单个列表或数组，则matplotlib假定它是一系列y值，并自动为您生成x值。
 pip --default-timeout=100 install -U Pillow #设置延迟时间