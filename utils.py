"""
Created on Sat Nov 9 12:45:19 2019
@author: Habbab
"""
import config
import sys

def get_sequence(file):
    seq = open(file).read().strip(' \n')
    if len(seq) > config.MAX_SEQ_LENGTH:
        sys.exit('ERROR: Please enter a sequence which has length less than or equal the the one specified in config.txt')
    else:
        return seq

def parse_config(file):
    myvars = {}
    with open(file) as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            myvars[name.strip()] = int(var)
    config.GP = myvars['GP']
    config.DIFF = myvars['DIFF']
    config.SAME = myvars['SAME']
    config.MAX_NUMBER_PATHS = myvars['MAX_NUMBER_PATHS']
    config.MAX_SEQ_LENGTH = myvars['MAX_SEQ_LENGTH']
