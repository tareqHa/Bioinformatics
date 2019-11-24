"""
@author: Habbab
"""
import config
import sys
import argparse

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

def parse_args():
    ap = argparse.ArgumentParser()

    ap.add_argument("-a", "--seq1", required=True, help="first sequence input file")



    ap.add_argument("-b", "--seq2", required=True, help="second sequence input file")

    ap.add_argument("-c", "--config", required=True, help = "config file")

    args = vars(ap.parse_args())
    sequence1File = args['seq1']
    sequence2File = args['seq2']
    configFile = args['config']
    return sequence1File, sequence2File, configFile

def get_sequences(sequence1File, sequence2File):
    seq1 = get_sequence(sequence1File)
    seq2 = get_sequence(sequence2File)
    return seq1, seq2

def write_out_results(allAlignmentsA, allAlignmentsB, table, n, m):
    number_of_paths = len(allAlignmentsB)

    outputFile = open('result.txt', 'w')
    
    outputFile.write('Score = ' + str(table[n-1][m-1]) + '\n' + '----------------------------------\n')

    if number_of_paths-1 > config.MAX_NUMBER_PATHS:
        print('Number of possible alignments exceded the maximum number of paths specified in config.txt')

    for i in range(1, number_of_paths):
        allAlignmentsA[i].reverse()
        allAlignmentsB[i].reverse()
        outputFile.write(''.join(map(str, allAlignmentsA[i])) + '\n')
        outputFile.write(''.join(map(str, allAlignmentsB[i])) + '\n')
        outputFile.write('----------------------------------\n')
    outputFile.close()
