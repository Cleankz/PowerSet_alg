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
        for i in range(10000):
            s.put(random.randint(1,20000))
        sets = PowerSet()
        s.union(sets)
        self.assertTrue( s.size() <= 20000 )
        for j in range(10000):
            sets.put(random.randint(1,20000))
        s.union(sets)
        sz = s.size()
        self.assertTrue( sz > 200 )

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
        self.assertTrue (dif.size() <= s.size())

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
