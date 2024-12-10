from point import Point

class Ships():

    def __init__(self, x: int, y: int, size, orientation = 'horizontal'):
        try:
            self._statusship = []
            if x <= 0 or y <=0:
                raise ValueError('недопустимые координаты')
            self._plase = [x, y]
            self._size = size
            self._orientation = orientation
            for el in range(size):
                if self._orientation == 'horizontal':
                    self._statusship.append(Point(x, y, 'ship'))
                    y += 1
                else:
                    self._statusship.append(Point(x, y, 'ship'))
                    x += 1
        except ValueError:
            print('недопустимые координаты')

    def __str__(self):
        return self.print_ship()

    @property
    def size(self):
        return self._size

    @property
    def orientation(self):
        return self._orientation
    
    @property
    def plase(self):
        return self._plase
    
    @property
    def statusship(self):
        return self._statusship

    @property
    def hp(self):
        i = 0
        for el in self._statusship:
            if el.status == 'ship': i += 1            
        return i

    def print_ship(self):
        return ''.join(map(str, self._statusship))
    