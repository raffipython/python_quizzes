# -*- coding: utf-8 -*-
class Calculator():
    def __init__(self):
        pass
    
    def menu(self):
        print("""
        ------------------
        a - addition
        s - substraction
        m - multiplication
        d - division
        o - module
        e - exit
        """)
    
    @staticmethod
    def addition(number1, number2):
        result = number1 + number2
        print("#####\nResult: {}\n#####".format(result))    
   
    @staticmethod
    def substraction(number1, number2):
        result = number1 - number2
        print("#####\nResult: {}\n#####".format(result))    
 
    @staticmethod
    def multiplier(number1, number2):
        result = number1 * number2
        print("#####\nResult: {}\n#####".format(result))    
            
    @staticmethod
    def dividor(number1, number2):
        if number2 != 0:
            result = number1 / number2
            print("#####\nResult: {}\n#####".format(result))
        else:
            print("divide by 0 is not permitted")

    @staticmethod
    def mod(number1, number2):
        result = number1 % number2
        print("#####\nResult: {}\n#####".format(result))    
    
c = Calculator()
selection = ""
while selection != "e": 
    c.menu()
    selection = input("Make a selection:\n")
    if selection == "e":
        pass
    else:
        first = int(input("First number: "))
        second = int(input("Second number: "))
    
        if selection == "a":
            c.addition(first, second)
        if selection == "s":
            c.substraction(first, second)
        if selection == "m":
            c.multiplier(first, second)
        if selection == "d":
            c.dividor(first, second)
        if selection == "o":
            c.mod(first, second)
