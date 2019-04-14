'''
Author: Justin
Date: 2019/04/08
Info: Coding Club
'''

#--Librarys--

import random as rand

#--Functions--

def D6():
    return rand.randint(1, 6)

def D20():
    return rand.randint(1, 20)

def D100():
    return rand.randint(1, 100)

def greeting():
    return print("hello world")

#--Vars&Consts--

playerName = "Bob William Christian Smith Richard Johns"

#--Main--

print('''
======================================
+ Hello kind Creetins of Grinderland +
+             Welcome                +
======================================
''')
greeting()
