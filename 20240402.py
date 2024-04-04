import random
#1  guest Num 1~ 6 


def guest():
    return int(input("please guest:"))


def guestNum():
    x = random.randint(1,6)
    s = guest()

    while s != x:           #use while loop to asking num and march with the guest num
        if s > x:
            print(f"You Num is greater than guest num")
            
        else:
            print(f"You Num is less than guest num")
        s =guest()   
        
    print(f"random num is {x}")
    print(f"You are right")

'''guestNum()
'''
#2 class 

class guestNum:

    def guest(self) -> int:
        return int(input("please guest:"))

    def guestNum(self):
        print(1)
        x = random.randint(1,6)
        s = self.guest()

        while s != x:
            if s > x:
                print(f"You Num is greater than guest num")
            else:
                print(f"You Num is less than guest num")
            s = self.guest()   
            
        print(f"random num is {x}")
        print(f"You are right")

a = guestNum()
print(9)
a.guestNum()

#3
