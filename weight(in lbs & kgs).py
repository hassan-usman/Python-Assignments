weight = float(input("Enter your weight: "))
weight_type = str(input("Enter type L(bs) or K(bs): " ))
if weight_type.upper == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")













































