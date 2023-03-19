#   W09 Assignment Milestone

items = []
prices =[]
menu = 1

print('\nWelcome to the Shopping Cart Program!')




while menu != '5' :

    print('\nMenu: \n1. Add item to your cart \n2. View cart \n3. Remove an item \n4. Computer total \n5. Quit')
    menu = input('\nPlease enter the number of the action you want to do. ')
    
    if menu == '1' : #Add to cart
        print()
        product = input('What is the name of the item you would like to add? ')
        cost = float(input('What is the price of the item? '))
        print()
        print ("\033[1m{}\033[00m" .format(product.capitalize()),end='')
        print(f' has been added to your cart with a price of ${cost:.2f}')

        items.append(product.lower())
        prices.append(cost)

        print('\n-----------------------------------------------')

    elif menu == '2' : # View cart

        print('\nThis is the content of your shopping cart.')

        for i in range(len(items)) :
            n = i + 1
            price = prices[i]
            print(f'{n}. {items[i]} - ${price:.2f}')
        
        print('\n-----------------------------------------------')


    elif menu == '3' : # Remove an item

        print("in progress")

        print('\n-----------------------------------------------')

    elif menu == '4' : #Compute total

        print("in progress")

        print('\n-----------------------------------------------')


    elif menu == '5' : # Quit
        menu = '5'
    else :
        print('\nThat is not a valid option. \nPlease choose one from the following options.')
    
else :
    print('\nThank you for using the Shopping Cart Program.')
    print('This program was made by', "\033[1m{}\033[00m" .format('Ana Luisa Castañeda.'))
    print('Godbye.\n')