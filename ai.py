import random

from player import Palyer
from board import Boards, Ships

class Ai(Palyer):

    def __init__(self):
        super().__init__()
        self.arr_ship = [] #массив кораблей

    def _search_ship(self, point, arr_ship) -> int:
        for i in range(len(arr_ship)):
            if point in arr_ship[i].statusship:
                return i

    def build_ship(self, br: Boards):
        # 1 - 3-x, 2 - 2-x, 3 - 1-а
        i = 0
        ort = ['horizontal', 'vertical']
        fin = True
        while i <= 100 and fin:
            br.clear()
            self.arr_ship.clear()
            i3 = 0
            while i3 <100:
                sh3 = Ships(random.randint(1,6), random.randint(1,6), 3, random.choice(ort))
                if br.add_ship(sh3):
                    self.arr_ship.append(sh3)
                    break
                else:
                    i3 += 1
    
            i2_1 = 0
            while i2_1 < 100:
                sh2_1 = Ships(random.randint(1,6), random.randint(1,6), 2, random.choice(ort))
                if br.add_ship(sh2_1):
                    self.arr_ship.append(sh2_1)
                    break
                else:
                    i2_1 += 1

            i2_2 = 0
            while i2_2 < 100:
                sh2_2 = Ships(random.randint(1,6), random.randint(1,6), 2, random.choice(ort))
                if br.add_ship(sh2_2):
                    self.arr_ship.append(sh2_2)
                    break
                else:
                    i2_2 += 1

            i1_1 = 0
            while i1_1 < 100:
                sh1_1 = Ships(random.randint(1,6), random.randint(1,6), 1)
                if br.add_ship(sh1_1):
                    self.arr_ship.append(sh1_1)
                    break
                else:
                    i1_1 += 1

            i1_2 = 0
            while i1_2 < 100:
                sh1_2 = Ships(random.randint(1,6), random.randint(1,6), 1)
                if br.add_ship(sh1_2):
                    self.arr_ship.append(sh1_2)
                    break
                else:
                    i1_2 += 1

            i1_3 = 0
            while i1_3 < 100:
                sh1_3 = Ships(random.randint(1,6), random.randint(1,6), 1)
                if br.add_ship(sh1_3):
                    self.arr_ship.append(sh1_3)
                    fin = False
                    break
                else:
                    i1_3 += 1
#            print('Построенные доски:', i) #счётчик сколько попыток построить доску было
            i += 1

#        print(f'sh3={i3}, sh2_1={i2_1}, sh2_2={i2_2}, sh1_1={i1_1}, sh1_1={i1_2}, sh1_1={i1_3}, i={i}') #сколько попыток было поставить каждый корабль
        # Убираем символы куда строить нельзя
        for row in br.matrix:
            for el in row:
                if el.status == 'no_build':
                    el.status = 'free'

    def fire(self, br: Boards, arr_ship1) -> str:
        # хорошо развернуть весь массив и собрать из него список свободных поинтов, а там выбирать рандомный элемент из этого списка
        free_point = []
        for row in br.matrix:
            for el in row:
                if el.status not in ['fire', 'miss', 'no_build']:
                    free_point.append(el)
        
        el = random.choice(free_point)
        print(f'Целим в {el.x}, {el.y}')
        if el.status == 'ship':
            el.status = 'fire'
            i = self._search_ship(el, arr_ship1)
            if arr_ship1[i].hp == 0:
                print('Убит!')
                br.area_ship(arr_ship1[i])
                return 'kill'
            else:
                print('Ранил!')
                return 'wound'
        else:
            print('Мимо!')
            el.status = 'miss'
            return 'miss'
        
    def end_ship(self) -> bool:
        for el in self.arr_ship:
            if '■' in str(el):
                return False
        return True
