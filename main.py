"""
@author: Habbab
"""
import argparse
from utils import *
import sys
from algo import *

ap = argparse.ArgumentParser()

ap.add_argument("-a", "--seq1", required=True, help="first sequence input file")



ap.add_argument("-b", "--seq2", required=True, help="second sequence input file")

ap.add_argument("-c", "--config", required=True, help = "config file")

args = vars(ap.parse_args())
sequence1File = args['seq1']
sequence2File = args['seq2']
configFile = args['config']
parse_config(configFile)

seq1 = get_sequence(sequence1File)
seq2 = get_sequence(sequence2File)
table = init_table(seq1, seq2)
table = Needleman_Wunsch(table, seq1, seq2)
n = len(table)
m = len(table[0])
trace_path(table, seq1, seq2, n - 1, m - 1)

number_of_paths = len(all_alignmentsB)

outputFile = open('result.txt', 'w')

outputFile.write('Score = ' + str(table[n-1][m-1]) + '\n' + '----------------------------------\n')

if number_of_paths-1 > config.MAX_NUMBER_PATHS:
    print('Number of possible alignments exceded the maximum number of paths specified in config.txt')

for i in range(1, number_of_paths):
    all_alignmentsA[i].reverse()
    all_alignmentsB[i].reverse()
    outputFile.write(''.join(map(str, all_alignmentsA[i])) + '\n')
    outputFile.write(''.join(map(str, all_alignmentsB[i])) + '\n')
    outputFile.write('----------------------------------\n')
outputFile.close()
