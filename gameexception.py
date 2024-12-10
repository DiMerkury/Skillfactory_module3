class GameException(Exception):
    pass

class PlaseTaken(Exception):
    def __init__(self, message="Объекты пересекаются друг с другом"):
        self.message = message
        super().__init__(self.message)
        