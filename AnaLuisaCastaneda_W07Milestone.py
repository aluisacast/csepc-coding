#     W07 Prove: Assignment Milestone
#    Author: Ana Luisa Castañeda


print('\nWelcome to this word game.\n\nInstructions: You have to guess our secret word. ')


word = 'cheese'

guess = input('\nWhat is your guess? ')

num_guess = 1

while guess.lower() != word :
    num_guess = num_guess + 1

    print('\nSorry, your guess isn\'t correct.')
    guess = input('\nWhat is your new guess? ')

else :

    if num_guess == 1 :    
        print(f'\nCongratulations! Your guess is correct!\n')
        print(f'It took you 1 guess.\n')
    else :
        print(f'\nCongratulations! Your guess is correct!\n')
        print(f'It took you {num_guess} guesses.\n')
    
    print('Thank you for playing with us today.\n')
