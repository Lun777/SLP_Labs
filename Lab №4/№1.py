class Square:
    def __init__(self, length):
        self.length = length
    def find_perimeter(self):
        return 4*self.length
    def find_square(self):
        return self.length * self.length
    def find_diagonal(self):
        return 2*self.length*self.length

a = Square(5)
print(a.find_perimeter())
print(a.find_square())
print(a.find_diagonal())
