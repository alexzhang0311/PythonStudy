###小整数对象池###
'''
[-5,256] 之间的小整数常驻内存中，可以重复使用
'''
a_num = 1
b_num = 1

print(id(a_num),id(b_num))

###字符串###
'''
如果两个字符串的字符相同，并且只包含英文字符，那么会公用同一对象
避免频繁的开辟，关闭内存空间
'''
a = 'alex'
b = 'alex'
c = 'hello world'
d = 'hello world'
print(id(a),id(b),id(c),id(d))

import sys,gc

print(sys.getrefcount(a_num)) #被引用了134次

