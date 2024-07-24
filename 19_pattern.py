#square pattern
n=5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()
#triangle pattern
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()
#reverse triangle
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()
#right side triangle
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
#upside down right side triangle
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
#printing proper triangle
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
#printing upside down triangle
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
#diamond pattern
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
#letter H
for i in range(n):
    for j in range(n):
        if(
            print('* ',end=' ')
        else:
            print(' ',end=' ')
    print()
