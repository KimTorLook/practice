#corn volume 


r = int(input())
h = int(input())
PI = 3.141592653589793 

if r >= 1 and r <= 100 and h >= 1 and h <= 100 :
    pass
else:
    print('r & h must bewteen in 1 and 100')

volume = round((PI * (r**2) * h) /3, 2)


print(volume)