import config
all_alignmentsA = [[]]
all_alignmentsB = [[]]
alignmentA = []
alignmentB = []

def init_table(seq1, seq2):
    n = len(seq1) + 1
    m = len(seq2) + 1
    table =[[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        table[i][0] = i * config.GP
    for i in range(m):
        table[0][i] = i * config.GP
    return table

def S(a, b):
    if a == b:
        return config.SAME
    else:
        return config.DIFF
def Needleman_Wunsch(table, A, B):
    n = len(table)
    m = len(table[0])

    for i in range(1, n):
        for j in range(1, m):
            match = table[i-1][j-1] + S(A[i-1], B[j-1])
            gap1 = table[i-1][j] + config.GP
            gap2 = table[i][j-1] + config.GP
            table[i][j] = max(match, gap1, gap2)
    return table

def trace_path(table, A, B, i, j):

    if i == 0 and j == 0:
        all_alignmentsA.append(alignmentA[:])
        all_alignmentsB.append(alignmentB[:])
        return
    if i > 0 and j > 0 and table[i][j] == table[i-1][j-1] + S(A[i-1], B[j-1]):
        alignmentA.append(A[i-1])
        alignmentB.append(B[j-1])
        trace_path(table, A, B, i-1, j-1)
        alignmentA.pop()
        alignmentB.pop()
    if i > 0 and table[i][j] == table[i-1][j] + config.GP:
        alignmentA.append(A[i-1])
        alignmentB.append('-')
        trace_path(table, A, B, i-1, j)
        alignmentA.pop()
        alignmentB.pop()
    if j > 0 and table[i][j] == table[i][j-1] + config.GP:
        alignmentA.append('-')
        alignmentB.append(B[j-1])
        trace_path(table, A, B, i, j-1)
        alignmentA.pop()
        alignmentB.pop()
    

