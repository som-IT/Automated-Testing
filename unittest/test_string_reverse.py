# test_string_reverse.py
import unittest
from string_reverse import reverse_words  

class TestStringOperations(unittest.TestCase):
    def test_reverse_words(self):
        sentence = "hello world"
        reversed_sentence = "olleh dlrow"
        self.assertEqual(reverse_words(sentence), reversed_sentence)

if __name__ == '__main__':
    unittest.main()
