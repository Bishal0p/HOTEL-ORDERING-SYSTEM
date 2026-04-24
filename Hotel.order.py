menu = {
    "Buff" : 150,
    "Pork" : 200,
    "Duck" : 140,
    "Chicken" : 65,
    "Sukuti" : 90,
    "Mutton" : 300,
    "Beer" : 160,
    "Signature" : 1350,
    "old monk" : 500,
    "Cubic ice" : 100,
}
print("Warm Welcome to my Sagarmatha Hotel") 
print("Duck: Rs.140\nChicken: Rs.65\nSukuti: Rs.90\nMutton: Rs.300\nBeer: Rs.160\nSignature: Rs.1350\nold monk: Rs.500\nCubic ice: Rs.100")

sum = 0
first_order = input("Enter your first order = ")
if first_order in menu:
    sum += menu[first_order]
    print(f"Your first order {first_order}  has been added")
else:
    print(f"This order {first_order} is not available!")
    
extra_order = input("Do you want more order?(Yes/No)")
if extra_order == "Yes":
    
    second_order = input("Enter the second order = ")
    if second_order in menu:
        sum += menu[second_order]
        print(f"The second order {second_order} is added")
    else:
        print(f"The order {second_order} is not available")
        
print("The total amount you have to pay is", sum)

