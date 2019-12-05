import sys

Total = int(sys.argv[1])
for i in range(int(sys.argv[2]) - 1):
    Total = Total * int(sys.argv[1])
    i = i + 1

print('Output:', Total)