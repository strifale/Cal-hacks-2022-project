import src

class fileEditor:
    def __init__(self, fileName, isSample: bool) -> None:
        self.name = fileName
        self.isSample = isSample

    def readFile(self):
        file = open(self.name, "r")
        