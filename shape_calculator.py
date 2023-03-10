class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"     #Rectangle(width=5, height=10)
    def set_width(self, w):
        self.width = w
        
    def set_height(self, h):
        self.height = h
        
    def get_area(self): #Returns area (width * height)
        return self.width*self.height
        
    def get_perimeter(self): #Returns perimeter (2 * width + 2 * height)
        return (2*self.width + 2*self.height)
        
    def get_diagonal(self): #Returns diagonal ((width ** 2 + height ** 2) ** .5)
        return ((self.width**2+self.height**2)**0.5)
        
    def get_picture(self): #Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
        if self.height>50 or self.width>50:
            return "Too big for picture."
        rect = ''
        for i in range(self.height):
            rect = rect+'*'*self.width+'\n'
        return rect
    def get_amount_inside(self, obj): #Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        return self.get_area()//obj.get_area()

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side) # super().__init__(self, side, side) 
    def __str__(self):
        return "Square(side="+str(self.width)+")"
        
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
