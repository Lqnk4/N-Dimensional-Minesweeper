
class GameSettings:
    def __init__(self, dimensions: int, width: int, mine_count: int):
        if dimensions > 6 :
            self.dimensions = 6
        elif dimensions < 1:
            self.dimensions = 1
        else:
            self.dimensions = dimensions

        if width >= 10:
            self.width = 10
        elif width < 2:
            self.width = 2
        else:
            self.width = width
        if mine_count > width**dimensions :
            self.mine_count = width**dimensions
        else:
            self.mine_count = mine_count



