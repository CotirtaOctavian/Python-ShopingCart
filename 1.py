class Ball(object):
    def __init__(self, color, size):
        self.color=color
        self.size=size

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.color == other.color
        return False


    def __ne__(self, other):
        return self.color != other.color

class Box(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.color == other.color
        return False


    def __ne__(self, other):
        return self.color != other.color


ball1 = Ball('blue', 'small')
ball2 = Ball('blue', 'small')
box1 = Box('blue', 'small')
ball3 = Ball('green', 'small')

print(ball1 == ball2)
print(ball1 == ball3)
print(ball1 == box1)
