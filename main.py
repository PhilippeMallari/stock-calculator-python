# Constants for commissions
COMMISSION_ZERO = 0
COMMISSION_FIFTY = 50
COMMISSION_HUNDRED = 100

# Constants for threshold values of purchased/sold shares
THRESHOLD_ONE_THOUSAND = 1000
THRESHOLD_TWO_THOUSAND = 2000

print("-" * 54)
print("*** Welcome to the Stock Value Calculator Program! ***")
print("-" * 54)

# Get the stock name
stock_name = input("Enter stock's name: ")

# Get the input for the purchased share
purchased_shares = float(input("Enter the total number of purchased shares: "))
# Validation if purchased share <= 0
if purchased_shares <= 0:
    print("Error: Number of purchased shares should be >= 0")
    exit()

# Get the input for the amount purchased per share
per_purchased_share = float(input("Enter the dollar amount paid per purchased share: "))
if per_purchased_share <= 0:
    print("Error: the purchase amount should be > 0")
    exit()

# Get the input for the total number of sold shares
total_number_of_sold_shares = int(input("Enter the total number of sold shares: "))
if total_number_of_sold_shares <= 0 or total_number_of_sold_shares > purchased_shares:
    print("Error: Number of sold shares should be >= 0 and must be <= number of purchased shares.")
    exit()

# Get the input for the dollar amount paid per sold share
per_sold_share = float(input("Enter the dollar amount paid per sold share: "))
if per_sold_share <= 0:
    print('Error: The amount should be > 0')
    exit()

print("*" * 54)
# Checking first for scenario one:
if purchased_shares < THRESHOLD_ONE_THOUSAND:
    # Commission of 100 if the number of shares purchased is less than 1000
    purchase_commission = COMMISSION_HUNDRED
else:
    # No commission if the number of shares purchased is 1000 or more
    purchase_commission = COMMISSION_ZERO

# Checking for scenario two:
if total_number_of_sold_shares <  THRESHOLD_ONE_THOUSAND:
    # Commission of 100 if the number of shares sold is less than 1000
    sale_commission = COMMISSION_HUNDRED
elif total_number_of_sold_shares < THRESHOLD_TWO_THOUSAND:
    # Commission of fifty if the number of shares sold is 1000 to 2000
    sale_commission = COMMISSION_FIFTY
else:
    # No commission to be given if the shares sold is more than 2000
    sale_commission = COMMISSION_ZERO

# Output
# Center the "Purchasing Report" within a 54-character wide line
purchasing_report_title = "Purchasing Report"
print(purchasing_report_title.center(54))
print("*" * 54)

total_purchase_amount = purchased_shares * per_purchased_share
total_sale_amount = total_number_of_sold_shares * per_sold_share

# Calculate the total profit
if total_number_of_sold_shares < purchased_shares:
    profit = total_sale_amount - (total_number_of_sold_shares * per_purchased_share) - purchase_commission - sale_commission
else:
    profit = total_sale_amount - total_purchase_amount - purchase_commission - sale_commission


print("Stock Name: " + stock_name)
print("Total purchase amount: $", total_purchase_amount)
print("Purchase Commission: " + str(purchase_commission))
print("*" * 54)
selling_report_title = "Selling Report"
print(selling_report_title.center(54))
print("*" * 54)
print("Total sold amount: $", round(total_sale_amount, 1))
print("Sold Commission: " + str(sale_commission))
print("*" * 54)

# If profit is less than 0
if profit < 0:
    print("Good Luck Next Time, You Lost: $-", round(profit, 1))
# If profit is equal to 0
elif profit == 0:
    print("No Profit or Loss, Total Profit: ", round(profit, 1))
# If user has profit
else:   
    print("Congratulations, Total Profit: $", round(profit, 1))