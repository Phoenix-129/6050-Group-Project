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
import census
import us

from census import Census
from us import states

c = Census("3f2ba2143b0d33ef1ceec3c75c4090499c59c5a6")
print(c.acs5.state_county(('NAME','B25034_010E'),states.AK.fips, '170'))




########################### 
# GLOBAL VARIABLES
###########################


########################### 
# USER-DEFINED FUNCTIONS
###########################


########################### 
# SCRIPT HERE
###########################
