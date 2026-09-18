#number of items
#quantity
#price
#total

number_of_items=int(input("How many items do you have: "))
total=0
for i in range(number_of_items):
    print("\nItems: ",i+1)
    quantity=int(input("Enter the quantity: "))
    price=float(input("Enter the price: "))
    total=total+(quantity*price)

print("\nTotal bill: ",total)