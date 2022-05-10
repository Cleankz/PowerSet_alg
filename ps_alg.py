# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
import random
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.array = []

    def size(self):
        return len(self.array)
        # количество элементов в множестве

    def put(self, value):
        if value not in self.array:
            self.array.append(value)
        # всегда срабатывает

    def get(self, value):
        if value in self.array:
            return True
        else:
            return False
        # возвращает True если value имеется в множестве,
        # иначе False

    def remove(self, value):
        if value in self.array:
            del self.array[self.array.index(value)]
            return True
        else:
            return False
        # возвращает True если value удалено
        # иначе False

    def intersection(self, set2):
        t1 = type({123,156})
        t2 = type([1,2,3])
        t3 = type({})
        if type(set2) is t1 or type(set2) is t2 or type(set2) is t3:
            result_set = PowerSet()
            for i in range(len(self.array)):
                if self.array[i] in set2:
                    result_set.put(self.array[i])
            return result_set

        result_set = PowerSet()
        for i in range(len(self.array)):
            if self.array[i] in set2.array:
                result_set.put(self.array[i])
        # пересечение текущего множества и set2 (self.array[i])
        return result_set

    def union(self, set2):
        t1 = type({123,156})
        t2 = type([1,2,3])
        t3 = type({})
        if type(set2) is t1 or type(set2) is t2 or type(set2) is t3:
            result_set = PowerSet()
            result_set.array = self.array
            for i in set2:
                result_set.put(i)
            return result_set

        result_set = PowerSet()
        result_set.array = self.array
        for i in set2.array:
            result_set.put(i)
        return result_set

    def difference(self, set2):
        t1 = type({123,156})
        t2 = type([1,2,3])
        t3 = type({})
        if type(set2) is t1 or type(set2) is t2 or type(set2) is t3:
            result_set = PowerSet()
            for i in self.array:
                if i not in set2:
                    result_set.put(i)
            return result_set
        result_set = PowerSet()
        for i in range(len(self.array)):
            if self.array[i] not in set2.array:
                result_set.put(self.array[i])
        # разница текущего множества и set2
        return result_set

    def issubset(self, set2):
        t1 = type({123,156})
        t2 = type([1,2,3])
        t3 = type({})
        if type(set2) is t1 or type(set2) is t2 or type(set2) is t3:
            for i in set2:
                if i not in self.array:
                    return False
            return True

        for i in (set2.array):
            if i not in self.array:
                return False
        return True
