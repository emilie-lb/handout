import os
import unittest

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'test_planning.log')

class BasicTest(unittest.TestCase):
    """Basic test cases."""

    # à voir pour tester ouverture du fichier.log (à adapter)
    def setUp(self):
       self.testdata = open(TESTDATA_FILENAME).read()

    def test_intermediaire(self):
        self.assertEqual(intermediaire("12:30-12:45 Dictionaries"), "Dictionaries               15 minutes  100%"  )


    def test_final(self):
        self.assertEqual(final(TESTDATA_FILENAME),  )



if __name__ == '__main__':
    unittest.main()

