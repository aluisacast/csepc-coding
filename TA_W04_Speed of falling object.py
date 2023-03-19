import math

print('\nWelcome to the velocity calculator. Please enter the following: ')

m = float(input('\nMass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
c = (p * C * A) / 2 #inner value

print (f'\nThe inner value of c is: {c:.3f}')
v_at_t = math.sqrt((m *g) /c) * (1 - math.exp((-(math.sqrt(m *g * c)) /m ) * t ))

print (f'The velocity after {t} seconds is {v_at_t:.3f} m/s\n')