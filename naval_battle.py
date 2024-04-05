# Создаем класс игрового поля
class Playing_field:
    # Доска принимает параметр размер
    def __init__(self, size):
        self.size = size
        # В цикле итерируем доску
        self.grid = [['0' for i in range(size)] for i in range(size)]

# field_plauer = Playing_field(6)
# print(field_plauer.grid)

    # Отображаем доску в табличном виде
    def show_field(self):
        # Выводим номера столбцов
        print(' |1|2|3|4|5|6|')
        print('---------------')
        # В цикле итерируем строки доски с первым элементом номера строки
        for i in range(self.size):
            row = ' '.join(self.grid[i])
            print(f'{i+1}|{row}|')
            print('---------------')

# field_plauer = Playing_field(6)
# print(field_plauer.show_field())

    # Определяем координаты коробля на доске
    def check_hit(self, cords):
        x, y = cords
        # Возвращаем координаты на доску
        return self.grid[x][y] == '#'

    #  Определяем кординаты хода на доске
    def mark_hit(self, cords, is_hit):
        x, y = cords
        # Определяем метки попадания и промаха
        if is_hit:
            self.grid[x][y] = 'X'
        else:
            self.grid[x][y] = 'T'

# Создаем класс кораблей
class Ship:
    # Корабль принимает параметр размер
    def __init__(self, size):
        self.size = size
        # Создаем позицию корабля
        self.cords = []
    # Определяем место корабля на доске

    def place_ship(self, cords):
        self.cords = cords
    # Проеряем позицию корабля
    def check_hit(self, cords):
        return cords in self.cords
    # Ставим корабль на позицию
    def hit(self, cords):
        # Если позиция не занята ставим корабль на доску
        if self.check_hit(cords):
            self.cords.remove(cords)
            return True
        return False
    # Проверяем колличество попаданий
    def is_destroyed(self):
        return len(self.cords) == 0

# Модуль генерации случайного числа
from random import randint

# Создаем класс игры
class Game:
    # Определяем размер и номера кораблей
    def __init__(self, size, num_ships):
        self.size = size
        self.num_ships = num_ships
        self.Playing_field = Playing_field(size)
        self.Ships = [Ship(randint(2, 4)) for i in range(num_ships)]
        self.remaining_ships = num_ships

    # Определяем место кораблей
    def place_ships(self):
        for ship in self.Ships:
            while True:
                x = randint(0, self.size-1)
                y = randint(0, self.size-1)
                # Определяем ориентацию кораблей
                orientation = randint(0, 1) # 0 - вертикально, 1 - горизонтально
                cords = []
                for i in range(ship.size):
                    if orientation == 0:
                        cords.append((x, y + i))
                    else:
                        cords.append((x + i, y))
                if all(0 <= p[0] < self.size and 0 <= p[1] < self.size for p in cords):
                    ship.place_ship(cords)
                    break

    # Игровой режим
    def play(self):
        while self.remaining_ships > 0:
            self.Playing_field.show_field()
            x = int(input('Для выстрела введите координату Х: '))-1
            y = int(input('Для выстрела введите координату Y: '))-1
            if not (0 <= x < self.size and 0 <= y < self.size):
                print('Координаты в не диапазона')
                continue
            hit = False
            for ship in self.Ships:
                if ship.hit((x, y)):
                    self.Playing_field.mark_hit((x, y), True)
                    print('Попадание')
                    if ship.is_destroyed():
                        print('Корабль выведен из строя')
                        self.remaining_ships -= 1
                        hit = True
                        break
            if not hit:
                print('Мимо')
                self.Playing_field.mark_hit((x, y), False)
        print('Победа')

# Использование
game = Game(6,3)
game.place_ships()
game.play()

















