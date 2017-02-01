"""RichardSalasChavezA4Q1

COMP 1012 SECTION A01
INSTRUCTOR Terry Andres
ASSIGNMENT: A4 Question 1
AUTHOR Richard Salas Chavez
VERSION March 14, 2015

PURPOSE: to solve verbal math puzzles using brute force.
"""

#imports
import time
import math
import string
import numpy as np

ARROW = U"\N{Black RIGHTWARDS ARROWHEAD}"

PUZZLES = ("2BANANA == 102020",
            "3HE + ME == WE",
            "7TWO + TWO == FOUR",
            "7FIVE + FIVE == SEVEN",
            "8SIX + SEVEN + SEVEN == TWENTY",
            "9SEND + MORE == MONEY",
            "9SPRING + RAINS + BRING + GREEN == PLAINS",
            "9CLOCK + TELLS + TIME == CHIMES",
            "9TERRIBLE + NUMBER == THIRTEEN",
            "0ENTER YOUR OWN MATHWORD PUZZLE")

print "            W O R D   M A T H   P U Z Z L E S    "


#***************************************************************************main
def main() :
    """Where main program resides."""
    STOP_CODE = 'Q'
    code = menu(PUZZLES) #print out table of choices and gets the user choice 
    
    while code != STOP_CODE :
        #valid input requiring processing
        code = int(code)
        wordMath = PUZZLES[code][1:] #gets the word math puzzle part from the 
                                                                #tuple PUZZLES
        maxDigit = int(PUZZLES[code][0]) #gets the max digit from the constant 
                                                                #tuple PUZZLES
        if 0 <= code < 9 :
            #solves puzzles 0 t0 8
            print
            print 'Date: ' + '.' * 30 + time.ctime()
            print
            solvePuzzle(wordMath, maxDigit)
            print
            print 'Date: ' + '.' * 30 + time.ctime()
            
        else :
            #calls getPuzzle to get a puzzle from the user
            userInputPuzzle = getPuzzle()
            wordMath = userInputPuzzle[1:] #gets the word math puzzle part 
                                            #from the user input in getPuzzle
            maxDigit = int(userInputPuzzle[0]) #gets the max digit from the 
                                                    # user input in getPuzzle 
            print
            print 'Date: ' + '.' * 30 + time.ctime()
            print
            solvePuzzle(wordMath, maxDigit)
            print
            print 'Date: ' + '.' * 30 + time.ctime()
        
        code = menu(PUZZLES)
            
    theEnd()


#**********************************************************************getPuzzle
def getPuzzle() :
    """Returns a puzzle acquired from the user in the format of the puzzles in 
    PUZZLE."""
    warning = "\n" #newline; no effect here
    userInputPuzzle = raw_input('Enter a word math puzzle:' + warning)

    while len(warning) > 0 :
    #warning: what was wrong last time
        warning = ""
        if '==' not in userInputPuzzle :
            print
            warning += "Puzzle '%s' does not contain '=='" % userInputPuzzle
            print warning
            userInputPuzzle = raw_input('Enter a word math puzzle:\n')
        
        if len(lettersIn(userInputPuzzle)) > 10 :
        #puzzle can't have more than 10 letters since there are only 10 digits
            print
            warning += ("Puzzle '%s' contains more than 10 letters" % 
                                                                userInputPuzzle)
            print warning
            userInputPuzzle = raw_input('Enter a word math puzzle:\n')
    
    userInputMaxNum = raw_input('What is the largest digit allowed?\n').strip()
    userInputMaxNum.strip().upper()
    
    warning = "\n" #newline; no effect here
    
    while len(warning) > 0 :
    #warning: what was wrong last time
        warning = ""
        if len(userInputMaxNum) > 1 :
            print
            warning += "Num '%s' must be between 0 and 9" % userInputMaxNum
            print warning
            userInputMaxNum = raw_input('What is the largest digit allowed?\n')
            userInputMaxNum.strip()
        
        elif '0' > userInputMaxNum > '9' :
            print
            warning += ("Number '%s' must be an interger between 0 and 9" %
                                                                userInputMaxNum)
            print warning
            userInputMaxNum = raw_input('What is the largest digit allowed?\n')
            userInputMaxNum.strip()
        
        userInputMaxNum = int(userInputMaxNum)
             
        if userInputMaxNum + 1 < int(len(lettersIn(userInputPuzzle))) :
        #the largest digit + 1 must be at least as big as the number of distinct 
        #letters in the puzzle
            print
            warning += ("Largest digit '%d' + 1 must be at least as big as " + 
            "the number of distinct letters in the puzzle") % userInputMaxNum
            print warning
            userInputMaxNum = raw_input('What is the largest digit allowed?\n')
            userInputMaxNum.strip()
    
    userPuzzle = "%d%s" % (userInputMaxNum, userInputPuzzle)
    return userPuzzle


