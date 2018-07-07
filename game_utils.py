import sys,os
import io

def print_as_table(d):
    for k, v in d.items():
        print (k,"  : \n",v)
title = '''
                                                                                                                            
=============================================================================================================================
     _______.     ___      .__   __.     __    __   _______         _______..___________.  ______   .______     ____    ____
    /       |    /   \     |  \ |  |    |  |  |  | |   ____|       /       ||           | /  __  \  |   _  \    \   \  /   /
   |   (----`   /  ^  \    |   \|  |    |  |__|  | |  |__         |   (----``---|  |----`|  |  |  | |  |_)  |    \   \/   / 
    \   \      /  /_\  \   |  . `  |    |   __   | |   __|         \   \        |  |     |  |  |  | |      /      \_    _/  
.----)   |    /  _____  \  |  |\   |    |  |  |  | |  |____    .----)   |       |  |     |  `--'  | |  |\  \----.   |  |    
|_______/    /__/     \__\ |__| \__|    |__|  |__| |_______|   |_______/        |__|      \______/  | _| `._____|   |__|    
                                                                                                                            
=============================================================================================================================
'''
def simple_progress_bar(percentage):
    print("[",end='')
    for i in range(0,50):
        if i/50 < percentage:
            print("#",end='')
        else:
            print("_",end='')
    print("]",end='')

def print_property_with_progress_bar(name,property,max_value):
    print(name," ",property,"       ",end='')
    simple_progress_bar(property/max_value)
    print("\n")

def print_status(status):
    print(title)
    print("===================================================================================================================")
    print("当前资金:    ",status["Money"])
    print_property_with_progress_bar("还债进度:    ",status["Debt"],50000)
    print_property_with_progress_bar("当前健康：   ",status["HP"],100)
    print("===================================================================================================================")
    print(status["Message"])