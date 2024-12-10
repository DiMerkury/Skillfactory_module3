class Point():

    _values = ['free', 'fire', 'ship', 'miss', 'no_build']

    def __init__(self, x: int, y: int, value = "free"):
        self._x = x
        self._y = y
        self._status = value

    def __str__(self):
        if self._status == 'ship': return '■'
        if self._status == 'fire': return 'x'
        if self._status == 'free': return 'o'
        if self._status == 'miss': return 'T'
        if self._status == 'no_build': return '~'
        return self._status

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in self._values: 
            self._status = value
        else: print('Ошибка ввода:'+ value)


    