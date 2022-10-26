class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        h, w = self.height, self.width
        return h * (w * "*" + "\n") if w <= 50 and h <=50 else "Too big for picture."

    def get_amount_inside(self, rectangle):
        return (self.width // rectangle.width) * (self.height // rectangle.height)



class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(side={self.width})"

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)




if __name__ == "__main__":

    # copied the example code of the usage of the classes from the project description

    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())    


    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))