Balance = 5000
A =int(input("withdrawal_amount:"))

if (Balance < A):
    print("Insufficient Balance")

else:
    print("Remaining Amount:",Balance-A )