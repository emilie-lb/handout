import os
import unittest

from parse_log import *

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'planning.log')


class TestBasic(unittest.TestCase):
    """Basic test cases."""

    # à voir pour tester ouverture du fichier.log (à adapter)
    def setUp(self):
       self.testdata = open(TESTDATA_FILENAME).read()
       self.dict_delai = {"test1":55, "test2":15, "test3":20}


    # def open_log_file(path):


    def test_delai_min(self):
        self.assertEqual(delai_min("09:20-11:00 Introduction"), 100)
        self.assertEqual(delai_min("12:30-12:45 Dictionaries"), 15)

    def test_create_delai_list(self):
        self.assertEqual(create_delai_list("09:20-11:00 Introduction"), [100, "Introduction"])
        self.assertEqual(create_delai_list("11:35-12:30 Numbers and strings"), [55, "Numbers and strings"])
        self.assertIsInstance(create_delai_list("11:35-12:30 Numbers and strings"), list)
        self.assertIsNotNone(create_delai_list("11:35-12:30 Numbers and strings"))

    def test_temps_total(self):
        self.assertEqual(temps_total(self.dict_delai), 90)
        self.assertIsInstance(temps_total(self.dict_delai), int)

    # def test_write_file(self):

    # def test_liste_lignes_export(self):
    
    # def test_create_dico_delai(self):
        # self.assertIsInstance(self.liste, dict)



if __name__ == '__main__':
    unittest.main()

