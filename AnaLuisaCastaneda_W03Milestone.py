# 03 Prove: Milestone - Meal Price Calculator
# Ana Luisa Castañeda Garces

price_child = float(input("What is the price of a child's meal? "))
price_adult = float(input("What is the price of an adult's meal? "))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))

subtotal = (price_child*children)+(price_adult*adults)
sales_tax  = subtotal*(tax/100)
total = subtotal + sales_tax



print(f'\nSubtotal: ${"{:.2f}" .format(subtotal)}')
print(f'Sales Tax: ${"{:.2f}" .format(sales_tax)}')
print(f'Total: ${"{:.2f}" .format(total)} \n')

amount = int(input('What is the payment amount? '))
change = amount - total
print(f'Change: ${"{:.2f}" .format(change)} \n')
