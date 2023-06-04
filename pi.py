from random import random
count=0
try:
    a=eval(input("重复实验次数："))
    for i in range(a):
        x=random()
        y=random()
        if x**2+y**2<1:
            count+=1
    print("π的值约为：{:.2f}".format(4*count/a))
except:
    print("请输入整数！")