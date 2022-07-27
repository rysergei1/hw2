p = 3.14
radius_planet_1 = int(input('Напишите радиус планеты №1 в млн.км.:\n')) * 1000000
radius_planet_2 = int(input('Напишите радиус планеты №2 в млн.км.:\n')) * 1000000
orbital_velocity_1 = int(input('Укажите орбитальную скорость планеты №1 в км/ч:\n'))
orbital_velocity_2 = int(input('Укажите орбитальную скорость планеты №2 в км/ч:\n'))
duration_1 = round(2 * radius_planet_1 * p / (orbital_velocity_1 * 24))
duration_2 = round(2 * radius_planet_2 * p / (orbital_velocity_2 * 24))
print(f'На планете №1 год длится: {duration_1} дн.')
print(f'На планете №2 год длится: {duration_2} дн.')
print('Правда ли, что на первой планете год больше, чем на второй?')
print(f'На планете №2 год длится: {duration_1 > duration_2} дн.')
print(duration_1 > duration_2)
