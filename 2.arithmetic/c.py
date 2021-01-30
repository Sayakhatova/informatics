x=int(input())
Thenext='The next number for the number {} is {}.'
prev='The previous number for the number {} is {}.'
print(Thenext.format(x, x+1))
print(prev.format(x, x-1))