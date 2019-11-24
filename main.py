"""
@author: Habbab
"""
import argparse
from utils import *
import sys
from algo import *


sequence1File, sequence2File, configFile = parse_args() # parse the arguments

parse_config(configFile)    # parse the config

seq1, seq2 = get_sequences(sequence1File, sequence2File)

table = init_table(seq1, seq2)  # initialize the table

table = Needleman_Wunsch(table, seq1, seq2) # fill the table with the algorithm

n = len(table)  # number of rows
m = len(table[0])   # number of columns

trace_path(table, seq1, seq2, n - 1, m - 1) # get all optimal paths

write_out_results(all_alignmentsA, all_alignmentsB, table, n, m) # write out the results to results.txt
