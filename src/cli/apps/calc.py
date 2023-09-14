def evaluate_equ(equ: str):
    try:    
        print(f'{equ} =',
                f'{round(eval(equ), 4)}')            
    except ZeroDivisionError:
        print('You cannot divide by 0')
    except NameError:
        print('Invalid Expression')
    except TypeError:
        print('Invalid Expression')

        

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
        a = float(input('Enter the radius of circle: '))
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
    a: float
    b: float
    
    """
    cube
    circle
    rectangular prism
    """    
    
    if shape in 'cube':
        a = float(input("Enter side length of cube: "))
        print(a * a * a)
    
    