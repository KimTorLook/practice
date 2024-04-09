"""def state():
    arg = 0

    while arg != "exit":
        arg = str(input())
        if arg == "1":
            print("one")       
        elif arg == "2":
            print("two")
            
        elif arg == "3":
            print("three")
        elif arg == "exit":
            break
        else:
            print("unknow")


state()












#2 try use array
def state2():
    arg = {"1":"one","2":"two","3":"three"}
    question = "0"
    while question != "exit":
        question = str(input())
        if question in arg.keys():
            print(arg[question])
        elif question != arg.keys():
            print("unknow")

state2()

"""

















#classmate output
eng = [0, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
u = eng[:10]
x = input('pls input a no.')
while x != 'exit':
    y = int(x)
    print(u[y])
    x = input('pls input a no.')






