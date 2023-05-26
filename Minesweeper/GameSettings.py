
class GameSettings:
    def __init__(self, dimensions: int, width: int, mine_count: int):
        if(dimensions > 5):
            self.dimensions = 5
        elif(dimensions < 2):
            self.dimensions = 2
        else:
            self.dimensions = dimensions

        if(width >= 10):
            self.width = 10
        elif(width < 3):
            self.width = 3
        else:
            self.width = width
        if(mine_count > width**dimensions):
            self.mine_count == width**dimensions
        else:
            self.mine_count = mine_count



