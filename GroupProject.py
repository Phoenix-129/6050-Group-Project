#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: [date here]
@Author: [Phoenix A., Griffin B., Wyatt G., Courtney K., Kristi P]
@Course: INF 6050
@University: Wayne State University
@Assignment: [Group Project]
    
@Python Version: 3.8x   
@Required Modules: [Census, Us, format]
    
@Description: [User can find census data for set socioeconomic info for state
               and county of their choice]
"""
# 7-5-26 GB. Added global variables for putting data into
# 7-9-26 PA. Added funtion to pull the data for the set census variables 
# from a changable state and county + made slight changes to global variables
# 7-14-26 GB. Added user-made module, created introduction to program
# 7-15-26 GB. Added user-input funtions and printed results


#non-standard modules needed for this 
import census
import us
#user made modules
import extras
#specific aspects needed from modules
from census import Census
c = Census("3f2ba2143b0d33ef1ceec3c75c4090499c59c5a6")


########################### 
# GLOBAL VARIABLES
###########################

# i reorganzied the varaibles so they were seperated by ACS5DP and ACS5
# also for some of them i reduced the ammount of variables we were pulling 
# having found clearer data during testing (Poverty pop)

# variable that allows user to chose which county based on fips code
CountyFip = 163 #currently autoset for testing (wayne) 

# state fip, if we want user to be able to search other states to we can have 
# this be changable as well 
StateFip = 26 #currently autoset for testing (michigan)

# tuple used to input census varaibles into function (ACS5DP)
FieldDP = ('NAME','DP02_0060E','DP02_0072E','DP02_0153E','DP02_0154E',
          'DP03_0109E','DP03_0099E', 'DP04_0058E')

# tuple used to input census vairables into function (ACS5)
Field = ('B10010_001E','B25011_002E','B09010_002E','B16009_002E')

#searches ACS5DP for the data ass. with the set location
DataDP = c.acs5dp.state_county(FieldDP,StateFip,CountyFip)
#searches ACS5 for the data ass. with the set location
Data = c.acs5.state_county(Field,StateFip,CountyFip)

DictDataDP = DataDP[0]  # makes list of dictionaries into 1 dictionary
DictData = Data[0]  # makes list of dictionaries into 1 dictionary

# variable for population with less than 9th grade education 
NumNinthGradeEd = DictDataDP['DP02_0060E']  # DP02_0060E table

#  variable for non-institutionalised civilian population with disabilities
NumDisabledPop = DictDataDP['DP02_0072E']  # DP02_0072E table

# variable for households that have access to internet or computers
# DP02_0153E and 0154E tables
NumHouseWTech = [DictDataDP['DP02_0153E'], DictDataDP['DP02_0154E']]  

# variable for people over 16 who are unemployed
NumUnemployed = DictDataDP['DP03_0109E']  # DP03_0109E table

# variable for people without healthcare
NumWithoutHealthcare = DictDataDP['DP03_0099E']  # DP03_0099E table

# variable for people without vehicles
NumPopNoCar = DictDataDP['DP04_0058E']  # DP04_0058E table

# variable for household median income
MedianHouseIncome = DictData['B10010_001E']  # B10010_001E table

#variable for people below the poverty line
NumPopBelowPov = DictData['B16009_002E']  # B16009_002E table

# variable for person living in own house, not rented
NumHouseOwners = DictData['B25011_002E']  # B25011_002E table

# variable for households living on benefits like SSI or food stamps
NumHouseGovBen = DictData['B09010_002E']  # B09010_002E table

DemoDict = {} # dictionary for holding data user wants to compare
CompareList = [] # list of dictionaries for if comparing multiple zipcodes

########################### 
# USER-DEFINED FUNCTIONS
###########################

def AskStateInfo():  # asks user for state fip codes
     AskLoop = True  # set variable for state loop
     while AskLoop == True:  # set loop asking for state fip
        try:
            global StateFip  # call variable for user input
            # asks for user's chosen state
            StateFip = print('What state(s) are you looking at? ')
            StateFip = str.strip(StateFip)  # strip whitespace
            StateFip = str.lower(StateFip)  # make lowercase for quit
            if StateFip == 'q':
                extras.goodbye()  # calls goodbye function
                break
            else:
                StateFip = int(StateFip)  # make integer
                AskLoop = False  # end loop
        except:  # checks for non-integer input
            print('Sorry, your answer needs to be an integer.')
            continue  # repeats question

def AskCountyInfo():  # asks user for county fip codes
     AskLoop2 = True  # set variable for county loop
     while AskLoop2 == True:  # set loop asking for county fip
        try:
            global CountyFip   # call variable for user input
            # asks for user's chosen county
            CountyFip = print('What county/counties are you looking at? ')
            CountyFip = str.strip(CountyFip)  # strip whitespace
            CountyFip = str.lower(CountyFip)  # makes lowercase for quit
            if CountyFip == 'q':
                extras.goodbye()  # calls goodbye function
                break 
            else:
                CountyFip = int(CountyFip)  # make integer
                AskLoop2 = False  # end loop
        except:  # checks for non-integer input
            print('Sorry, your answer needs to be an integer.')
            continue  # repeats question

# add function here for asking for what kind of info they want
def AskDemoInfo():
    # create menu of options
    print('You can choose up 5 of the following ten choices', end=' ')
    print('your data. They are:\n\tA. The median household', end=' ')
    print('income\n\tB. The number of the population below', end=' ')
    print('the poverty line\n\tC. The number of people who', end=' ')
    print('are unemployed\n\tD. The number of disabled', end=' ')
    print('people who are not institutionalized\n\tE. The', end=' ')
    print('number of people without healthcare\n\tF. The', end=' ')
    print('number of households without a vehicle\n\tG. The', end=' ')
    print('number of households on government benefits\n\t', end=' ')
    print('H. The number of households with computers or', end=' ')
    print('internet\n\tI. The number of people who live in', end=' ')
    print('their own homes\n\tJ. The number of people over', end=' ')
    print('over 25 who never finished 9th grade')
    Again = True  # create variable to control loop
    while Again == True:  # start ask loop
        try:
            global NumDisabledPop  # global variable for disability option
            global NumHouseGovBen  # global variable for benefits option
            global NumNinthGradeEd  # global variable for education option
            global NumHouseOwners  # global variable for homeowner option
            global NumHouseWTech  # global variable for technology option
            global NumUnemployed  # global variable for unemployment option
            # global variable for healthcare option
            global NumWithoutHealthcare  
            global NumPopNoCar  # global variable for vehical option
            global NumPopBelowPov  # global variable for poverty option
            global MedianHouseIncome  # global variable for income option
            global DemoDict  # calls dictionary for adding data values
            global CompareList  # calls list for adding results
            global UserInput  # global variable for user input 
            UserInput = input('What demographic data do you want to see? ')
            UserInput = str.lower(UserInput)  # makes lowercase
            UserInput = str.strip(UserInput)  # strips whitespace
            if UserInput == 'a':  # assigns data based on user input
                DemoDict['Median Income'] = [MedianHouseIncome]
                Again == False  # ends loop
            elif UserInput == 'b':
                DemoDict['Below Poverty Line'] = [NumPopBelowPov]
                Again == False  # ends loop
            elif UserInput == 'c':
                DemoDict['Unemployed'] = [NumUnemployed]
                Again == False  # ends loop
            elif UserInput == 'd':
                DemoDict['Disabled Population'] = [NumDisabledPop]
                Again == False  # ends loop
            elif UserInput == 'e':
                DemoDict['No Healthcare'] = [NumWithoutHealthcare]
                Again == False  # ends loop
            elif UserInput == 'f':
                DemoDict['No Vehicle'] = [NumPopNoCar]
                Again == False  # ends loop
            elif UserInput == 'g':
                DemoDict['On Benefits'] = [NumHouseGovBen]
                Again == False  # ends loop
            elif UserInput == 'h':
                DemoDict['Has Digital Access'] = [NumHouseWTech]
                Again == False  # ends loop
            elif UserInput == 'i':
                DemoDict['Owns a Home'] = [NumHouseOwners]
                Again == False  # ends loop
            elif UserInput == 'j':
                DemoDict['Unfinished Ninth Grade'] = [NumNinthGradeEd]
                Again == False  # ends loop
            else:  # checks for quit input
                UserInput == 'q'
                extras.goodbye()  # calls goodbye message
                break  # breaks loop
        except:  # checks for input errors
            print('Sorry, that answer is invalid. Please try again.')
            continue  # continues loop until correct answer
    CompareList.append(DemoDict)  # appends data to list for later
    extras.goAgain()  # asks about adding more data
            

# the information the user wants is paired with its census variable 
# nicly within the DataDP+Data dictionaries
# i was unsure how you planned to go about your input/outputs so i didnt 
# set up the variables in the nNinthGradeEd = DataDP['DP02_0072E'] manner
# in case that was not your plan

##########################
# SCRIPT HERE
##########################
# print introduction
print('Welcome to the Demographic Displayer for Decision-Making program.\n')
print('Here you can select which counties you want to look at and', end='')
print('what kind of demographic data you want to compare from each county.')
print('\nIf you need to quit, just type "q" without the quotes and', end=' ')
print('the program will exit.')

extras.lineBreak()  # calls linebreak for spacing

mainLoop = True  # variable for while loop

while mainLoop == True:  # start while loop for main program
    print("First, let's choose a state and county.")  # intros next step
    AskStateInfo()  # calls function for asking for state fip codes
    if StateFip == 'q':  # breaks loop if user input is quit
        break
    AskCountyInfo()  # calls function for asking for county fip codes
    if CountyFip == 'q':  # breaks loop if user input is quit
        break
    AskDemoInfo()  # calls function for asking for demographic data
    if UserInput == 'q':  # breaks loop if user input is quit
        break
    # asks if user wants to see results or add more data
    print('Are you ready for your results or would you like to', end=' ')
    print('compare them to another county?\n')
    ReadyResults = input('Press "y" for "yes, ready", or "n" for "not yet" ')
    ReadyResults = str.lower(ReadyResults)  # makes lowercase
    ReadyResults = str.strip(ReadyResults)  # strips whitespace
    if ReadyResults == 'y':
        FileCheck = input('\nSave the results to a csv file? y/n ')
        FileCheck = str.lower(FileCheck)  # makes lowercase
        FileCheck = str.strip(FileCheck)  # strips whitespace
        if FileCheck == 'y':
            # add function for saving to csv file -- Courtney
        elif FileCheck == 'n': 
            print(CompareList)
        elif FileCheck == 'q':  # check for quit
            extras.goodbye()
            break
        else:  # check for errors
            print('Sorry, that is not a valid answer. Please try again.')
    elif ReadyResults == 'n':  
        print(CompareList)  # prints list of dictionaries for user to see
        mainLoop = False
    elif ReadyResults == 'q':  # checks for quit
        extras.goodbye()
        break
    else:  # error check
        print('Sorry, that is not a valid answer. Please try again.')
    extras.goAgain()  # checks if user wants to do a new search
    if Again == True:  # new search is a go
        DemoDict.clear()  # clears dictionary for new data
        CompareList.clear()  # clears list for new data
        continue
    elif Again == False:
        extras.goodbye()  # prints goodbye message
        break  # breaks loop to end program



