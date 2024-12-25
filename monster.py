# Класс монстра с атрибутами name, monster_type и element
class Monster:
    def __init__(self, name, monster_type, element):
        self.name = name
        self.monster_type = monster_type
        self.element = element

    def __repr__(self):
        return f"{self.name} (Тип: {self.monster_type}, Стихия: {self.element})"


# Класс коллекции монстров
class MonsterCollection:
    def __init__(self):
        self.monsters = []

    # добавлять новых монстров
    def add_monster(self, monster):
        self.monsters.append(monster)

    # возвращает экземпляр итератора MonsterIterator
    def __iter__(self):
        return MonsterIterator(self)

    # метод для выбора монстров по стихии
    def get_monsters_by_element(self, element):
        return [monster for monster in self.monsters if monster.element.lower() == element.lower()]


# Итератор для коллекции монстров
class MonsterIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    # возвращает следующий элемент из коллекции или вызывает исключение StopIteration, если элементы закончились
    def __next__(self):
        if self._index < len(self._collection.monsters):
            monster = self._collection.monsters[self._index]
            self._index += 1
            return monster
        else:
            raise StopIteration


if __name__ == "__main__":
    # Создаем коллекцию монстров
    monster_collection = MonsterCollection()

    # Добавляем монстров в коллекцию
    monster_collection.add_monster(Monster("Гидра", "Гидро", "Вода"))
    monster_collection.add_monster(Monster("Феникс", "Пиро", "Огонь"))
    monster_collection.add_monster(Monster("Саламандра", "Пиро", "Огонь"))
    monster_collection.add_monster(Monster("Титан", "Гео", "Земля"))
    monster_collection.add_monster(Monster("Ледяной дракон", "Крио", "Крио"))
    monster_collection.add_monster(Monster("Электро-демон", "Электро", "Электро"))
    monster_collection.add_monster(Monster("Горгулья", "Анемо", "Воздух"))
    monster_collection.add_monster(Monster("Аранара", "Дендро", "Трава"))
    monster_collection.add_monster(Monster("Анемо-Слайм", "Анемо", "Воздух"))

    # Перебираем монстров в коллекции
    print("Монстры в коллекции:")
    for monster in monster_collection:
        print(monster)
 #       print(iter(monster_collection))


    # Запрашиваем стихию
    selected_element = input("\nВведите стихию для выбора монстров: ")

    # Получаем монстров по выбранной стихии
    filtered_monsters = monster_collection.get_monsters_by_element(selected_element)

    # Выводим отфильтрованных монстров
    if filtered_monsters:
        print(f"\nМонстры со стихией '{selected_element}':")
        for monster in filtered_monsters:
            print(monster)
    else:
        print(f"\nНет монстров со стихией '{selected_element}'.")

