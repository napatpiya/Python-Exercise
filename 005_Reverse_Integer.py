import sys

x = sys.argv[1]

if int(sys.argv[1]) < 0:
    res = '-'
    num = int(len(sys.argv[1])-1)
    for i in range(len(sys.argv[1])-1):
        res = res + x[num]
        num = num - 1
else:
    res = ''
    num = int(len(sys.argv[1])-1)
    for i in range(len(sys.argv[1])):
        res = res + x[num]
        num = num -1
print('Output:', int(res))
