#!/usr/bin/env python3


# Calculating square of a figure (rectangle, circle, triangle)

def digits_check(num):
    flag = True
    for c in num:
        if c.isdigit() == False:
            if c != '.':
                flag = False
    return flag

def number_call():
    while True:
        number = input('Enter a number in format 12.345: ')
        if number == '' or not digits_check(number):
            print('Please try again.')
            continue
        else:
            return float(number)

def shape_sq():
    shapes = {'rectangle', 'triangle', 'circle'}
    answ = True
    while answ:
        answ = input('To start (start again) press "y" or press any button to exit: ')
        if not answ == 'y':
            print('Exiting...')
            print('Exited')
            break
        else:
            shape = input('Enter a figure shape [rectangle, circle, triangle]: ')
            shape = shape.lower()
            if shape not in shapes:
                print('Please enter one of 3 forms [rectangle, circle, triangle]')
                continue
            else:
                if shape == 'triangle':
                    sizes1 = ['A', 'B', 'C']
                    a1 = []
                    for i in range(len(sizes1)):
                        print(f'Please enter size {sizes1[i]}.')
                        a1.append(number_call())
                    p = (a1[0] + a1[1] + a1[2]) / 2
                    print(f"Triangle's square is {(p * (p - a1[0]) * (p - a1[1]) * (p - a1[2])) ** 0.5}")
                elif shape == 'rectangle':
                    sizes2 = ['A', 'B']
                    a2 = []
                    for i in range(len(sizes2)):
                        print(f'Please enter size {sizes2[i]}.')
                        a2.append(number_call())
                    print(f"Rectangle's square is {a2[0] * a2[1]}")
                elif shape == 'circle':
                    print(f'Please enter radius.')
                    r = number_call()
                    print(f"Circle's square is {3.14 * r ** 2}")

shape_sq()

