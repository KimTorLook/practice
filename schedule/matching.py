from itertools import permutations 

persons = ['Jay', 'JC', 'Henry', 'Ian', 'Bi', 'Kelly', 'David', 'Emma', 'Fany']
match = []

 
perm = permutations(persons, 9) 
 
for i in perm: 
    print(i)
    match.append(i)


