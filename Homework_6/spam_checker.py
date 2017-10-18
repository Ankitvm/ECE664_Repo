#!/usr/bin/env python

#-------------------------------------------------------------------------------
""" spam_filter.py: Program to identify the word 'diagra' and its variants as spam """

__author__      = "Ankit Manerikar"
__copyright__   = "Copyright (C) 2017, course homework - ECE 664 (Purdue)"
__date__        = "17 October, 2017"
__credits__     = ["Ankit Manerikar"]
__license__     = "Public Domain"
__version__     = "1.0"
__maintainer__  = "Ankit Manerikar"
__email__       = "amanerik@purdue.edu"
__status__      = "Prototype"
#-------------------------------------------------------------------------------

import time
import re
import os, argparse
import numpy as np

def check_spam_words(input_line):
    spam_pattern =    r'^\s*d\s*([.]{,4}|[-]{,4})?\s*' + \
                           'i\s*([.]{,4}|[-]{,4})?\s*' + \
                           'a\s*([.]{,4}|[-]{,4})?\s*' + \
                           'g\s*([.]{,4}|[-]{,4})?\s*' + \
                           'r\s*([.]{,4}|[-]{,4})?\s*' + \
                           'a\s*$'

    if re.match(spam_pattern, input_line) == None:
        return ['No Spam Keywords Detected.', False]
    else:
        return ['Spam Keywords Detected!', True]

def get_sys_args():
    
    parser = argparse.ArgumentParser(description='Spam Checker Program')    
    parser.add_argument('--file', metavar='DIR',
                        default='./sample_text.txt',
                        help='path to the text file to be checked for spam')
    args = parser.parse_args()
    
    return args.file

if __name__ == "__main__":

    text_file_loc = get_sys_args()
    print '====================================================================='
    print 'Spam-Checking Program - Homework 7 (ECE 664)'
    print '---------------------------------------------------------------------'
    print 'Written by: ', __author__
    print 'Date Created: ', __date__
    print 'Program Start Time:', time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
    print '---------------------------------------------------------------------\n'

    print 'Checking for spam keywords in message file', text_file_loc,'...\n'

    print 'Checking message text line-wise ...'
    with open(text_file_loc,'r') as currfile:
        message_data = currfile.read().splitlines()
        ctr = 1
        spam_flag_list = []
        
        for msgline in message_data:
            [result_text, spamflag] = check_spam_words(msgline)
            if spamflag:
                print_line = '\tDetected Spam: '+msgline
            else:
                print_line = ''
            print 'Line ',ctr,':\tResult:  ', result_text, print_line
            spam_flag_list.append(spamflag)
            ctr +=1


    print '\n\nFinal Result:'

    if any(spam_flag_list):
        print 'Current Message suspected as Spam'
    else:
        print 'Current Message is not found to be Spam'
    print '\n====================================================================='
            
        
    
