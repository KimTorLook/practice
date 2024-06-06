'''
schedule
我想寫個program編更表， 一編就編一年。
每個星期日當更。崗位上大約有10個。
我有一班兄弟會做呢d崗位。
有人係會參加做多個一個崗位，￼
但每個星期日每個人只能做一個崗位。
而且我想每個人都能平均參與。

1.365日
2.有10個崗位
3.有一人有多過一個崗位
4.sunday 1人只做1崗位
5.每個人都能平均參與
'''


from matching import perm
from scheduel import timeschudule
from random import 
position = ['CEO', 'CFO', 'CTO', 'HR Manager', 'Sale Manager', 'Maketing Manager', 'Purchasing Manager', 'Manufactoring Manager', 'General Manager', 'Customer Service Manager']

# 1. 先random 1個 sequence 抽每日的順序
# 2. permutation 個 persons , 並設有sequence編號
# 3. 將permutation sequence 與 random sequence match up 
# 4. 將每個sequence 最後 append 多一個 person 作為最後一個position
# 5. 用 for loop 將matching 完整呈現