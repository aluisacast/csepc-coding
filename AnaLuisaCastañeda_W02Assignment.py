# Ana Luisa Castañeda W02 Prove: Assignment - Word Games
print()
print("This is a game where tou get to be the author of your own story. \n\nTo create it, I need you to give me:\n")

name = input('Your name: ')
bf= input ("Your best friend's name: ")
animal = input('An animal: ')
verb = input('A verb: ')
exclamation = input('An exlamation: ')
verb2 = input ('A verb: ')
adjective = input ('An adjetive: ')
verb3 = input ('A verb: ')
event = input('An event: ')
end = "the end"
name_color = "\033[95m {}\033[00m" .format(name.capitalize()+ ': ')
bf_color = "\033[96m {}\033[00m" .format(bf.capitalize()+ ': ')

print("\nIn this story you are messaging with your best friend. \n")

print(name_color + 'Oh, '+ bf.capitalize() + " you won't believe what happened!  \n")
print(bf_color + 'What happened?\n')
output= f'The other day, I was really in trouble. It all started when I saw a very {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family.\n'
print (name_color  + output)
print(bf_color + 'Really? What did your parents do?\n')
print(name_color + "You know them, I'm grounded till next week. That's why I'm calling you. I wont be able to attend  to the " + event.lower() + ' this weekend with you.\n')
print(bf_color + 'No! I was looking forward to go with you.\n')
print(name_color + 'I know me too! Anyway, I have to go, if not my mom will get angrier. Bye!\n')
print(bf_color + 'Bye! Talk to you later.\n')
print(end.upper())
print('\nThank you for playing. \n')