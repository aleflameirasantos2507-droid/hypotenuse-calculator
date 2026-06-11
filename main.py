from math import sqrt, pow

opposite_side = float(input('Enter the opposite side: '))
adjacent_side = float(input('Enter the adjacent side: '))

hypotenuse = sqrt(pow(opposite_side, 2) + pow(adjacent_side, 2))

print(
    'The hypotenuse of the triangle with opposite side {:.2f} and adjacent side {:.2f} is {:.2f}'.format(
        opposite_side,
        adjacent_side,
        hypotenuse
    )
)
