import os
import unittest

from parse_log import delai_min, create_delai_list, temps_total, create_dico_delai, liste_lignes_export

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'planning.log')


class TestBasic(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.testdata = open(TESTDATA_FILENAME).read()
        self.dict_delai = {"test1": 55, "test2": 15, "test3": 20}
        self.dict_delai2 = {"test1": 40, "test2": 205}
        self.liste_delai = [[40, "test1"], [100, "test2"], [105, "test2"]]
        self.total = 245

    # à voir pour tester ouverture du fichier.log (à adapter)
    # def open_log_file(path):

    def test_delai_min(self):
        self.assertEqual(delai_min("09:20-11:00 Introduction"), 100)
        self.assertEqual(delai_min("12:30-12:45 Dictionaries"), 15)
        self.assertIsInstance(delai_min("10:30-10:50 Break"), int)

    def test_create_delai_list(self):
        self.assertEqual(create_delai_list("09:20-11:00 Introduction"), [100, "Introduction"])
        self.assertEqual(create_delai_list("11:35-12:30 Numbers and strings"), [55, "Numbers and strings"])
        self.assertIsInstance(create_delai_list("11:35-12:30 Numbers and strings"), list)
        self.assertIsNotNone(create_delai_list("11:35-12:30 Numbers and strings"))

    def test_create_dico_delai(self):
        self.assertEqual(create_dico_delai(self.liste_delai), {"test1": 40, "test2": 205})
        self.assertIsInstance(create_dico_delai(self.liste_delai), dict)
        self.assertEqual(create_dico_delai([]), {})

    def test_temps_total(self):
        self.assertEqual(temps_total(self.dict_delai), 90)
        self.assertIsInstance(temps_total(self.dict_delai), int)
        self.assertIsNotNone(temps_total(self.dict_delai))

    def test_liste_lignes_export(self):
        self.assertEqual(liste_lignes_export(self.dict_delai2, self.total), 
        ["test1                      40 minutes   16%",
         "test2                     205 minutes   83%"])
        self.assertNotEqual(liste_lignes_export(self.dict_delai2, self.total), 
        ["test1             40 minutes   16%",
         "test2            205 minutes   83%"])
         self.assertIsInstance(liste_lignes_export(self.dict_delai2, self.total), list)
         
    # def test_write_file(self):


if __name__ == '__main__':
    unittest.main()