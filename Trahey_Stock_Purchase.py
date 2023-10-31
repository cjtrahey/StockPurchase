# Constants - 3%
purchaseCommission = 0.03
salesCommission = 0.03

# Inputs
sharesBought = int(input('Enter the number of shares purchased: '))
buyPricePerShare = float(input('Enter the purchase price per share: '))
soldPricePerShare = float(input('Enter the selling price per share:' ))

# Amount paid for stock
paidForStock = sharesBought * buyPricePerShare

# Commission paid - buying
boughtCommissionTotal = paidForStock * purchaseCommission

# Total cost of buying
purchaseTotal = paidForStock + boughtCommissionTotal

# Total value of selling
soldForStock = sharesBought * soldPricePerShare

# Commission paid - selling
soldCommissionTotal = soldForStock * salesCommission

# Sale Total Calculation
salesBalance = soldForStock - soldCommissionTotal

# Profit or Loss?
totalValue = salesBalance - purchaseTotal

# Results Output
print("Stock Transactions")
print("------------------")
print(f"Amount paid for the stock: ${paidForStock:10.2f}")
print(f"Plus purchase commission: ${boughtCommissionTotal:10.2f}")
print(" ----------")
print(f"Balance of purchase: ${purchaseTotal:10.2f}")
print(f"Amount stock was sold for: ${soldForStock:10.2f}")
print(f"Less sales commission: ${soldCommissionTotal:10.2f}")
print(" ----------")
print(f"Balance of Sale: ${salesBalance:10.2f}")
print(f"Profit or Loss: ${totalValue:10.2f}")