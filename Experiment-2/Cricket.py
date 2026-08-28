# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:16:17 2026

@author: user
"""

runs_scored1 = int(input("Enter Run Scored of player "))
print(runs_scored1)
balls_faced = int(input("Enter Balls Faced by player "))
print(balls_faced)
Fours = int(input("Enter Total Fours Hit "))
print(Fours)
Six = int(input("Enter Total Six hit "))
print(Six)
Wicket_Taken = int(input("Enter total Wicket Taken "))
print(Wicket_Taken)
Run_Con = int(input("Enter Runs "))
print(Run_Con)
Overs_bowled = int(input("Enter Overs "))
print(Overs_bowled)
catch_taken = int(input("Enter Catch Taken "))
print(catch_taken)


print("Calculating Batting Strike Rate......")

sr = (runs_scored1/balls_faced) * 100
print("Batting strike Rate is ")
print(sr)


print("Calculating Balling Economy Rate..... ")

er = (Run_Con/Overs_bowled)
print("Balling Economy rate is ")
print(er)
batter = 1
if runs_scored1 >= 50 and sr >= 120:
    print("Excellent Batter")
    batter = 2
elif runs_scored1 >= 30 and sr >=100:
    print("Good Batter")
    batter = 3
elif runs_scored1 >= 20:
    print("Average Batter")
else:
    print("Poor batter")
    
bowler = 1
if Wicket_Taken >= 3 and er <= 6:
    print("Excellent Bowler")
    bowler = 2
elif Wicket_Taken >= 2 and er <= 6:
    print("Good Bowler")
    bowler = 3
elif Wicket_Taken >= 1:
    print("Average Bowler")
else:
    print("Poor Bowler")
    

if catch_taken >= 2:
    print("Outstanding Fielder")
elif catch_taken == 1:
    print("Active Fielder")
else:
    print("Needs Improvement")


print("Overall All-Rounder Decision")
if batter == 2 and bowler == 2:
    print("Star ALl-Rounder")
elif batter == 3 and bowler == 3:
    print("Strong All-Rounder")
elif batter == 3 or bowler == 3:
    print("Supporting All-Rounder")

    
