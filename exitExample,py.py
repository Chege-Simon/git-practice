import sys

while True:
    print('Type leave to exit')
    response = input()
    if response == 'leave':
        sys.exit()
    print('You typed ' + response + '.')
