#Terminal TicTacToe
import sys
from board import Board

#Menu displayed
def menu() -> None:
    opt = 0
    while opt != 2:
        print('What do you want to do?\n')
        print('1. Play\n2.Leave\n')
        try:
            opt = int(input())
        except ValueError:
            print('Please introduce a number')
        if opt == 1:
            pass
        elif opt == 2:
            pass
        else:
            print('Goodbye!')
            sys.exit()

if __name__ == '__main__':
    print('Welcome to TicTacToe')
    # menu()
    b = Board()
    b.play()
    
