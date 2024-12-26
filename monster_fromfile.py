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

    # добавлять новых монстров с валидацией
    def add_monster(self, monster):
        if not isinstance(monster, Monster):
            raise TypeError("Добавляемый объект должен быть экземпляром класса Monster")
        self.monsters.append(monster)

    # возвращает экземпляр итератора MonsterIterator
    def __iter__(self):
        return MonsterIterator(self)

    # метод для выбора монстров по стихии
    def get_monsters_by_element(self, element):
        return [monster for monster in self.monsters if monster.element.lower() == element.lower()]

    # метод для выбора монстров по типу
    def get_monsters_by_type(self, monster_type):
        return [monster for monster in self.monsters if monster.monster_type.lower() == monster_type.lower()]

    # метод для получения всех уникальных стихий
    def get_unique_elements(self):
        return set(monster.element for monster in self.monsters)

    # метод для получения всех уникальных типов
    def get_unique_types(self):
        return set(monster.monster_type for monster in self.monsters)

    # метод для загрузки монстров из текстового файла
    def load_monsters_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                monster_data = line.strip().split(';')
                if len(monster_data) != 3:
                    raise TypeError(
                        f"Ошибка в строке: '{line.strip()}'. Ожидалось 3 параметра монстр;тип;стихия, но получено {len(monster_data)}.")
                self.add_monster(Monster(*monster_data))


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

    # Загружаем монстров из текстового файла
    try:
        monster_collection.load_monsters_from_file('monsters.txt')
    except FileNotFoundError:
        print("Файл 'monsters.txt' не найден.")
        exit(1)

    while True:
        # Запрашиваем у пользователя выбор фильтрации
        choice = input(
            "\nВы хотите выбрать монстра по стихии или по типу? (введите 'стихия' или 'тип'): ").strip().lower()

        if choice == 'стихия':
            # Получаем все уникальные стихии и запрашиваем у пользователя стихию
            unique_elements = monster_collection.get_unique_elements()
            selected_element = input(f"Введите стихию для выбора монстров ({', '.join(unique_elements)}): ")
            filtered_monsters = monster_collection.get_monsters_by_element(selected_element)

            # Выводим отфильтрованных монстров по стихии
            if filtered_monsters:
                print(f"\nМонстры со стихией '{selected_element}':")
                for monster in filtered_monsters:
                    print(monster)
            else:
                print(f"\nНет монстров со стихией '{selected_element}'.")

        elif choice == 'тип':
            # Получаем все уникальные типы и запрашиваем у пользователя тип
            unique_types = monster_collection.get_unique_types()
            selected_type = input(f"Введите тип для выбора монстров ({', '.join(unique_types)}): ")
            filtered_monsters = monster_collection.get_monsters_by_type(selected_type)

            # Выводим отфильтрованных монстров по типу
            if filtered_monsters:
                print(f"\nМонстры с типом '{selected_type}':")
                for monster in filtered_monsters:
                    print(monster)
            else:
                print(f"\nНет монстров с типом '{selected_type}'.")

        else:
            print("Неверный ввод. Пожалуйста, введите 'стихия' или 'тип'.")

        # Запрос на продолжение работы программы
        continue_choice = input("\nХотите продолжить? (да/нет): ").strip().lower()

        if continue_choice != 'да':
            print("Удачи!")
            break  # Выход из цикла и завершение программы
