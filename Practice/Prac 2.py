weight_lb = int(input("Write your weight: "))

weight_kg = weight_lb/2.20462
protein = round(weight_kg)*2

print("You need " + str(protein) + " grams of protein")