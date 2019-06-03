import unittest
import doctest

testSuite = unittest.TestSuite()
# for mod in dict_functions, list_functions, string_functions, float_functions:
# 	testSuite.addTest(doctest.DocTestSuite(mod))
unittest.TextTestRunner().run(testSuite)
