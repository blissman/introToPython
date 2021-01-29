mass = float(input("What is your weight? "))
units = input("[K]g or [L]bs? ")
if units.upper() == "K":
    converted = 2.20462 * mass
    alt_unit = "lbs"
elif units.upper() == "L":
    converted = 0.453592 * mass
    alt_unit = "kg"
print("Your converted weight is: " + str(converted) + " " + alt_unit)