#**********************************************************************lettersIn
def lettersIn(text) :
    """Returns an alpabetically sorted list of distinct letters in a string."""
    ALPHABET = string.ascii_uppercase #uppercase alphabet from string library
    text.upper()
    mySet = set(text).intersection(set(ALPHABET)) #gets distinct letters
    letters = sorted(mySet) #sorts letters in alphabetical order
    return letters


#********************************************************************listPuzzles
def menu(listPuzzles) :
    """Finds out from the user which one of the puzzles in listPuzzles the user 
    wants."""
    print
    print "Enter the number of one of these puzzles (Q to quit):"
    print
    for puzz in range(9) :
        number = puzz 
        puzzle = listPuzzles[puzz][1:]
        limit = listPuzzles[puzz][0]
        print "%d. %s using digits from 0 to %s" % (number, puzzle, limit)
    print "%d. %s" % (9,listPuzzles[9][1:])

    warning = " " #blank; no effect here
    userInput = raw_input(ARROW + warning).strip().upper()
    
    while len(warning) > 0 : #warning: what was wrong last time
        warning = ""
        if len(userInput) > 1 :
            print
            warning += "You entered %s; enter a valid digit, or Q" % userInput
            print warning
            print
            print "Enter the number of one of these puzzles (Q to quit):"
            print
            for puzz in range(9) :
                number = puzz 
                puzzle = listPuzzles[puzz][1:]
                limit = listPuzzles[puzz][0]
                print ("%d. %s using digits from 0 to %s" % (number, puzzle, 
                                                                        limit))
            print "%d. %s" % (9,listPuzzles[9][1:])
            userInput = raw_input(ARROW + ' ').strip().upper()
        choice = userInput
    return choice


#*******************************************************************permutations
def permutations(NN) : #http://www.quickperm.org 
    """Returns a list of all the permutations of the digits from 0 to NN - 1."""                    
    a_ = ["%d" % num for num in range(NN)] #arbitrary List
    N_ = len(a_)
    P_ = np.array(range(N_ + 1))
    i_ = 1
    listOfPerms = []
    listOfPerms.append("".join(a_))
    
    while i_ < N_ :
        P_[i_] -= 1
        if i_ % 2 == 1 : #if i_ is odd
            j_ = P_[i_]
        else : #if i_ is even steven
            j_ = 0
        swap(a_, j_, i_)
        listOfPerms.append("".join(a_))
        i_ = 1
        while P_[i_] == 0 :
            P_[i_] = i_
            i_ += 1 
    return listOfPerms
                        

#********************************************************************solvePuzzle                        
def solvePuzzle(wordMath, maxDigit) :
    """finds and print all solutions to the given word math puzzle."""
    letters = lettersIn(wordMath)
    perms = permutations(maxDigit + 1)
    solutionPermutations = []
    solutions = []
    
    print "Solving the puzzle:  %s"  % wordMath
    print "Calulating permutations of %d items; please wait ..."%(maxDigit + 1)
    print "PUZZLE:   %s" % wordMath
    
    for perm in perms :
        puzzle = wordMath
        for pos in range(len(letters)):
            puzzle = puzzle.replace(letters[pos],perm[pos])
        puzzle = " %s" % puzzle #checks for leading zero 
        
        if (' 0' not in puzzle) and ('==0' not in puzzle) :
             if eval(puzzle) :
                puzzle.strip
                solutionPermutations.append(perm)
                
                if puzzle not in solutions : #ensures same solution isn't 
                                                    #printed out more than once
                    solutions.append(puzzle)
                    print "SOLUTION:%s" % puzzle           
    return solutionPermutations
    
    
#***************************************************************************swap   
def swap(aList, pos0, pos1) :
    """Swaps position of two entries in a list."""
    aList[pos0], aList[pos1] = aList[pos1], aList[pos0]
    

#*************************************************************************theEnd
def theEnd() :
    """Prints termination output."""
    print "\nProgramed by Richard Salas Chavez"
    print "Date:", time.ctime()
    print "End of processing"  


main() # required call to start the program
