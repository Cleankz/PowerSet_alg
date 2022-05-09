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
        result_set = []
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
        result_set = []
        for i in range(len(self.array)):
            if self.array[i] not in set2.array:
                result_set.append(self.array[i])
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
