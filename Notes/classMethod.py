class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0)

a = Point.zero()
