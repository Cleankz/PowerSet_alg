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
        for i in range(1000):
            s.remove(random.randint(1,20000))
        self.assertTrue(s.size() < size)

    def test_intersection(self):
        s = PowerSet()
        set = []
        set_result = s.intersection(set)
        self.assertEqual([],set_result)
        for i in range(200):
            s.put(i)

        set_result = s.intersection(set)
        self.assertEqual([],set_result)

        for i in range(20):
            set.append(i)
        set_result = s.intersection(set)
        self.assertNotEqual([],set_result)

    def test_union(self):
        s = PowerSet()
        for i in range(200):
            s.put(random.randint(1,20000))
        set = []
        s.union(set)
        self.assertTrue( s.size() <= 200 )
        for j in range(10):
            set.append(random.randint(1,20000))
        s.union(set)
        sz = s.size()
        self.assertTrue( sz > 200 )

    def test_difference(self):
        s = PowerSet()
        for i in range(20000):
            s.put(random.randint(1,20000))
        set = []
        self.assertTrue(len(s.difference(set)) == s.size())
        for j in range(20000):
            set.append(random.randint(1,20000))
        self.assertTrue(len(s.difference(set)) <= s.size())

    def test_issubset(self):
        s = PowerSet()
        set = []
        for i in range(20):
            s.put(i)
        for j in range(20):
            set.append(j)
        self.assertTrue(s.issubset(set))

if __name__ == '__main__':
    unittest.main()
    