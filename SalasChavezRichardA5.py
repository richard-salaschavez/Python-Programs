"""RichardSalasChavezA5Q1

COMP 1012 SECTION A01
INSTRUCTOR Terry Andres
ASSIGNMENT: A5 Question 1
AUTHOR Richard Salas Chavez
VERSION March 17, 2015

PURPOSE: perform calculations using the numpy library
"""

#imports
import time
import math
import numpy as np


#***************************************************************************main
def main() :
    """Where main program resides."""
    print "PROPERTIES OF SOLIDS OF REVOLUTION"
    print
    HEADING = "Select a solid of revolution to analyze:"
    CHOICES = ("earth: evaluate properties of the planet earth:",
               "bowlingPin: evaluate attributes of a bowling pin",
               "saucePan: evaluate size of the inside of a sauce pan")
    STOP_CODE =  "Q"
    
    code = getChoice(HEADING, CHOICES, STOP_CODE) #print out table of choices and gets the user choice 
    
    while code != STOP_CODE :
        #valid input requiring processing
        CHOICE = CHOICES[code]
        FNC_NAME = CHOICE.split(":")[0]
        MIN_POINTS = 5 #given
        MAX_POINTS = 5120 #given
        
        analyzeSolid(FNC_NAME, MIN_POINTS, MAX_POINTS) 
        
        code = getChoice(HEADING, CHOICES, STOP_CODE)
            
    theEnd()


#*******************************************************************analyzeSolid
def analyzeSolid(fncName, minPoints, maxPoints) :
    """" put description here """
    silhouetteFnc = eval(fncName)
    UNITS = silhouetteFnc(0)[0] #argument has no effect since we are only looking for the unit
    VERT = "|" #vertical line
    HORZ = "-" #horizontal line
    CONN = "+" #connection
    
    HEADING = ("%7s%18s%7s%15s" % (VERT, "SILHOUETTE", VERT, "SOLID") + "\n" +
               " # OF %s %10s %8s %4s %9s %11s" % (VERT, "PERIMETER", "AREA", VERT, "SURFACE", "VOLUME") + "\n" +
               "POINTS" + VERT + "%9s %11s %3s %9s %11s" % ("["+UNITS+"]", "["+UNITS+"^2]", VERT, "["+UNITS+"^2]", "["+UNITS+"^3]") + "\n" +
               (HORZ * 6) + CONN + (HORZ * 24) + CONN + (HORZ * 24))
    print HEADING           
    numOfRows = int(math.ceil((math.log(maxPoints) + 1) / (math.log(minPoints * 2)))) * 2 #why doesn't dis work?
    
    for point in range(numOfRows) :
        numOfPoints = minPoints * 2 ** point
        xs = silhouetteFnc(numOfPoints)[1]
        ys =  silhouetteFnc(numOfPoints)[2]
        solidsInfo = solidSizes(xs,ys)
        perimeter = solidsInfo[0]
        area = solidsInfo[1]
        surface = solidsInfo[2]
        volume = solidsInfo[3]
        print "%5d %s %9.5g %11.5g %2s %10.5g %11.5g" % (numOfPoints, VERT, perimeter, area, VERT, surface, volume)
    print
    

#*********************************************************************bowlingPin
def bowlingPin(numPoints) :
    """represents a 15-inch bowling pin """
    xs = np.linspace(0, 15, numPoints)
    
    coefficients = [1.27731344, 0.85418707, 0.032282353, 0.127018447, 
                    -5.1957538e-2, 6.718114e-3, -3.61828e-4, 7.025e-6]
    
    ys = np.sqrt(evalPoly(coefficients, xs))
    
    UNIT = 'in'
    
    return (UNIT, xs , ys)


#***********************************************************************evalPoly
def evalPoly(poly, xx) : #from notes with slight modification 
    """Evaluate at xx a polynomial with coefficients in poly."""
    result = 0.0
    for coef in poly[-1::-1] :
        result = result * xx + coef
    return result 


