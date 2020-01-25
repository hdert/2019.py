'''
Author: hdert
Date: 19/5/20
'''

#--Librarys--



#--Main--

print( "Hi" )
age = 19
while( True ):
    print( "Hello {}".format(age) )
    print( "Also in the loop" )
    age -= 1
    if( age < 1 ):
        break
print( "Out of loop" )

