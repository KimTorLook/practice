
import random
answer = []

def GenRamdomNum() -> list:
    Num1 = 0

    for x in range(1,3):
        
        Num1 = random.randint(1,99)
        answer.append( Num1 )
    return answer

print(GenRamdomNum())





#2  Gen two random nums by using a list
import random
answer = []

def GenRamdomNum() -> list:  
    Num1 = 0

    for x in range(1,3):
        
        Num1 = random.randint(1,99)
        answer.append( Num1 )
        x+=1
    return answer

print(f"the first Num:{answer[0]} and the second Num:{answer[1]}")
print(f"{answer[0]} + {answer[1]} = {answer[0] + answer[1]}")






#3  Gen two random nums by using a list, sum of these and ask for the answer.
import random
answer = []
def GenRamdomNum() -> list:
    Num1 = 0

    for x in range(1,3):
        Num1 = random.randint(1,99)
        answer.append( Num1 )
        x+=1
    
def JudgeSys() -> str :
    num1 = int(input(f"{answer[0]} + {answer[1]} =?? answer here -->"))
    if num1 == (answer[0]  + answer[1]):
        print(f"Correct")
    else:
        print(f"Wrong")
    return 

GenRamdomNum()
JudgeSys()








def main() -> None:
    GenRamdomNum()
    JudgeSys()


if __name__ == '__main__':
    GenRamdomNum()
    JudgeSys()

