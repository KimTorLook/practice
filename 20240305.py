"""
def say(name, age=10):
...     print(f"{name} is {age} year old!")
...
>>> say("Peter", 20)
Peter is 20 year old!
>>> say("Peter")
Peter is 10 year old!
"""
#1

def say_hello():
    print("say")

def say_hello():
    print("Hi")

a=say_hello
print(a())
"""

"""
#2
def say_hello(say, hello ):
    print(say, hello)


a=say_hello
print(a(1))


#3
def sum(*arg, **kwarg):
    b=0
    for n in arg:
        b += n
    print(b)

    for key, value in kwarg.items():
        print(f"{key}:{value}")


a=sum
print(a(1,2,3, name="alice", age=30))
"""

def sum(*aaa):
    b=0
    for n in aaa:
        b += n
    print(b)


'''@sum
def multiply(ccc):
    m=0
    for n in ccc:
        m-= n
''' 
a=sum
print(a(1,2,3))

"""
def main() -> None:
    sum()
    multiply()


if __name__ == '__main__':
    sum()

#20240306
def out_func(f):
    def in_func():
        f()
        f()
        f()
        f()
        return
    return in_func

def unknow():
    print("hello")

a=out_func

print(a)
print(a(unknow))
print(a(unknow)())
