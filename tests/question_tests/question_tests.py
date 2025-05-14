#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_d.question_d import get_most_likely_ancestor_consensus, test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_most_likely_ancestor_consensus ():
        
     pos1, pos2, pos3 = get_most_likely_ancestor_consensus ('GATATATGCATATACT", "ATAT')

     assert (pos1, pos2, pos3 )== (2,4,10), f"Expected (2, 4, 10), got ({pos1}, {pos2}, {pos3})"
                
    test_get_most_likely_ancestor_consensus()
    print ("test completed")


