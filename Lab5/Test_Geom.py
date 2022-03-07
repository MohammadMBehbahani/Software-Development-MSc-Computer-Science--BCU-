import geom

     
def main():
    geo1 = geom.Coordinate(10, 15)
    geo2 = geom.Coordinate(5, 25)
    
    rec = geom.Rectangle(geo1, geo2)
    print(rec.area())
    
main()