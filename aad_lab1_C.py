def main():
    LOm = float(input("Enter m for Line 1: "))
    LOb = float(input("Enter b for Line 1: "))
    LSm = float(input("Enter m for Line 2: "))
    LSb = float(input("Enter b for Line 2: "))

    ValX = (LSb - LOb)/(LOm - LSm)
    ValY = round(((LOm * ValX) + LOb), 2)



    print(f"The intersection point is {round(ValX, 2), ValY}")

if __name__=="__main__": 
    main()




