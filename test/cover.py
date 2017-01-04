#!/usr/bin/python3

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
    
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
    def get(self):
    	return self.__secretCount
counter = JustCounter()
counter.count()
print (counter.get())
print (counter.publicCount)
'''print (counter.__secretCount) ''' # 报错，实例不能访问私有变量
print ("created by tengxing")