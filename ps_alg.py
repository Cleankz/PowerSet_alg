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
        result_set = self.array
        for i in set2.array:
            result_set.append(i)
        return self.array

    def difference(self, set2):
        result_set = PowerSet()
        for i in range(len(self.array)):
            if self.array[i] not in set2.array:
                result_set.put(self.array[i])
        # разница текущего множества и set2
        return result_set

    def issubset(self, set2):
        for i in (set2.array):
            if i not in self.array:
                return False
        return True
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
# a = PowerSet()
# b = [1235,46551651,51,51,6156,21,54,2,12231,5,12,5,42,6442,26,412,4,78,96,24,67,23,25,96,84,15,19]
# b = {}
# b = PowerSet()
# for i in range(50):
#     a.put(random.randint(0,50))
# for i in range(50):
#     b.put(random.randint(0,50))
# print(a.intersection(b))