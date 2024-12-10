from player import Palyer
from board import Boards, Ships

class User(Palyer):

    def __init__(self) -> None:
        super().__init__()
        self.arr_ship = [] #массив кораблей
    
    def _messenge_build_ship(self, type_ship: int):
        if type_ship == 3:
            st = '3-х палубный'
        if type_ship == 2:
            st = '2-х палубный'  
        if type_ship == 1:
            st = '1 палубный'
        print(f'Надо расположить свой {st} корабль.\n'+
                'Введите координаты левой верхней точки на поле, где бы вы хотели расположить свой корабль:')
        
    def _input_date(self, size = 1):
        while True:
            try:
                input_st = input('Примеры: "1 2", "3 3", "3 1": ').split()
                print(input_st)
                x = int(input_st[0])
                y = int(input_st[1])
                if size != 1:
                    input_orien = input('Введите направлеие коробля (1-по горизонтали, 2-по вертикали):')
                    orien = int(input_orien)
                    if orien not in [1, 2]: raise ValueError
                    else: 
                        if orien == 1:
                            orien = 'horizontal'
                        else:
                            orien = 'vertical'
                else:
                    orien = 1
            except ValueError:
                print('Ошибка ввода цифр, посмотри примеры и описание')
            except IndexError:
                print('Ошибка ввода цифр, надо 2 значения, посмотри примеры')
            else:
                return [y, x, orien]
            
    def _search_ship(self, point, arr_ship) -> int:
        for i in range(len(arr_ship)):
            if point in arr_ship[i].statusship:
                return i

    def build_ship(self, br: Boards):
        print('Вам необходимо расставить корабли на поле.\n'+
               'Доступны: один 3-х палубный, два 2-х палубных, три 1 палубных корабля.')
             
        #начало добавления
        while True:
            self._messenge_build_ship(3)
            x_y_orien = self._input_date(3)
            print(x_y_orien[1], x_y_orien[0])
            sh3 = Ships(x_y_orien[1], x_y_orien[0], 3, x_y_orien[2])
            if br.add_ship(sh3):
                self.arr_ship.append(sh3)
                break
        print('Получилось поле:')
        br.print_board()

        while True:
            self._messenge_build_ship(2)
            x_y_orien = self._input_date(2)
            sh2_1 = Ships(x_y_orien[1], x_y_orien[0], 2, x_y_orien[2])
            if br.add_ship(sh2_1):
                self.arr_ship.append(sh2_1)
                break
        print('Получилось поле:')
        br.print_board()

        while True:
            self._messenge_build_ship(2)
            x_y_orien = self._input_date(2)
            sh2_2 = Ships(x_y_orien[1], x_y_orien[0], 2, x_y_orien[2])
            if br.add_ship(sh2_2):
                self.arr_ship.append(sh2_2)
                break
        print('Получилось поле:')
        br.print_board()

        while True:
            self._messenge_build_ship(1)
            x_y_orien = self._input_date()
            sh1_1 = Ships(x_y_orien[1], x_y_orien[0], 1)
            if br.add_ship(sh1_1):
                self.arr_ship.append(sh1_1)
                break
        print('Получилось поле:')
        br.print_board()

        while True:
            self._messenge_build_ship(1)
            x_y_orien = self._input_date()
            sh1_2 = Ships(x_y_orien[1], x_y_orien[0], 1)
            if br.add_ship(sh1_2):
                self.arr_ship.append(sh1_2)
                break
        print('Получилось поле:')
        br.print_board()

        while True:
            self._messenge_build_ship(1)
            x_y_orien = self._input_date()
            sh1_3 = Ships(x_y_orien[1], x_y_orien[0], 1)
            if br.add_ship(sh1_3):
                self.arr_ship.append(sh1_3)
                break

        # Убираем символы куда строить нельзя
        for row in br.matrix:
            for el in row:
                if el.status == 'no_build':
                    el.status = 'free'       

    def fire(self, br: Boards, arr_ship1) -> str:
        while True:
            x_y = self._input_date()
            print(f'Целим в {x_y[0]}, {x_y[1]}')
            try:
                if br.matrix[x_y[0] - 1][x_y[1] - 1] in ['fire', 'miss', 'no_build']:
                    print('Сюда нет смысла стрелять!')
                else: 
                    break
            except IndexError:
                print('Сюда нет смысла стрелять!')
        
        if br.matrix[x_y[0] - 1][x_y[1] - 1].status == 'ship':
            br.matrix[x_y[0] - 1][x_y[1] - 1].status = 'fire'

            i = self._search_ship(br.matrix[x_y[0] - 1][x_y[1] - 1], arr_ship1)
            if arr_ship1[i].hp == 0:
                print('Убит!')
                br.area_ship(arr_ship1[i])
                return 'kill'
            else:
                print('Ранил!')
                return 'wound'
        else:
            print('Мимо!')
            br.matrix[x_y[0] - 1][x_y[1] - 1].status = 'miss'
            return 'miss'
