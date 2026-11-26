import unittest
from countunit import (value, from_pesos, normalize, add, compare, convert,
                       count_pile, check_coins, fmt)


class TestCountUnit(unittest.TestCase):
    def test_value(self):
        self.assertEqual(value(125, 713), 1338)

    def test_normalize(self):
        self.assertEqual(normalize(125, 713), (267, 3))

    def test_from_pesos(self):
        self.assertEqual(from_pesos(489), (97, 4))

    def test_add(self):
        self.assertEqual(add((125, 713), (3, 400)), (350, 3))
        self.assertEqual(value(350, 3), 1753)

    def test_compare(self):
        self.assertEqual(compare((267, 3), (266, 4)), 1)
        self.assertEqual(compare((125, 713), (267, 3)), 0)

    def test_convert(self):
        self.assertEqual(convert(125, 713, 5, 10), (133, 8))
        self.assertEqual(convert(0, 20_837_147, 1, 1000), (20837, 147))
        self.assertEqual(convert(5625, 1, 5, 100), (281, 26))
        self.assertEqual(convert(5625, 1, 5, 1000), (28, 126))

    def test_count_pile(self):
        pile = {5: 3, 10: 2, 100: 1, 1: 4}
        self.assertEqual(count_pile(pile), (27, 4))
        self.assertEqual(value(*count_pile(pile)), 139)

    def test_pooling_example(self):
        slips = [(631, 20), (527, 32), (1307, 35), (757, 37), (1025, 34), (1342, 23)]
        total = (0, 0)
        for s in slips:
            total = add(total, s)
        self.assertEqual(total, (5625, 1))
        self.assertEqual(value(*total), 28126)

    def test_check_coins(self):
        self.assertTrue(check_coins(22, 7267))
        self.assertFalse(check_coins(52, 11459))

    def test_chaining(self):
        direct = convert(267, 3, 5, 100)
        via = convert(*convert(267, 3, 5, 10), 10, 100)
        self.assertEqual(direct, via)

    def test_roundtrip(self):
        W, L = convert(*convert(267, 3, 5, 10), 10, 5)
        self.assertEqual(value(W, L), 1338)

    def test_fmt(self):
        self.assertEqual(fmt(267, 3), "267 ₱₅ 3")
        self.assertEqual(fmt(28, 126, 1000), "28 ₱₁₀₀₀ 126")


if __name__ == "__main__":
    unittest.main()
