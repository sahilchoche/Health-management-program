# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:03:11 2021

@author: HP
"""

import datetime
def gettime():
    return datetime.datetime.now()
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

def take (k): 
    if k==1:
        c=int(input(" press 1 for_execersise press 2 for_food:"))
        if c==1:
             value=input("type here\n")
             with open("sahil-ex.txt","a") as op:
                 op.write(str([str(gettime())])+": "+value+"\n")
             print("successfully written")
        elif c==2:
              value=input("type here\n")
              with open("sahil-food.txt","a") as op:
                  op.write(str([str(gettime())])+": "+value+"\n")
              print("successfully written")
    elif k==2:
         c=int(input(" press 1 for_execersise press 2 for_food:"))
         if c==1:
             value=input("type here\n")
             with open("sharon-ex.txt","a") as op:
                 op.write(str([str(gettime())])+": "+value+"\n")
             print("successfully written")
         if c==2:
             value=input("type here\n")
             with open("sharon-food.txt","a") as op:
                 op.write(str([str(gettime())])+": "+value+"\n")
             print("successfully written")
    elif k==3:
        
         c=int(input(" press 1 for_execersise press 2 for_food:"))
         if c==1:
            value=input("type here\n")
            with open("husaim-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
         if c ==2:
             value=input("type here\n")
             with open("husain-food.txt","a") as op:
                 op.write(str([str(gettime())])+": "+value+"\n")
             print("successfully written")
    else:
        
         print("plz enter valid number")
def retrieve (k):
    if k==1:
        c=int(input("press 1 for_execersise press 2 for_food"))
        if c==1:
            with open("sahil-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("sahil-food.txt") as op:
                for i in op:
                    print(i,end="")
        
        elif k==2:
            
            c=int(input("press 1 for_execersise press 2 for_food"))
        if c==1:
            with open("sharon-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("sharon-food.txt") as op:
                for i in op:
                    print(i,end="")
        elif k==3:
          
          c=int(input("press 1 for_execersise press 2 for_food"))
        if c==1:
            with open("husain-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("husain-food.txt") as op:
                for i in op:
                    print(i,end="")
        else:
            print("enter the valid data")
if a==1:
    b = int(input("Press 1 for sahil 2 for sharon 3 for husain "))
    take(b)
else: 
    b = int(input("Press 1 for sahil 2 for sharon 3 for husain "))
    retrieve(b)            
                    