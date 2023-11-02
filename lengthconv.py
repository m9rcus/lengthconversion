while True:
    
    conv = input("What would you like to do (1: Inches to Centimeters, 2: Centimeters to Inches, 3: Feet to Yards, 4: Yards to Feet, 5: Inch to Feet, 6: Feet to Inch, 7: Centimeters to Feet, 8: Feet to Centimeters, 9: Inches to Yards, 10: Yards to Inches, 11: Centimeters to Yards, 12: Yards to Centimeters): ")
        
    if conv == "1":
        in1 = input("Enter inches: ")
        try:
            in1 = float(in1)
            if in1 < 0:
                print("Enter a number greater than 0")
            else:
                cm1 = in1 * 2.54
                print(cm1, "cm")
        except ValueError:
            print("Enter a valid number")

    elif conv == "2":
        cm2 = input("Enter centimeters: ")
        try:
            cm2 = float(cm2)
            if cm2 < 0:
                print("Enter a number greater than 0")
            else:
                in2 = cm2 / 2.54
                print(in2, "in")
        except ValueError:
            print("Enter a valid number")
    
    elif conv == "3":
        ft3 = input("Enter feet: ")
        try:
            ft3 = float(ft3)
            if ft3 < 0:
                print("Enter a number greater than 0")
            else:
                yd3 = ft3 / 3
                print(yd3, "yd")
        except ValueError:
            print("Enter a valid number")
    
    elif conv == "4":
        yd4 = input("Enter yards: ")
        try:
            yd4 = float(yd4)
            if yd4 < 0:
                print("Enter a number greater than 0")
            else:
                ft4 = yd4 * 3
                print(ft4, "ft")
        except ValueError:
            print("Enter a valid number")

    elif conv == "5":
        in5 = input("Enter inches: ")
        try:
            in5 = float(in5)
            if in5 < 0:
                print("Enter a number greater than 0")
            else:
                ft5 = in5 / 12
                print(ft5, "ft")
        except ValueError:
            print("Enter a valid number")
    
    elif conv == "6":
        ft6 = input("Enter inches: ")
        try:
            ft6 = float(ft6)
            if ft6 < 0:
                print("Enter a number greater than 0")
            else:
                in6 = ft6 * 12
                print(in6, "in")
        except ValueError:
            print("Enter a valid number")

    elif conv == "7":
        cm7 = input("Enter centimeters: ")
        try:
            cm7 = float(cm7)
            if cm7 < 0:
                print("Enter a number greater than 0")
            else:
                ft7 = cm7 / 30.48
                print(ft7, "ft")
        except ValueError:
            print("Enter a valid number")

    elif conv == "8":
        ft8 = input("Enter feet: ")
        try:
            ft8 = float(ft8)
            if ft8 < 0:
                print("Enter a number greater than 0")
            else:
                cm8 = ft8 * 30.38
                print(cm1, "cm")
        except ValueError:
            print("Enter a valid number")
    
    elif conv == "9":
        in9 = input("Enter inches: ")
        try:
            in1 = float(in1)
            if in1 < 0:
                print("Enter a number greater than 0")
            else:
                yd9 = in9 / 36
                print(cm1, "yd")
        except ValueError:
            print("Enter a valid number")
    
    elif conv == "10":
        yd10 = input("Enter yards: ")
        try:
            yd10 = float(yd10)
            if yd10 < 0:
                print("Enter a number greater than 0")
            else:
                in10 = yd10 * 36
                print(in10, "in")
        except ValueError:
            print("Enter a valid number")

    elif conv == "11":
        cm11 = input("Enter centimeters: ")
        try:
            cm11 = float(cm11)
            if cm11 < 0:
                print("Enter a number greater than 0")
            else:
                yd11 = cm11 / 91.44
                print(yd11, "yd")
        except ValueError:
            print("Enter a valid number")

    elif conv == "12":
        yd12 = input("Enter yards: ")
        try:
            yd12 = float(yd12)
            if yd12 < 0:
                print("Enter a number greater than 0")
            else:
                cm12 = yd12 * 91.44
                print(cm12, "cm")
        except ValueError:
            print("Enter a valid number")
    
    else:
        print("Enter a number from 1 to 12")
