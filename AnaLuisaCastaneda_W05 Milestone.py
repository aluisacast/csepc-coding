# Autor: Ana Luisa Castañeda Garce
#      W05 ADVENTURE GAME

import textwrap as tr
caps = "\033[91m {}\033[00m".format('CAPITALIZED')

print(f'\nWelcome adventurer!\n \nThis is your universe, you are the one that decides your fate.\n')
print(f'Remember to choose your options from the{caps} words :D \n')
ready = input(f'Are you ready for this adventure? (YES or NO) ')

if ready.lower() == 'no' :
   print("\nDon't worry, you can play other time. \n")
elif ready.lower() == 'yes' :
    start = "Your story starts as you overheard someone, mentioning that there is a treasure near your village. So, you decided that you'll find it yourself."
    print(tr(start)," \n")
    print(tr("The next day after arming yourself you embark on the bigest adventure of your life."), "\n")
    choice1 = input('Now, the question is do you go to the DESERT or the MOUNTAINS, \nboth just outside your village. ')
    if choice1.lower() == 'desert' :
        
        print()
        print(tr.fill('After walking for what appeared an entire week, you are dying of thirst. You see in the distance an oasis. '))
    
        choice2 = input('\nDo you RUN towards it or IGNORE it? ')

        if choice2.lower() == 'run' :
            print()
            print(tr.fill('That oasis was a hallucination. Sadly, because you ran without a thought you got lost without food and water and died.'))
            
            print("Don't worry you can find the treasure other time. \n") 

        elif choice2.lower() == 'ignore' :
            print()
            print(tr.fill("That oasis was a hallucination. Aren't you glad you ignored it? Because you kept walking, trying to find the treasure, you found another person. He told you he was looking for the treasure as well, and that the treasure wasn't in the desert."))
            choice3 = input('\nDo you TRUST in this treasure hunter and go back to search the treasure \nin the mountains or IGNORE him, he looks suspicious?  ')

            if choice3.lower() == 'ignore' :
                print()
                print(tr.fill("Because you didn't trust him, you wandered the desert without a thought. When you wanted to go back you coudn't find your way. As you didn't brought food or water, you died."))
            
                print("Don't worry you can find the treasure other time.") 
                print()
            
            elif choice3.lower() == 'trust' :
                print()
                print (tr.fill("Because you trusted him, you can rule out the desert as a place where the treasure is. Sadly, you've spent your entire day in the desert and have to go home."))
                print('\nNext morning you are ready to explore the mountains')
            
                print('\nThey say a dragon lives in the mountains.')
                choice = input('\nAre you sure you want to explore them (YES/NO)? \nThey say a dragon lives in there. ')

                if choice.lower() == 'no' :
                    print("\nDon't worry a dragon scares most people. \n")
                    print("You decided that you don't need a trasure, it is better to be alive.")
                    

                elif choice.lower() == 'yes' :
                    print('\nGood choice! \nHere in the mountains there should be fewer places to search for the treasure.')
                    print('\nAfter a couple of hours hiking, you see a crumbling castle.')
                
                    choice = input("Do you want to EXPLORE or do you keep WALKING? \nMaybe you'll find someplace else where the treasure might be. ")


                    if choice.lower() == 'explore' :
                        print()
                        print(tr.fill('You are the bravest person I know. Once you are inside the castle you see on the mezzanine two different color doors.'))
                        choice = input ('Do you want to explore inside the RED door or the BLACK one? ')

                        if choice.lower() == 'red' :
                            print('')
                            print(" __     __         _              __                      _ ")  
                            print(" \ \   / /        ( )            / _|                    | |")  
                            print("  \ \_/ /__  _   _|/__   _____  | |_ ___  _   _ _ __   __| | ") 
                            print("   \   / _ \| | | | \ \ / / _ \ |  _/ _ \| | | | '_ \ / _` |")  
                            print("    | | (_) | |_| |  \ V /  __/ | || (_) | |_| | | | | (_| | ") 
                            print("  _ |_|\___/ \__,_|_  \_/ \___| |_| \___/ \__,_|_| |_|\__,_| ") 
                            print(" | | | |          | |                                     ")    
                            print(" | |_| |__   ___  | |_ _ __ ___  __ _ ___ _   _ _ __ ___  ")    
                            print(" | __| '_ \ / _ \ | __| '__/ _ \/ _` / __| | | | '__/ _ \ ")    
                            print(" | |_| | | |  __/ | |_| | |  __/ (_| \__ \ |_| | | |  __/ ")     
                            print("  \__|_| |_|\___|  \__|_|  \___|\__,_|___/\__,_|_|  \___| ") 
                            print('')
                            print('')
                            print("   _____ ____ _____         _____ ____ _____         _____ ____ _____    ")
                            print("  /    /      \    \       /    /      \    \       /    /      \    \   ")
                            print("/____ /_________\____\   /____ /_________\____\   /____ /_________\____\ ")
                            print("\    \          /    /   \    \          /    /   \    \          /    / ")
                            print("   \  \        /  /         \  \        /  /         \  \        /  /    ")
                            print("      \ \    / /               \ \    / /               \ \    / /       ")
                            print("        \ \/ /                   \ \/ /                   \ \/ /         ")
                            print("          \/                       \/                       \/           ")
                            print('')
                            print('')
                            print("  _______ _    _ ______   ______ _   _ _____      ")
                            print(" |__   __| |  | |  ____| |  ____| \ | |  __ \     ")
                            print("    | |  | |__| | |__    | |__  |  \| | |  | |    ")
                            print("    | |  |  __  |  __|   |  __| | . ` | |  | |    ")
                            print("    | |  | |  | | |____  | |____| |\  | |__| |   ")
                            print("    |_|  |_|  |_|______| |______|_| \_|_____/  ")
                            print('')

                        elif choice.lower() == 'black' :

                            print("\nOh no! You've found a dragon, you must defeat it to survive. ")
                            choice = input('\nWhat weapon have you brought with you, a SWORD or a BOW and arrows? ')
                            if choice.lower() == 'sword' :
                                print()
                                print(tr.fill("After a good fight you have defeated the dragon. You decided to return home, to claim the title of a knight due to your heroic act of defeating a dragon.\n"))

                                            
                            elif choice.lower() == 'bow' :
                                print ("The arrows you've brought couldn't pierce the dragon's scales. But you made the dragon angry, he breathed fire and killed you.")
    
                                print("Don't worry, you can find the treasure another time.\n") 
                            else :
                                print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))
                        else :
                            print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))

                    elif choice.lower() == 'walking' :
                        print("\nGood choice, a few miles away from the castle you found a cave and a bridge that leads to a forest. \n")
                        choice = input('Do you want to explore the CAVE or a FOREST you see in the distance? ')

                        if choice.lower() == 'bridge' :

                            print('\nThe bridge was really old, as soon as you stepped on it broke and you fell to your death.')

                            print("Don't worry you can find the treasure other time.\n") 
                    

                        elif choice.lower() == 'cave' :

                            print("\nOh no! You've also found a dragon guarding it. You must defeat the dragon to win the treasure. As well, if you kill the dragon, you can become a knight. \n")

                            choice = input('\nWhat weapon will you use, a SWORD or your WORDS? Maybe you can reason with it. ')

                            if choice.lower() == 'sword' :
                
                                print("\nThis dragon has fought with multiple people and knows to not come close to a sword. He breathed fire and killed you.")
        
                            elif choice.lower() == 'words' :
                                print ("\nGood choice! This dragon was lonely so he spreaded the rumor of a treasure only to have someone to talk to.")
                                print('\nAfter hours of talking, the dragon is your friend and allowed you to take part of his the treasure home.')
                            else :
                                print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))
                        else :
                            print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))
                    else :
                        print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))
                else :
                    print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))
            else :
                print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))
        else :
            print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))

    elif choice1.lower() == "mountains" :
        print('\nThey say a dragon lives in the mountains.')
    else :
        print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))

else :
    print("\033[91m {}\033[00m" .format('\nSorry, we can only play if you follow the rules. You must choose from the CAPITALIZED words.  \n'))


