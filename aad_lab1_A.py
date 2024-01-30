def main():

    r1 = float(input("What is the value of R1? "))
    r2 = float(input("What is the value of R2? ")) 
    r3 = float(input("What is the value of R3? "))

    resistance = round((1/((1/r1) + (1/r2) + (1/r3))),2)

    print(f"The equivalent resistance is {resistance} ohms")

if __name__=="__main__": 
    main()