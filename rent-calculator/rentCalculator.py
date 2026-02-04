#For the calculation of the rent 

rent = int(input("enter the rent of the house ="))
person = int(input("enter the number of person in the house ="))
electricity_bill = int(input("enter the electricity bill amount ="))
food = int(input("enter food expences  ="))
extra_material_expencies = int(input("enter extra material expencies  ="))
if person <= 0:
    print("Number of persons must be greater than 0")
else:
    total = (rent + electricity_bill + food + extra_material_expencies) / person
    print(f"Total bill per person ({person} persons) = {total}")


