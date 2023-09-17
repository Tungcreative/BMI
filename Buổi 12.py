n = list(int(num)for num in input('Hãy nhập phép tính: ').split('+'))
n.sort()
n = '+'.join ([str(c)for c in n])
print(n)

print()

n = str(input('Hãy nhập n: '))
m = str(input('Hãy nhập m: '))
o = sorted(n, reverse=True)
o = ''.join([str(c) for c in o])
if m == o:
    print('No')
else:
    print('Yes')

print()

