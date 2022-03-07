import rectangle

def test_area():
     print("Testing area method")
     height = int(input("Enter height: "))
     width = int(input("Enter width: "))
    
     rect = rectangle.Rectangle(height, width)
     actual = rect.area()
     print("area of a rectangle of width {} and height {} is expected to be {}".format(width, height, actual)) 
     print("actual result {}".format(actual))
     
def test_perimeter():
     print("Testing perimeter method")
     height = int(input("Enter height: "))
     width = int(input("Enter width: "))
     
     rect = rectangle.Rectangle(height, width)
     actual = rect.perimeter()
     print("perimeter of a rectangle of width {} and height {} is expected to be {}".format(width, height, actual)) 
     print("actual result {}".format(actual))     
     
     
def main():
    test_area()
    test_perimeter()
    
main()