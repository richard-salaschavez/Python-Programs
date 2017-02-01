"""RichardSalasChavezA2Q1

COMP 1012 SECTION A01
INSTRUCTOR Terry Andres
ASSIGNMENT: A2 Question 1
AUTHOR Richard Salas Chavez
VERSION February 3, 2015

PURPOSE: to find the square root of your student number with Python in as
many ways as you can. 
"""
# imports

import math, cmath, numpy, time

#s_ = 7654321 #student number
s_ = 7764077 #my student number

print 'Finding the square root of' , s_

#Simple math operations method
powerOperator = s_ ** 0.5

print '\nUsing the power operator: %r' % powerOperator

#Search method
#begin with the interger 1 and increment its value by 1 until a number is found
#with a square greater than the student number 

search = 1
while (search ** 2) < s_ :
    search += 1

print
print ('Using search with increment of 1, the root lies between %d and %d' %  
        (search - 1, search))

#Math library functions method
#use square root functions from various libraries 

math_ = math.sqrt(s_) #from math library

print
print 'Using math.sqrt:          %r' % math_

numpy_ = numpy.sqrt(s_) #from numpy library

print 'Using numpy.sqrt:         %r' % numpy_

cmath_ = cmath.sqrt(s_) #from cmath library

print 'Using cmath.sqrt:\n                          %r' % cmath_

cmath_ = cmath.sqrt(-s_)

print '                          %r' % cmath_

#Logarithms method: using log base 10
print '\nSimulating the manual calculation of square root using logarithms:'
y_ = 0.5 #square root power
x_ = s_ 
root = 10 ** (y_ * math.log10(x_)) # math identity, page 2 of assignment
log_10 = math.log10(s_)
log_10_root = math.log10(root)

print 'log10(7654321) =          %.4f rounded to 4 decimals' % log_10
print 'log10(root) =             %.5f' % log_10_root
print 'root =                    %.0f to 4 significant figures' % root

#Factoring method
#we factor out the square root of 4 from the square root of the student number
#until the number inside the square root is between 0.4 and 1.6

print '\nFinding an appropriate root by factoring ; the root is:'

n_ = 4. * s_ #n_1 is 4 times n_0 
term = 0

while n_ > 1.6:
    factor = (2 ** term)
    n_ = n_ / 4
    term += 1
    print '%30d * sqrt(%r)' % (factor, n_)

#Babylonian method
print '\nUsing the Babylonian method:'
print

count = 0
y_i = factor
x_ = s_
small = 1.e-20

while abs(y_i - x_/float(y_i)) > small :
    count += 1
    y_i_1 = (y_i + x_/float(y_i)) / 2 #y_i_1 represents y_i+1 in the equation
    print '     %d: root estimate:   %r' % (count, y_i)
    y_i = y_i_1
print '  final root estimate:   %r' % y_i

#Infinite series

x_ = n_ - 1 #the series calculates for (x_ + 1) = n_ thus x_ = (n_ - 1)

print '\nUsing infinite series with x = %r' % x_
    
count = 0
product = 1.0
term = product
constant = 0.5 #constant in mathematical terms, i.e. not a variable but a number
terms = [ ] #empty list that will hold our terms 
small = 1.e-17 #small number that satisfies the convergence criterion

while abs(term) > small:
    print '    count: %3d      term: %r' % (count, term)
    count += 1
    product = product * constant * x_/count
    constant -= 1
    terms.append(term)
    term = product

sumForwards = factor * sum(terms)
sumBackwards = factor * sum(reversed(terms))

print '    Sum forwards is     %r' % sumForwards
print '    Sum backwards is    %r' % sumBackwards    


#Multi Precision Babylonian Method
#Unlike the Babylonian method now avoid float type numbers for higher precision
print '\nUsing the Babylonian method and interger calculations:'

count = 0
BIG_NUM = 10 ** 40
y_i = factor * BIG_NUM
x_ = s_ * (BIG_NUM ** 2)
epsilon = 1e20

while abs(y_i - x_/y_i) > epsilon :
    count += 1
    y_i_1 = (y_i + x_/y_i) / 2
    print ('     %d: root estimate:   %d_%040d' % (count, y_i // BIG_NUM, 
            y_i % BIG_NUM))
    y_i = y_i_1
print '  final root estimate:   %d_%d' % (y_i // BIG_NUM, y_i % BIG_NUM)


#Multi precision infinite series
n_ = (s_ * BIG_NUM) / ((factor) ** 2) #recalculate n_ using int values
x_ = n_ - (1 * BIG_NUM)
sign = '-'
val = x_

print ('\nUsing infinite series with x = %d_%d:' % (n_ // 
        BIG_NUM, abs(x_) % BIG_NUM))

count = 0
total = 0
product = 1 * BIG_NUM
term = product 
numerator = 1
epsilon = 1e5

while abs(term) > epsilon :
    print '    count: %3d     total: %d_%040d' % (count, total // BIG_NUM, abs(total) % BIG_NUM)
    #print '    count:', "%4d" % count
    #print ('    count:   %d     total: %d_%d' % (count, total // BIG_NUM, 
            #abs(total) % BIG_NUM))
    count += 1
    total += term
    product = (product * numerator * x_ ) / (count * 10 ** 40 * 2)
    numerator -= 2
    term = product

finalEstimate = total * factor
print ('    Final estimate is     %d_%d' % (finalEstimate // BIG_NUM, 
        abs(finalEstimate) % BIG_NUM))

print "\nProgramed by Richard Salas Chavez"
print "Date:", time.ctime()
print "End of processing"

    
        
    
    
    
    
