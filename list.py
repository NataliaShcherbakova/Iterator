# Класс MyList: Хранит данные в атрибуте data
# Метод __iter__ возвращает экземпляр итератора MyListIterator
# Класс MyListIterator: Инициализируется объектом MyList и устанавливает начальный индекс
# Метод __iter__ возвращает сам итератор
# Метод __next__ возвращает следующий элемент списка или вызывает исключение StopIteration, если элементы закончились.
class MyList:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyListIterator(self)


class MyListIterator:
    def __init__(self, my_list):
        self._my_list = my_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._my_list.data):
            result = self._my_list.data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


# Пример использования

# Создается экземпляр MyList с набором данных
# С помощью цикла for происходит итерация по элементам списка и их вывод
if __name__ == "__main__":
    my_list = MyList([1, 2, 3, 4, 5])

    print("Перебор элементов списка:")
    for item in my_list:
        print(item)

