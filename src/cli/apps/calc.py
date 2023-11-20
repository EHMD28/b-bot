import math

def evaluate_equ(equ: str):    
    try:
        print(f'{equ} =',
              f'{round(eval(equ), 4)}')
    except ZeroDivisionError:
        print("You cannot divide by 0")
    except NameError:
        print("Invalid Expression")
    except TypeError:
        print("Invalid Expression")


def calc_area(shape: str):
    a: float
    b: float

    if 'square' in shape:
        a = round(float(input('Enter side length of square: ')), 2)
        # space
        s: str = ' ' * len(str(a))

        print(f'          {a}\n',
              f'{s}   ----------\n',
              f'{s}  |          |\n',
              f'{a}  |          |\n',
              f'{s}  |          |\n',
              f'{s}   ----------\n')
        print(f'Area of square (side length {a}): {a * a}')
    elif 'tri' in shape:
        ...
    elif 'circ' in shape:
        PI = 3.14159
        a = float(input("Enter the radius of circle: "))
        # space
        s: str = ' ' * (len(str(a)))

        print(f'\n               {s}*  *    \n',
              f'           {s}*        * \n',
              f'          {s}*          *\n',
              f'Radius: {a}  *     T    *\n',
              f'           {s}*    |   * \n',
              f'              {s}*  *    \n',
              )

        print(f'Area of circle (radius {a}): {PI * (a * a)}')
    elif 'rect' in shape:
        a = round(float(input('Enter height of rectangle: ')), 2)
        b = round(float(input('Enter width of rectangle: ')), 2)
        # space
        s: str = ' ' * len(str(a))

        if a > b:
            print(f'          {a}\n',
                  f'{s}   ---------------\n',
                  f'{s}  |               |\n',
                  f'{b}  |               |\n',
                  f'{s}  |               |\n',
                  f'{s}   ---------------\n')
            print(f'Area of square (side lengths {a} x {b}): {a * b}')
        else:
            print(f'          {b}\n',
                  f'{s}   ---------------\n',
                  f'{s}  |               |\n',
                  f'{a}  |               |\n',
                  f'{s}  |               |\n',
                  f'{s}   ---------------\n')
            print(f'Area of square (side lengths {a} x {b}): {a * b}')
    else:
        print('Invalid shape')


def calc_volume(shape: str):
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0
    result: float = 0.0

    if shape in 'cube':
        a = float(input("Enter side length of cube: "))
        result = a * a * a
        print(f"Volume for cube with side length {a} is: {result}")
    elif shape in 'rectangular-prism':
        a = float(input("Enter length of rectangular prism: "))
        b = float(input("Enter width of rectangular prism: "))
        c = float(input("Enter heigh of rectangular prism: "))
        result = a * b * c
        print(f"Volume for a {a} x {b} x {c} rectangular prism is: {result}")
    elif shape in 'pyramid':
        ...
    elif shape in 'cone':
        ...
    elif shape in 'cylinder':
        ...
    elif shape in 'sphere':
        a = float(input("Enter radius of sphere: "))
        result = 4 * math.pi * (a * a)
        print(f"Volume of sphere with radius {a} is {result}")

