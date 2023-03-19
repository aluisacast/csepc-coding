#   CSE 110  W1  Prove Assignment

#   Ana Luisa Castañeda Garces


class ANSI():
    def color(code):
        # Black:   30
        # Red:     31
        # Green:   32
        # Yellow:  33
        # Blue:    34
        # Magenta: 35
        # Cyan:    36
        # White:   37
        return "\33[{code};1m".format(code=code)  
    
    def reset() :
        return "\33[0m".format()
        
n = input('\nWhat is your name? ')

name = n.capitalize()

print()
print(  ANSI.color(34) + name + ', my favorite color is blue.\n' + ANSI.reset())

c = input('\n' +  'What is your favorite color? ')

color = c.lower()

print('\n' + ANSI.color(31) + "Your "  + ANSI.color(33) + 'favorite ' + \
     ANSI.color(32) + 'color ' + ANSI.color(36) + 'is ' + ANSI.color(35) + color +'.' \
        + ANSI.reset(), '\n') 
