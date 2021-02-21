class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def __str__(self):
        return (("Rectangle(width={0}, height={1})").format(self.width,self.height))
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 *self.height)

    def get_diagonal(self):
        return ( (self.width ** 2)+ (self.height **2)) **.5

    def get_picture(self):
        if(self.width <= 50 and self.height <= 50):
            return ((self.width* "*") + "\n") * self.height
        else:
            return "Too big for picture."
    
    def get_amount_inside(self,shape):
        return (self.width * self.height) // (shape.height * shape.width)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    
    def set_side(self,value):
        self.set_height(value)
        self.set_width(value)
    
    def __str__(self):
        return (("Square(side={0})").format(self.width))
