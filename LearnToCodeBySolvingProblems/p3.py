'''
    • Show marks form A team n B team
    • Show winner or tie
    • Six line of input
        ○ 3point of A
        ○ 2point of A
        ○ 1point of A
        ○ 3point of B
        ○ 2point of B
        ○ 1point of B
            § Integer 0 ~ 100
    • Output - show winner or tie
'''

aTeam3point = int(input())
aTeam2point = int(input())
aTeam1point = int(input())
bTeam3point = int(input())
bTeam2point = int(input())
bTeam1point = int(input())

aTeamTotal = aTeam3point*3 + aTeam2point*2 +  aTeam1point
bTeamTotal = bTeam3point*3 + bTeam2point*2 +  bTeam1point

if aTeamTotal > bTeamTotal:
    print('A')
elif aTeamTotal < bTeamTotal:
    print('B')
elif aTeamTotal == bTeamTotal:
    print('T')