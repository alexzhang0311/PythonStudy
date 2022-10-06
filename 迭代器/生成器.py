###不是一次性把数据全部加载到内存中，遍历的时候才会生成###

###普通列表###
a = [x for x in range(100)]
###生成器###
b = (x for x in range(100))

print(next(b))
print(next(b))
print('**************')
def my_gen():
    yield 1
    yield 2
    yield 3

ret = my_gen()

print(next(ret))
print(next(ret))
print(next(ret))

###这是一个生成器函数###
def my_gen(start,end):
    index = start
    while index <= end:
        yield index
        index += 1

ret = my_gen(1, 2)

print(next(ret))
print(next(ret))

print('------------send--------------')

#1.send 函数可以传递值给yield 表达式，next不可以
#2.第一次执行生成器代码的时候，send函数必须要传一个值进去，next函数可以不用传
#3. return 会触发stopIterator异常

def my_gen(start):
    index = start
    while index < 10:
        temp = yield index
        print(temp)
        index += 1
        #return 'hi'

ret = my_gen(1)
print(ret.send(None))
print(next(ret))
print(next(ret))
print(ret.send('alexxzhang'))

###斐波那契数列###
orgin = []
while len(orgin) < 10:
    index = len(orgin)
    if index < 2:
        orgin.append(1)
    else:
        new = orgin[index-1] + orgin[index-2]
        orgin.append(new)
print(orgin)


def fib(count):
    a,b = 0,1
    index = 1
    while index <= count:
        yield b
        c = b
        # print(b)
        b = a + b
        a = c
        index += 1
        

f = fib(10)


for i in fib(10):
    print(i)


def neteasy_music(duration):
    time = 0
    while time <= duration:
        print('歌曲听到第%d分钟了'%time)
        time += 1
        yield None
    # raise StopIteration()

def youku_movie(duration):
    time = 0
    while time <= duration:
        print('电影看到第%d分钟了'%time)
        time += 1
        yield None
    # raise StopIteration()

def main():
    music = neteasy_music(10)
    movie = youku_movie(10)
    while True:
        try:
            next(music)
        except StopIteration:
            print('音乐播放完毕')
        try:
            next(movie)
        except StopIteration:
            print('电影播放完毕')
            break

if __name__ == "__main__":
    main()