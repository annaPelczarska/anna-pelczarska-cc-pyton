import sys

if len(sys.argv) < 2:
    print('Hello World!')
else:
    i = 0
    while(i < len(sys.argv)):
        print('Hello ' + sys.argv[i] + '!')
        i = i + 1

print(len(sys.argv))
