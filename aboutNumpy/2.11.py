#-*- coding:UTF-8 -*-
from head import *
#有关数组的部分
#创建
#函数里用[]还是()都一样
a = np.array([1,2,3,4])
b = np.array((1,2,3,4))
c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#多维数组最外面还要加[]框起来啊
print 'a==b',a==b
print 'a=',a
print 'b=',b
print 'c=',c

#数组的大小可以通过其shape属性获得
print 'a.shape=',a.shape
#也可以通过reshape改变,但是不能改变数据大小
print 'c.reshape(2,6)=',c.reshape(2,6)

#数据类型可以用dtype获得，也可以创建时指定dtype，！！！不是方法！！！
print 'c.dtype',c.dtype
a = np.array([1,2,3,4],dtype = np.float)
print 'a.dtype',a.dtype

#有关数组创建的函数
#arange函数，指定初、终、步长
print 'np.arange(1,10,2)',np.arange(1,10,2)
#linspace指定初、终、个数
print 'np.linspace(1,10,10)',np.linspace(1,10,10)
#logspace指定初、终、比例
print 'np.logspace(1,10,10)',np.logspace(1,100,10)
#可以使用frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
#就是把别的类型当数来读,！！！必须恰好可以读完，即原数据大小必须是目标大小的整数倍！！！
print 'np.fromstring("abcde",dtype = np.int8)',np.fromstring('abcde',dtype = np.int8)
#可以写一个Python的函数，它将数组下标转换为数组中对应的值，然后使用此函数创建数组
def func(i):
    return i%4+1
def func2(i,j):
    return (i+1)*(j+1)
print 'np.fromfunction(func,(10,))',np.fromfunction(func,(10,)) # ！！输入必须为元组,表示所创数组的维数和大小  ！！！
print 'np.fromfunction(func2,(9,9))',np.fromfunction(func2,(9,9))
