class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        area=self.l*self.w
        return f"Area of rectangle: {area}cm²"

class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        area=(22/7)*self.r**2
        return f"Area of circle: {area:.2f}cm²"

shapes=[Rectangle(7,9),Circle(4),Rectangle(9,5),Circle(13)]
for i in shapes:
    print(i.area())