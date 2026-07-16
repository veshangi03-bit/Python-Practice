Units = int(input("Unit Used:"))
if Units<=100:
    print("Rates:₹5/unit")
    bill = Units*5
elif Units<=100:
    print("Rates:₹8/unit")
    bill = Units*8
elif Units<200:
    print("Rates:₹10/unit")
    bill = Units*10
print("Electricity Bill: ₹",bill)