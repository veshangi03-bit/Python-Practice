Age = int(input("Enter Age:"))

if Age<5:
    print("Free ticket")
elif Age >= 5 and Age <= 18:
    print("Ticket_price:100" )
elif Age>=19 and Age<=60:
    print("Ticket_price:200" )
elif Age<60:
    print("Ticket_price:150" )
