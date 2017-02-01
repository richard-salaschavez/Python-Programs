# -*- coding: utf-8 -*-
"""RichardSalasChavezA3Q1

COMP 1012 SECTION A01
INSTRUCTOR Terry Andres
ASSIGNMENT: A3 Question 1
AUTHOR Richard Salas Chavez
VERSION February 22, 2015

PURPOSE: Write a script that can print a full year’s calendar for any year from 1900 to 9999, using Excel dates, as 
described back in Assignment 1. 
"""

#imports
import time
import math

def calcExcelDate(year, month) :
    """Return the Excel Date for any year between 1900 to 9999."""
    day = 1
    y2 = year - 1900 
    em = math.floor((14 - month)/12) 
    y3 = y2 - em 
    m2 = month + 12 * em 
    l_ = (1 + min(y3, 0) + math.floor(y3/4) - math.floor(y3/100) +
        math.floor((y3 + 300)/400)) 
    d1 = math.floor(-1.63 + (m2 - 1) * 30.6) 
    d2 = day + y3 * 365 + l_ + d1
    excelDate = int(d2)
    return excelDate

def calcWeekDay(excelDate) :
    """Returns an int from 0 to 6 indicating which day of the week the Excel
    date refers to, where 0 designates Sunday, and 6 designates Saturday"""
    dayInWeek = (excelDate + 6) % 7 #since the day is assumed to be 1 we must
                                        #accomodate for this by adding 6.
    return dayInWeek

def daysInMonth(year, month) :
    """Returns the number of days in a given month using Excel dates.""" 
    numDays = calcExcelDate(year, month + 1) - calcExcelDate(year, month)
    return numDays 

def formatCalendar(monthDetail) :
    """Return a calendar layout for one month."""
    VERTICAL = U"\N{BOX DRAWINGS HEAVY VERTICAL}" #unicode for vertical line 
    TOP_LEFT = U"\N{BOX DRAWINGS HEAVY DOWN AND RIGHT}" 
    HORIZONTAL = U"\N{BOX DRAWINGS HEAVY HORIZONTAL}" 
    TOP_RIGHT = U"\N{BOX DRAWINGS HEAVY DOWN AND LEFT}"
    BOTTOM_LEFT = U"\N{BOX DRAWINGS HEAVY UP AND RIGHT}" 
    BOTTOM_RIGHT = U"\N{BOX DRAWINGS HEAVY UP AND LEFT}"
    NEW = '\n'
        
    DAYS = ' Sun  Mon  Tue  Wed  Thu  Fri  Sat  '  
    TOP = TOP_LEFT + HORIZONTAL * 18 + TOP_RIGHT
    BOTTOM = BOTTOM_LEFT + HORIZONTAL * 18 + BOTTOM_RIGHT 
             
    month = monthDetail[0] #name of month 
    days = monthDetail[1] #list of days in a specific month
    stringOfDays = VERTICAL + " "
    
    for num in range(42) :
        BLANK = " "
        stringOfDays += "%s" % days[num] + BLANK * 2 #converts list to string
        
        if(num > 0 and num % 7 == 6) :
        #starts a new row every seven entries
            stringOfDays += VERTICAL + NEW + (VERTICAL + BLANK) * (num < 41)
            
    formattedMonth = (TOP + NEW + VERTICAL + " %-35s" % month + VERTICAL + NEW
                    + VERTICAL + DAYS + VERTICAL + NEW + stringOfDays + BOTTOM)
      
    return formattedMonth
    
def listMonthDays(year) :
    """Return a list of data for each month."""
    MONTHS = (' ', 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
              'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER')
    STAR = U"\N{BLACK STAR}"
    monthDetails = range(13) #list with 12 items
    monthDetails[0] = year
    for month in range(1, 13) :
        excelDate = calcExcelDate(year, month) 
        dayInWeek = calcWeekDay(excelDate)
        listOfDays = ['   '] * 42
        days = range(1, int(daysInMonth(year, month))+1) #list of days in month

        for day in days :
            #converts list of number to list of strings
            listOfDays[dayInWeek + (day - 1)] = "%3d" % day#accounts for blanks 
        
        if month == 1 or month == 7 :
            #replaces ' 1’ by STAR + '1’.
            listOfDays[listOfDays.index('  1')] = '%s1' % STAR 
        
        monthDetails[month] = (MONTHS[month], listOfDays)
        
    return monthDetails

def theEnd( ) :
    """Prints termination output."""
    print "\nProgramed by Richard Salas Chavez"
    print "Date:", time.ctime()
    print "End of processing"   

YEAR = int(raw_input('input year: '))
monthDetails = listMonthDays(YEAR) 
print '%62d' % YEAR

for month in range(1, 13, 3) :
    left = formatCalendar(monthDetails[month]).split('\n')
    centre = formatCalendar(monthDetails[month+1]).split('\n')
    right = formatCalendar(monthDetails[month+2]).split('\n')
    for row in range(len(left)) :
        print "%s %s %s" % (left[row], centre[row], right[row])

theEnd( )
