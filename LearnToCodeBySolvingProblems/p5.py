#dmoj coci06c5p1

swap_type = []
swap_type = str(input())    

def three_ball(swap_type:str)->int:
    ball=1
    for s in swap_type:    # 將交換的代號及次數放入迴圈
        if ball == 1:      # 波的位置: 1=左, 2=中, 3=右  
            if s == "A":   # A=左中交換, B=中右, C=左右
                ball += 1
            elif s == "B": 
                pass
            elif s == "C":
                ball += 2

        elif ball == 2:
            if s == "A": 
                ball -= 1
            elif s == "B": 
                ball += 1
            elif s == "C":
                pass

        elif ball == 3:
            if s == "A": 
                pass
            elif s == "B": 
                ball -= 1
            elif s == "C":
                ball -= 2

    return ball



print(three_ball(swap_type))