#**************************************************************************earth
def earth(numPoints) :
    RADIUS = 6371 #[km]
    xs = np.linspace(-RADIUS, RADIUS, numPoints)
    ys = np.sqrt(RADIUS ** 2 - xs ** 2)
    UNIT = 'km'
    
    return (UNIT, xs, ys)

#**********************************************************************getChoice
def getChoice(heading, choices, stopCode) :
    """General menu function that returns user choice."""
    print heading
    for num, choice in enumerate(choices) :
        print "%d) %s" % (num, choice) 
    
    prompt = "Enter a choice number or enter Q to quit"
    warning = "\n" #newline character; no effect here
    userInput = raw_input(prompt + warning).strip()
    maxNum = len(choices) - 1
    
    if userInput.upper() == stopCode :
        choice = userInput.upper()
        
    else :
        while len(warning) > 0 : #warning: what was wrong last time
            warning = ""
            if len(userInput) > 1 :
                print
                warning += "You entered %s; enter a number from %d to %d, or Q" % (userInput, 0, maxNum)
                print warning
                print
                print heading
                for num, choice in enumerate(choices) :
                    print "%d) %s" % (num, choice)
              
                userInput = raw_input(prompt + '\n').strip()
                
            if userInput > str(maxNum) :
                print
                warning += "You entered %s; enter a number from %d to %d, or Q" % (userInput, 0, maxNum)
                print warning
                print
                print heading
                for num, choice in enumerate(choices) :
                    print "%d) %s" % (num, choice)
                
                userInput = raw_input(prompt + '\n').strip()
        choice = int(userInput)
    return choice


#***********************************************************************saucePan
def saucePan(numPoints) :
    R_PAN = 8.7 #[cm] radius of pan
    R_BASE = 1.5 #[cm] radius of base
    H_ = 8.5 #[cm] thickness
    R_LIP = 0.8 #[cm] radius of lip
    
    xs, ys = np.linspace(0, H_, numPoints), np.zeros(numPoints)
    
    ys += R_PAN
    
    btmCurve = (xs < R_BASE)
    ys[btmCurve] = (R_PAN - R_BASE + np.sqrt(xs[btmCurve] * (2 * R_BASE - xs[btmCurve])))
    
    topCurve = (xs >= H_ - R_LIP) 
    ys[topCurve] = (R_PAN + R_LIP - np.sqrt((R_LIP ** 2) - (H_ - R_LIP - xs[topCurve]) ** 2))
    
    UNIT = 'cm'
    
    return (UNIT, xs , ys)
    
    
#*********************************************************************solidSizes
def solidSizes(xs, ys) : 
    listXs = list(xs)
    listYs = list(ys)
    listXs.insert(0, xs[0])
    listYs.insert(0, 0)
    listXs.append(xs[-1])
    listYs.append(0)
    xs = np.array(listXs)
    ys = np.array(listYs)
    
    perimeter = np.sum(np.sqrt((xs[1:] - xs [:-1]) ** 2 + (ys[1:] - ys [:-1]) ** 2))
    
    areaUnderCurve = np.sum(0.5 * ((xs[1:] - xs [:-1]) * (ys[1:] + ys [:-1])))
    
    areaOfSolid = math.pi * np.sum((ys[1:] + ys [:-1]) * np.sqrt((xs[1:] - xs [:-1]) ** 2 + (ys[1:] - ys [:-1]) ** 2))
    
    volOfSolid = (math.pi / 4) * np.sum((xs[1:] - xs [:-1]) * (ys[1:] + ys [:-1]) ** 2)
    
    return (perimeter, areaUnderCurve, areaOfSolid, volOfSolid)
    
    
#*************************************************************************theEnd
def theEnd() :
    """Prints termination output."""
    print "\nProgramed by Richard Salas Chavez"
    print "Date:", time.ctime()
    print "End of processing"  


main() # required call to start the program
