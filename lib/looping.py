#!/usr/bin/env python3

def happy_new_year():
   year = 10
   while year >= 1:
         
         print(year) 
         year -= 1


   print("Happy New Year!")
        


def square_integers(int_list):
    # code goes here!
    int_list=[1, 2, 3, 4, 5]
    list=[n**2 for n in int_list]
    return list

def fizzbuzz():
    # code goes here!
    num=1
    for num in range(1, 101):
        print(num)
        
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz")
        else:
            print(num)
        num+=1


