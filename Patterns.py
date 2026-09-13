n=int(input('Enter a Number: '))

def right_angle_triangle(n):
    print("Right angle triangle")
    for i in range(0,n+1):
        for j in range(0,i):
            print('*',end=' ')
        print()

def inverted_right_angle(n):
    print("Inverted right angle triangle")
    for i in range(0,n+1):
        for k in range(0,n-i):
            print(' ',end=' ')
        for j in range(0,i):
            print('*', end=' ')
        print()

def reverse_right_angle(n):
    print("Reverse right angle triangle")
    for i in range(n,0,-1):
        for j in range(0,i):
            print('*',end=' ')
        print()

def reverse_inverted_right_angle(n):
    print("Reverse inverted right angle triangle")
    for i in range(n,0,-1):
        for k in range(0,n-i):
            print(' ',end=' ')
        for j in range(0,i):
            print('*', end=' ')
        print()

def pyramid(n):
    print('Pyramid')
    for i in range(0,n+1):
        for k in range(0,n-i):
            print(' ',end=' ')
        for j in range(i*2-1):
            print('*',end=' ')
        print()

def inverted_pyramid(n):
    print('Inverted Pyramid')
    for i in range(n,0,-1):
        for k in range(n-i):
            print(' ',end=' ')
        for j in range(1,i*2):
            print('*', end=' ')
        print()

def diamond(n):
    print('Diamond')
    for i in range(0,n):
        for k in range(0,n-i):
            print(' ', end=' ')
        for j in range(i*2-1):
            print('*', end=' ')
        print()
    for i in range(n,0,-1):
        for k in range(n-i):
            print(' ', end=' ')
        for j in range(1,i*2):
            print('*', end=' ')
        print()
            

right_angle_triangle(n)
inverted_right_angle(n)
reverse_right_angle(n)
reverse_inverted_right_angle(n)
pyramid(n)
inverted_pyramid(n)
diamond(n)