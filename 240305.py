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
