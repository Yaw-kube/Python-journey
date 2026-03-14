#Defining expenses variable
#food = int(input("Enter the amount of money you spent on Food: $"))
#rent = int (input("Enter the amount you spent on Rent: $"))
#water = int (input("Enter the amount of money you spent on Water: $"))
#transportation = int(input("Enter the amount you spent on Transportation: $"))
#power = int(input("Enter the amount you spent on power: $"))
#expenses = food+water+rent+transportation+power
#print("Your total spent today is: $",expenses)


#using for loop
sum=0
for i in range(5):
    expenses=int(input("Enter your expenses: $"))
    sum = sum+expenses
average= expenses/5
print("Your total expenses is: $ ",sum)
print("Your average expense is: $",average)