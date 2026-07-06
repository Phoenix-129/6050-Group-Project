#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: [date here]
@Author: [Phoenix A., Griffin B., Wyatt G., Courtney K., Kristi P]
@Course: INF 6050
@University: Wayne State University
@Assignment: [Group Project]
    
@Python Version: 3.8x   
@Required Modules: [any required modules]
    
@Description: [code description - what does this accomplish?]
"""
<<<<<<< Updated upstream
=======
# 7-5-26 GB. Added global variables for putting data into
import census
import us

from census import Census
from us import states

c = Census("3f2ba2143b0d33ef1ceec3c75c4090499c59c5a6")
print(c.acs5.state_county(('NAME','B25034_010E'),states.AK.fips, '170'))




>>>>>>> Stashed changes
########################### 
# GLOBAL VARIABLES
###########################
# variable for population with less than 9th grade education 
nNithGradeEd = 0  # DP02_0060E table
#  variable for non-institutionalised civilian population with disabilities
nDisabledPop = 0  # DP02_0072E table
# variable for households that have access to internet or computers
nHouseWTech = 0  # DP02_0153E and 0154E tables
# variable for people over 16 who are unemployed
nUnemployed = 0  # DP03_0109E table
# variable for household median income
medianHouseIncome = 0  # B10010_001E table
# variable for people without healthcare
nWithoutHealthcare = 0  # DP03_0099E table
# variable for people below the poverty line
nPopBelowPov = 0  # DP03_0119E through DP03_0137E tables
# variable for people without vehicles
nPopNoCar = 0  # DP04_0058E or B08014 tables
# variable for person living in own house, not rented
nHouseOwners = 0  # B25011_002E table
# variable for households living on benefits like SSI or food stamps
nHouseGovBen = 0  # B09010_002E table


########################### 
# USER-DEFINED FUNCTIONS
###########################


########################### 
# SCRIPT HERE
###########################
