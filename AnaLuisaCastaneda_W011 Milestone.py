#   W11 Assignment Milestone
#   Data Analysis

# Variables 
low_le = 10000000000000000000000
high_le = 0


source = 'James C. Riley (2005) - Estimates of Regional and Global Life Expectancy, 1800–2001. Issue Population and Development Review. Population and Development Review. Volume 31, Issue 3, pages 537–543, September 2005., Zijdeman, Richard; Ribeira da Silva, Filipa, 2015, "Life Expectancy at Birth (Total)", http://hdl.handle.net/10622/LKYT53, IISH Dataverse, V1, and UN Population Division (2019)'
# -------------------------------


print()
print('Welcome to the: ',end='')
print("\033[4m{}\033[00m".format('1543-2019 World'),end='')
print(' Life Expectancy Viewer Program')
print('Data from: OurWorldInData.org\n')


with open("life-expectancy.csv") as le_file :

    next(le_file) # This skips the first line of the file that indicates
    # Entity,Code,Year,Life expectancy (years)

    for line in le_file :

        clean_line = line.strip() # cleans the strings of spaces
        data = clean_line.split(',')  #splits each line when there is a ","

        le = float(data[3]) # retieves the fourth column from data

        if le < low_le :  #overwrites the variable low_le if the new life expentansy is lower
            low_le = le 

        if le > high_le : #overwrites the variable high_le if the new life expentansy is higher
            high_le = le

    print(f'The max life expectancy during this period was {high_le} years.')
    print(f'The min life expectancy during this period was {low_le} years.')

print('\nThank you for using the Life Expectancy Viewer Program.')
print('This program was made by', "\033[1m{}\033[00m" .format('Ana Luisa Castañeda.'))
print('Godbye.\n')