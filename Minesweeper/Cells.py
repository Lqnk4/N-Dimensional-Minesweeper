class Cells:
    def __init__(self, bomb: bool = False, clear: bool = False, flag: bool = False):
        self.bomb = bomb
        self.clear = clear
        self.flag = flag
        self.number = None
