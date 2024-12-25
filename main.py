# Класс MyCollection: Хранит список элементов (items)
class MyCollection:
    def __init__(self):
        self.items = []

# Метод add_item добавляет элемент в коллекцию.
    def add_item(self, item):
        self.items.append(item)

# Метод __iter__ возвращает экземпляр итератора.
    def __iter__(self):
        return MyIterator(self)

# Класс MyIterator: Инициализируется с коллекцией и начальным индексом.
class MyIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

# Метод __iter__ возвращает сам итератор.
    def __iter__(self):
        return self

# Метод __next__ возвращает следующий элемент коллекции или вызывает исключение StopIteration, если элементы закончились.
    def __next__(self):
        if self._index < len(self._collection.items):
            item = self._collection.items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

# Пример использования
if __name__ == "__main__":
    collection = MyCollection()
    collection.add_item("Первый элемент")
    collection.add_item("Второй элемент")
    collection.add_item("Третий элемент")

# Создаем экземпляр MyCollection, добавляем элементы и проходим по ним с помощью цикла for.
    for item in collection:
        print(item)

