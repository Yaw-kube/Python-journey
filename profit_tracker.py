total=0
num_trade = int(input("How many tades did you take today: "))
for i in range(num_trade):
    trade = int(input("Enter the results of each trade: $"))
    total= trade+total
print("Your total profit and loss is: $",total)

