class Palyer():
    def __init__(self) -> None:
        self.arr_ship = [] #массив кораблей

    def build_ship(self):
        pass

    def fire(self):
        pass

    def display_ship(self):
        print(', '.join(map(str, self.arr_ship)))

    @property
    def get_arr_ship(self):
        return self.arr_ship

    def end_ship(self):
        pass