from random import randrange
position = ['CEO', 'CFO', 'CTO', 'HR Manager', 'Sale Manager', 'Maketing Manager', 'Purchasing Manager', 'Manufactoring Manager', 'General Manager', 'Customer Service Manager']

# 1. 先random 1個 sequence 抽每日的順序                                         ok
# 2. permutation 個 persons , 並設有sequence編號                                ok
# 3. 將每個sequence 最後 append 多一個 person 作為最後一個position
# 4. 將permutation sequence 與 random sequence match up 
# 5. 用 for loop 將matching 完整呈現

def daily_sequence():
    for i in range(1,367):
        a = randrange(1,366,1)
        print(a)
        
daily_sequence()