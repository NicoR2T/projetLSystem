#!/usr/bin/env python3
##############################################################
# Programme de test unitaire
# Fichier: testunitaire.py

import unittest
from Programme import *
class TestProjetL_System(unittest.TestCase):
    def testLecture(self):
   	  self.assertEqual(InitialisationLecture("Entrée"), None, "Le fichier existe")

    def testEcriture(self):
      self.assertEqual(InitialisationEcriture("Sortie"), None, "Le fichier s'est bien écrit")

    def testCroissance(self):
   	 self.assertEqual(croissance("a-a-a-a",0,0), "a-a-a-a", "Application de la règle au niveau 0")


if __name__ == '__main__':
    unittest.main()
