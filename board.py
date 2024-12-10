from ships import Point, Ships
from gameexception import PlaseTaken

class Boards():

    def __init__(self) -> None:
        self._matrix = []
        self.val_size = [1, 2, 3, 4, 5, 6]
        for i in range(6):
            tmp_sp = []
            for j in range(6):
                tmp_sp.append(Point(i, j))
            self._matrix.append(tmp_sp.copy())
            tmp_sp.clear()

    @property
    def matrix(self):
        return self._matrix

    def area_ship_mark(self, x, y):
        if x in self.val_size and y in self.val_size:
            self._matrix[x - 1][y - 1].status = 'no_build'

    def area_ship(self, ship:Ships):
        for i in range(ship.size):
            if ship.orientation == 'horizontal':
                #заполнение вокркг корабля
                #заполнение сверху
                self.area_ship_mark(ship.plase[1] - 1, ship.plase[0] + i)
                #заполнение снизу
                self.area_ship_mark(ship.plase[1]+1, ship.plase[0] + i)
                #заполнение слева
                self.area_ship_mark(ship.plase[1], ship.plase[0] - 1)
                #заполнение справа
                self.area_ship_mark(ship.plase[1], ship.plase[0] + ship.size)
                #заполнение диагоналей
                self.area_ship_mark(ship.plase[1] - 1, ship.plase[0] - 1)
                self.area_ship_mark(ship.plase[1] + 1, ship.plase[0] - 1)
                #заполнение диагоналей
                self.area_ship_mark(ship.plase[1] - 1, ship.plase[0] + ship.size)
                self.area_ship_mark(ship.plase[1] + 1, ship.plase[0] + ship.size)

            else:
                #заполнение вокркг корабля
                #заполнение сверху
                self.area_ship_mark(ship.plase[1] - 1, ship.plase[0])
                #заполнение снизу
                self.area_ship_mark(ship.plase[1] + ship.size, ship.plase[0])
                #заполнение слева
                self.area_ship_mark(ship.plase[1] + i, ship.plase[0] - 1)
                #заполнение справа
                self.area_ship_mark(ship.plase[1] + i, ship.plase[0] + 1)
                #заполнение диагоналей
                self.area_ship_mark(ship.plase[1] - 1, ship.plase[0] - 1)
                self.area_ship_mark(ship.plase[1] + ship.size, ship.plase[0] - 1)
                #заполнение диагоналей
                self.area_ship_mark(ship.plase[1] - 1, ship.plase[0] + 1)
                self.area_ship_mark(ship.plase[1] + ship.size, ship.plase[0] + 1)

    def print_board(self, hide_ships: bool = False):
        print(' '.join(f'  {i}' if i == 1 else str(i) for i in range(1,7)))
        i = 1
        for row in self._matrix:
            st = str(i)
            for el in row:
                if hide_ships:
                    if el.status == 'ship':
                        st += ' ' + 'o'
                    else:
                        st += ' ' + str(el)
                else:
                    st += ' ' + str(el)
            i += 1
            print(st)

    def clear(self):
        self.__init__()

    def add_ship(self, ship: Ships) -> bool:
        try:
            if ship.plase[0] in self.val_size and ship.plase[1] in self.val_size:
                if ship.orientation == 'horizontal':
                    if (ship.plase[0] + ship.size - 1) not in self.val_size:
                        raise IndexError
                else:
                    if (ship.plase[1] + ship.size - 1) not in self.val_size:
                        raise IndexError                    
            else:
                raise IndexError

            if ship.orientation == 'horizontal':
                for i in range(ship.plase[0] - 1, ship.plase[0] + ship.size - 1):
                    if self._matrix[ship.plase[1] - 1][i].status != 'free':
                        raise PlaseTaken('Место размещения занято другим кораблём')
            else:
                for j in range(ship.plase[1] - 1, ship.plase[1] + ship.size - 1):
                    if self._matrix[j][ship.plase[0] - 1].status != 'free':
                        raise PlaseTaken('Место размещения занято другим кораблём')

        except IndexError:
            print('корабль не помещается на поле')
            return False

        except PlaseTaken:
            print('Место размещения занято другим кораблём')
            return False

        else:
            for i in range(ship.size):
                if ship.orientation == 'horizontal':
                    #установка корабля
                    ship.statusship[i].x = ship.plase[1] - 1
                    ship.statusship[i].y = ship.plase[0] - 1 + i
                    self._matrix[ship.plase[1] - 1][ship.plase[0] - 1 + i] = ship.statusship[i]
                else:
                    #установка корабля                    
                    ship.statusship[i].x = ship.plase[1] - 1 + i
                    ship.statusship[i].y = ship.plase[0] - 1
                    self._matrix[ship.plase[1] - 1 + i][ship.plase[0] - 1] = ship.statusship[i]
            self.area_ship(ship)
        return True
