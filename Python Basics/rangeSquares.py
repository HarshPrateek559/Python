def qrange(n):
    for i in range(1, n+1):
        yield i * i


n = int(input("Input the number to get squares: "))
print('Squares of numbers from 1 to %d are' % (n ), end =":")
for i in qrange(n):
    print(i, end=" ")
