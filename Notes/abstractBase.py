from abc import ABC,abstractmethod
class InvalidOperationError(Exception):
    pass
class Stream(ABC):
    def __init__(self):
        self.opened = False
    def open(self):
        if self.opened:
            raise InvalidOperationError("Steam is already opened")
        self.opened = True
    def close(self):
        if self.opened:
            raise InvalidOperationError("Steam is already closed")
        self.opened = False
    
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from file")

class Network(Stream):
    def read(self):
        print("Reading data from stream")

stream = Stream() 

