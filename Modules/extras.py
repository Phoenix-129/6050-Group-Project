#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:01:21 2026
@Assignment: Group Project
@Python version: 3.13.9
@Description: User-built module for INF6050 Group Project
"""
# 7-14-26 GB. Added linebreak,goodbye, and repeat functions

def lineBreak():  # adds linebreak with spaces on either side
    print('\n')
    print('-'*15)
    print('\n')
def goodbye():  # adds standardized goodbye
    print('The program will now close. Goodbye!')
def goAgain():  # adds loop to ask user if they want to repeat program
    global Again  # variable for setting program loop
    replayAsk = True
    while replayAsk == True:
        Again = input('\nDo you want to repeat your previous actions? y/n ')
        Again = str.lower(Again) # for accuracy
        Again = str.strip(Again) # for accuracy
        if Again == 'y':
            Again = True  # starts program loop over
            replayAsk = False  # ends ask loop
        elif Again == 'n': 
            Again = False  # ends program loop
            replayAsk = False  # ends ask loop
        else:  # check for invalid answers
            print('\nSorry, that answer is invalid. Can you try again?\n')
