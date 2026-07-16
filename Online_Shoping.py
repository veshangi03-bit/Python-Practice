Product_Name = (input("Product Name:"))
Product_Price = int(input("Product Price:"))
Quantity = int(input("No_of Quantity:"))
Total_bill = Product_Price*Quantity
if Total_bill>=5000:
    Discount = Total_bill * 10 / 100
    Final_bill = Total_bill - Discount
    print("Total Bill:", Total_bill)
    print("Discount:", Discount)
    print("Final Bill:", Final_bill)


else :
    print("Product Name:", Product_Name)
    print("Final_bill:",Total_bill)
print("THNAK YOU FOR SHOPPING!")

