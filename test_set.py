import unittest
from ps_alg import PowerSet
import random


class MyTests(unittest.TestCase):

    def test_put(self):
        s = PowerSet()
        for i in range(20000):
            s.put(random.randint(1,20000))
        self.assertTrue(20000 >= s.size())

    def test_remove(self):
        s = PowerSet()
        for i in range(20000):
            s.put(random.randint(1,20000))
        size = s.size()
        for i in range(20000):
            s.remove(random.randint(1,20000))
        self.assertTrue(s.size() < size)

    def test_intersection(self):
        s = PowerSet()
        sets = PowerSet()
        set_result = s.intersection(sets)
        for i in range(20000):
            s.put(i)

        set_result = s.intersection(sets)

        for i in range(20000):
            sets.put(i)
        set_result = s.intersection(sets)
        self.assertNotEqual([],set_result)

    def test_union(self):
        s = PowerSet()
        sets = PowerSet()
        self.assertEqual(s.size(), s.union(sets).size()) # проверяем что при объединении пустых множеств, размер не изменился
        for i in range(10000):
            s.put(random.randint(1,20000))

        self.assertEqual(s.size(), s.union(sets).size())# проверяем что при объединении пустого и не пустого множества, размер не изменился
        self.assertNotEqual(s, s.union(sets)) # проверяем что при объединении возврщается то же самое множество
        for j in range(10000):
            sets.put(random.randint(20000, 30000))
        self.assertTrue(s.size() < s.union(sets).size())# проверяем что произошло объединение
        self.assertTrue(s.union(sets).size() <= 18000)# проверяем что произошло объединение
        

    def test_difference(self):
        s = PowerSet()
        for i in range(20000):
            s.put(random.randint(1,20000))
        sets = PowerSet()
        s.difference(sets)
        self.assertTrue(sets.size() < s.size())
        for j in range(20000):
            sets.put(random.randint(1,20000))
        dif = s.difference(sets)
        self.assertTrue(dif.size() <= s.size())

    def test_issubset(self):
        s = PowerSet()
        sets = PowerSet()
        for i in range(20):
            s.put(i)
        for j in range(20):
            sets.put(j)
        self.assertTrue(s.issubset(sets))


if __name__ == '__main__':
    unittest.main()
