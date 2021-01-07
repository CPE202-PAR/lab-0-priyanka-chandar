import unittest
from planets import weight_on_planets

# Write more test cases!

class Test_planets(unittest.TestCase):

    def test_mars(self) -> None:
        weight_1 = 136
        self.assertAlmostEqual(weight_on_planets(weight_1, "Mars"), 51.68)
        weight_2 = 119
        self.assertAlmostEqual(weight_on_planets(weight_2,"Mars"), 45.22)
        weight_3 = 234
        self.assertAlmostEqual(weight_on_planets(weight_3,"Mars"), 88.92)

    def test_jupiter(self) -> None:
        weight_1 = 136
        self.assertAlmostEqual(weight_on_planets(weight_1,"Jupiter"), 318.24)
        weight_2 = 119
        self.assertAlmostEqual(weight_on_planets(weight_2,"Jupiter"), 278.46)
        weight_3 = 234
        self.assertAlmostEqual(weight_on_planets(weight_3,"Jupiter"), 547.56)

    def test_venus(self) -> None:
        weight_1 = 136
        self.assertAlmostEqual(weight_on_planets(weight_1,"Venus"), 123.76)
        weight_2 = 119
        self.assertAlmostEqual(weight_on_planets(weight_2,"Venus"), 108.29)
        weight_3 = 234
        self.assertAlmostEqual(weight_on_planets(weight_3,"Venus"), 212.94)

    def test_error(self) -> None:
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            weight = 99
            weight_on_planets(weight,"Neptune")

if __name__ == "__main__":
        unittest.main()
