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
#7-14-26 GB. Added user-made module, created introduction to program

#non-standard modules needed for this 
import census
import us
#user made modules
import format
#specific aspects needed from modules
from census import Census
c = Census("3f2ba2143b0d33ef1ceec3c75c4090499c59c5a6")


########################### 
# GLOBAL VARIABLES
###########################

# i reorganzied the varaibles so they were seperated by ACS5DP and ACS5
# also for some of them i reduced the ammount of variables we were pulling 
# having found clearer data during testing (Poverty pop)

# variable for population with less than 9th grade education 
NumNinthGradeEd = 0  # DP02_0060E table

#  variable for non-institutionalised civilian population with disabilities
NumDisabledPop = 0  # DP02_0072E table

# variable for households that have access to internet or computers
NumHouseWTech = 0  # DP02_0153E and 0154E tables

# variable for people over 16 who are unemployed
NumUnemployed = 0  # DP03_0109E table

# variable for people without healthcare
NumWithoutHealthcare = 0  # DP03_0099E table

# variable for people without vehicles
NumPopNoCar = 0  # DP04_0058E table

# variable for household median income
MedianHouseIncome = 0  # B10010_001E table

#variable for people below the poverty line
NumPopBelowPov = 0  # B16009_002E table

# variable for person living in own house, not rented
NumHouseOwners = 0  # B25011_002E table

# variable for households living on benefits like SSI or food stamps
NumHouseGovBen = 0  # B09010_002E table

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

########################### 
# USER-DEFINED FUNCTIONS
###########################

#searches ACS5DP for the data ass. with the set location
DataDP = c.acs5dp.state_county(FieldDP,StateFip,CountyFip)
#searches ACS5 for the data ass. with the set location
Data = c.acs5.state_county(Field,StateFip,CountyFip)

def AskPlaceInfo():  # asks user for state and county fip codes
     AskLoop = True  # set variable for state loop
     while AskLoop == True:  # set loop asking for state fip
        try:
            global StateFip  # call variable for user input
            # asks for user's chosen state
            StateFip = print('What state(s) are you looking at? ')
            StateFip = str.strip(StateFip)  # strip whitespace
            StateFip = int(StateFip)  # make integer
            AskLoop = False  # end loop
        except:  # checks for non-integer input
            print('Sorry, your answer needs to be an integer.')
            continue  # repeats question
    AskLoop2 = True  # set variable for county loop
    while AskLoop2 == True:  # set loop asking for county fip
        try:
            global CountyFip   # call variable for user input
            # asks for user's chosen county
            CountyFip = print('What county/counties are you looking at? ')
            CountyFip = str.strip(CountyFip)  # strip whitespace
            CountyFip = int(CountyFip)  # make integer
            AskLoop2 = False  # end loop
        except:  # checks for non-integer input
            print('Sorry, your answer needs to be an integer.')
            continue  # repeats question

# add function here for asking for what kind of info they want. give menu options 

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
lineBreak()  # calls linebreak for spacing
print("First, let's choose a state and county.")  # intros next step
AskPlaceInfo()  # calls function for asking for state/county fip codes

# add some code about what data user wants to look at and filter to just that


