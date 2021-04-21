theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
i = 0
turn = 'X'
def myBoard():
    print(theBoard['top-L']+'|'+theBoard['top-M']+'|'+theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L']+'|'+theBoard['low-M']+'|'+theBoard['low-R'])

while i <= 9:
    if turn == 'X':
        Location = input("Enter the location of the X: ")
        theBoard[Location] = 'X'
        if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == theBoard[Location]:
            print("You won " + theBoard['top-L'])
            break
        elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] == theBoard[Location]:
            print("You won " + theBoard['mid-L'])
            break
        elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == theBoard[Location]:
            print("You won " + theBoard['low-L'])
            break
        elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == theBoard[Location]:
            print("You won " + theBoard['top-L'])
            break
        elif theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == theBoard[Location]:
            print("You won " + theBoard['top-R'])
            break
        elif theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == theBoard[Location]:
            print("You won " + theBoard['top-m'])
            break
        else:
            i = i + 1
            turn = 'O'
            print(myBoard())
    else:
        Location = input("Enter the location of the O:")
        theBoard[Location] = 'O'
        if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == theBoard[Location]:
            print("You won " + theBoard['top-L'])
            break
        elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] == theBoard[Location]:
            print("You won " + theBoard['mid-L'])
            break
        elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == theBoard[Location]:
            print("You won " + theBoard['low-L'])
            break
        elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == theBoard[Location]:
            print("You won " + theBoard['top-L'])
            break
        elif theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == theBoard[Location]:
            print("You won " + theBoard['top-R'])
            break
        elif theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == theBoard[Location]:
            print("You won " + theBoard['top-m'])
            break
        else:
            i = i + 1
            turn = 'X'
            print(myBoard())
        if i == 9:
            print("No one won.")


