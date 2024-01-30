import math

def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    Perimeter = round(((2 *length) + (2*width)),2)
    Area = round((length * width), 2)
    diagonal = round(math.sqrt((length**2) + (width**2)),2)

    print(f"Rectangle perimeter: {Perimeter}")
    print(f"Rectangle area: {Area}")
    print(f"Rectangle diagonal: {diagonal}")

if __name__=="__main__": 
    main()