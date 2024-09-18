weight = int(input("Enter Weight: "))
unit = input("(L)bs or (K)g: ").lower()

if unit == 'l':
    weight_kg = weight * 0.45
    print(f"You are {weight_kg} kgs.")
else:
    weight_lb = weight / 0.45
    print(f"You are {weight_lb} pounds.")
