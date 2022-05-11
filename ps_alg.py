
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
        if isinstance(set2, (list, dict, set)): # на всякий случай добавил, для своего спокойствия, чтобы точно знать что я учел все варианты 
            result_set = PowerSet()
            for i in range(len(self.array)):
                if self.array[i] in set2:# если  элемент есть и в множестве-параметре тоже то мы  добавляем его к результату 
                    result_set.put(self.array[i])
            return result_set

        result_set = PowerSet()
        for i in range(len(self.array)):
            if self.array[i] in set2.array: # если элемент есть и в множестве-параметре тоже то мы  добавляем его к результату
                result_set.put(self.array[i])

        return result_set # возвращаем  новое множество

    def union(self, set2):
        if isinstance(set2, (list, dict, set)): # на всякий случай добавил, для своего спокойствия, чтобы точно знать что я учел все варианты
            result_set = PowerSet()
            result_set.array = self.array
            if len(set2) == 0: # если множество параметр пустое , это значит что вернется множество без изменений поэтому self
                return self
            if len(self.array) == 0: # то же самое что и выше
                return set2
            for i in set2:
                result_set.put(i)
            return result_set
        result_set = PowerSet()
        result_set.array = self.array
        if len(set2.array) == 0:  # если множество параметр пустое , это значит что вернется множество без изменений поэтому self
            return self
        if len(self.array) == 0:
            return set2
        for i in set2.array:
            result_set.put(i)

        return result_set # возвращаем новое множество содержащее в себе все элементы двух других без повторений


    def difference(self, set2):        # разница текущего множества и set2
        if isinstance(set2, (list, dict, set)): # на всякий случай добавил, для своего спокойствия, чтобы точно знать что я учел все варианты
            result_set = PowerSet()
            for i in self.array:
                if i not in set2:
                    result_set.put(i)
            return result_set

        result_set = PowerSet() # создаем новое множество
        for i in range(len(self.array)):
            if self.array[i] not in set2.array: # если элемента нет в множ-параметре то мы его добавляем в результат
                result_set.put(self.array[i])

        return result_set # возвращаем новое множество


    def issubset(self, set2):
        if isinstance(set2, (list, dict, set)):# на всякий случай добавил, для своего спокойствия, чтобы точно знать что я учел все варианты
            if len(set2) <= 0:
                return False
            for i in set2:
                if i not in self.array:
                    return False
            return True

        if len(set2.array) <= 0: # так как пустое множество является подмножеством любого множества 
            return True

        for i in (set2.array):
            if i not in self.array:#если хотябы один элемент не входит в основное множество то False
                return False
        return True