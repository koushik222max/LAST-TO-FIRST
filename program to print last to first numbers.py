def countdown(n):
    if n==0:
        print('last number')

    else:
        print(n)
        countdown(n-1)

countdown(5)

print('')

for i in range(5,-1,-1):
    if i==0:
        print('This is the last number')
    else:
        print(i)
