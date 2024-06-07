from itertools import permutations 
from random import choice

persons = ['Jay', 'JC', 'Henry', 'Ian', 'Bi', 'Kelly', 'David', 'Emma', 'Fany']
match = []

def permutat():
    perm = permutations(persons, 9) 
    perm_in_list = list(perm)
    tenth_person = []   #簡單啲，將兩組序列分別儲存，然後mix up
    


    counter = 0

    for iterate in perm: 






        counter +=1    
        permtat_outcome = f"{counter}. {iterate} "
        match.append(permtat_outcome)
        print(match)


permutat()
