import random
import sqlite3
'''
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

guestNum()





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




#20240404 expand form 20240402 #1

#1  guest Num 1~ 100 

def num_input():
    return int(input("please guest:"))
    print('11')


def num_process():
    return random.randint(1,100)
    print('12')


def matching():
    s = num_input()
    x = num_process()
    count = 0
    while s != x:           #use while loop to asking num and march with the guest num
        if s > x:
            print(f"You Num is greater than guest num")      
        else:
            print(f"You Num is less than guest num")
        count += 1
        print(f"you hv been guest {count} times")
        s =num_input()
    count += 1
    print(f"Right, random num is {x}, you total guest {count} times ")
    
num_process()
matching()


#2 expand form 20240402 #1  making class 

class gaming:

    def guest(self):
        return int(input("please guest:"))


    def guestNum(self):
        x = random.randint(1,6)
        s = self.guest()

        while s != x:           #use while loop to asking num and march with the guest num
            if s > x:
                print(f"You Num is greater than guest num")
                
            else:
                print(f"You Num is less than guest num")
            s =self.guest()   
            
        print(f"random num is {x}")
        print(f"You are right")

a = gaming()
a.guestNum()





#3 expand form #1  making class 

class gaming:
    def num_input(self):
        return int(input("please guest:"))
        print('11')


    def num_process(self):
        return random.randint(1,100)
        print('12')


    def matching(self):
        s = self.num_input()
        x = self.num_process()
        count = 0
        while s != x:           #use while loop to asking num and march with the guest num
            if s > x:
                print(f"You Num is greater than guest num")      
            else:
                print(f"You Num is less than guest num")
            count += 1
            print(f"you hv been guest {count} times")
            s =self.num_input()
        count += 1
        print(f"Right, random num is {x}, you total guest {count} times ")

a=gaming()    
a.num_process()
a.matching()







#4 making class with __init__

class Car:
    def __init__(self,fuel_cell, engine, cylinder, autopilot):
        self.fuel_cell = fuel_cell
        self.engine = engine
        self.cylinder = cylinder
        self.autopilot = autopilot
    
    def charging(self):
        self.fuel_cell = 100

    def refuel(self):
        self.cylinder = 100
        
class EV(Car):
    def __init__(self,cell_capacity, peak_power):
        self.cell_capacity = cell_capacity
        self.peak_power = peak_power

class GV(Car):
    def __init__(self, cylinder_capacity, horsepower):
        self.cylinder_capacity = cylinder_capacity
        self.horsepower = horsepower


talsaModelS =Car('100', '670','95',True)
talsaModelY = EV('81', '760')

hondaFit = GV('40','121')
hondaJazz = GV('50', '200')

print(talsaModelS())






20240405

#1
class monster:
    def __init__(self,feet:int, wing:bool,fin:bool,horn:bool,teeth:bool):
        self.feet = feet
        self.wing = wing
        self.fin = fin
        self.horn = horn
        self.teeth = teeth


    
    def flying(self,fly):
        self.fly = fly
        if self.wing == True: print(f"{self} can flying.")

    def swimming(self, swim):
        self.swim = swim
        if self.fin ==True: 
            print(f"{self} can swimming.")
        else:
            print(f"{self} cent swimming.")


Velkhana = monster(4,True,False,False,False,)
Nergigante = monster(4,True,False,True,False)

Velkhana.swimming('swim')

'''


