# assert 3 * 8 == 24, "should be 24"


# def tco():
#     assert 3*4 == 12, "=12"


# def tct():
#     assert 3*4 == 12, "=12"


# if __name__ == "__main__":
#     tco()
#     tct()
#     print("o&t passed")
import unittest


class mytestcase(unittest.TestCase):

    def testone(self):
        self.assertTrue(100 < 101, "it's true ")

    def testtwo(self):
        self.assertEqual(50+33, 100, " it's 100 ")

    def testthree(self):
        self.assertGreater(100, 80, "it's ture ")


if __name__ == "__main__":
    unittest.main()
