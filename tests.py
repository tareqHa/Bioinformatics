import unittest
from algo import *
import config
class TestAlgorithmMethods(unittest.TestCase):

    def test_init_table(self):
        # GIVEN
        seq1 = "SM"
        seq2 = "MA"
        seq3 = "ACG"
        seq4 = "CGA"
        expected_table1 = [[0, -2, -4], [-2, 0, 0], [-4, 0, 0]]
        expected_table2 = [[0, -2, -4, -6], [-2, 0, 0, 0], [-4, 0, 0, 0], [-6, 0, 0, 0]]
        GP = -2
        SAME = 5
        DIFF = -5
        # run the method
        actual_table1 = init_table(seq1, seq2)
        actual_table2 = init_table(seq3, seq4)

        #assert
        self.assertEqual(expected_table1, actual_table1)
        self.assertEqual(expected_table2, actual_table2)
    
    def test_S(self):
        #GIVEN
        a = 1
        b = 2
        c = 2
        
        #run and assert
        self.assertEqual(config.DIFF, S(a, b))
        self.assertEqual(config.SAME, S(b, c))

    def test_Needleman_Wunsch(self):
        #GIVEN
        seq1 = "SM"
        seq2 = "MA"
        table = [[0, -2, -4], [-2, 0, 0], [-4, 0, 0]]
        expected_result = [[0, -2, -4], [-2, -4, -6], [-4, 3, 1]]
        GP = -2
        SAME = 5
        DIFF = -5
        # run the method
        actual_result = Needleman_Wunsch(table, seq1, seq2)
        self.assertEqual(expected_result, actual_result)

    def test_trace_path(self):
        #GIVEN
        seq1 = "SMART"
        seq2 = "MARS"
        table = [[0, -2, -4, -6, -8], [-2, -4, -6, -8, -1], [-4, 3, 1, -1, -3], [-6, 1, 8, 6, 4], [-8, -1, 6, 13, 11], [-10, -3, 4, 11, 9]]
        GP = -2
        SAME = 5
        DIFF = -5
        
        # run the method
        trace_path(table, seq1, seq2, len(table) - 1, len(table[0]) - 1)

        # assert
        self.assertEqual(len(all_alignmentsA) - 1, 2)
        self.assertEqual(len(all_alignmentsB) - 1, 2)
        for i in range(1, 3):
            all_alignmentsA[i].reverse()
            all_alignmentsB[i].reverse()

        self.assertEqual(''.join(map(str, all_alignmentsA[1])), "SMAR-T")
        self.assertEqual(''.join(map(str, all_alignmentsA[2])), "SMART-")
        self.assertEqual(''.join(map(str, all_alignmentsB[1])), "-MARS-")
        self.assertEqual(''.join(map(str, all_alignmentsB[2])), "-MAR-S")

if __name__ == '__main__':
    unittest.main()