import sys

if sys.argv[3] == 'plus':
    print('Output:', int(sys.argv[1]) + int(sys.argv[2]))
elif sys.argv[3] == 'minus':
    print('Output:', int(sys.argv[1]) - int(sys.argv[2]))
elif sys.argv[3] == 'multiply':
    print('Output:', int(sys.argv[1]) * int(sys.argv[2]))
elif sys.argv[3] == 'divide':
    print('Output:', int(sys.argv[1]) / int(sys.argv[2]))
else:
    print('You put wrong argrument!! (plus,minus,multiply,divide)')

