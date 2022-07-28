class Board:

     #Game board
     bo = [
          ['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']
          ]

     def __init__(self) -> None:
          self.current = 'X'
          self.remaining = 9
          self.ending = ''
     
     def printBoard(self):
          print('| {} | {} | {} |'.format(self.bo[0][0], self.bo[0][1], self.bo[0][2]))
          print(' --- --- ---')
          print('| {} | {} | {} |'.format(self.bo[1][0], self.bo[1][1], self.bo[1][2]))
          print(' --- --- ---')
          print('| {} | {} | {} |'.format(self.bo[2][0], self.bo[2][1], self.bo[2][2]))
          print(' --- --- ---')

     def checkEnding(self):
          c = self.current
          #Horizontal wins
          for r in self.bo:
               if r == [c, c, c]:
                    return c
          
          #Vertical Wins
          for i in range(3):
               if self.bo[0][i] == c and self.bo[1][i] == c and self.bo[2][i] == c:
                    return c
          
          #Diagonal wins
          if self.bo[0][0] == c and self.bo[1][1] == c and self.bo[2][2] == c:
               return c
          elif self.bo[0][2] == c and self.bo[1][1] == c and self.bo[2][0] == c:
               return c
          
          if self.boardFull():
               return 'tie'

          return 

     def boardFull(self) -> bool:
          for i in self.bo:
               for xy in i:
                    if xy in ['1','2','3','4','5','6','7','8','9']:
                         return False
          return True

     def emptyCell(self, n):
          if n in [1,2,3]:
               if self.bo[0][n-1] in ['1','2','3','4','5','6','7','8','9']:
                    return True
          elif n in [4,5,6]:
               if self.bo[1][(n%3)-1] in ['1','2','3','4','5','6','7','8','9']:
                    return True
          else:
               if self.bo[2][(n%6)-1] in ['1','2','3','4','5','6','7','8','9']:
                    return True
          return False
     
     def addToBoard(self, n, curr):
          if n in [1,2,3]:
               self.bo[0][n-1] = curr
          elif n in [4,5,6]:
               self.bo[1][(n%3)-1] = curr
          else:
               self.bo[2][(n%6)-1] = curr


     def next(self, curr):
          if curr == 'X':
               return 'O'
          else:
               return 'X'
     
     def theEnd(self, result):
          if result == 'tie':
               self.printBoard()
               print('\n YOU TIED!\n')
          else:
               self.printBoard()
               print('\nPLAYER {} WON!\n'.format(result))
     
     def play(self):
          n = 0
          while True:
               self.printBoard()
               print('Player {}\'s turn\nChoose an available number\n'.format(self.current))
               while n not in [1,2,3,4,5,6,7,8,9]:
                    try:
                         n = int(input('Where do you want to write {}\n'.format(self.current)))
                    except ValueError:
                         print('You need to pick a number')
                    if n <= 0 or n >= 10:
                         print('The number has to be from 1 to 9, choose another number')
                         n=0
                    else:
                         if self.emptyCell(n):
                              self.addToBoard(n,self.current)
                              break
                         else:
                              print('That cell is not available, try again')
                              n=0
               e = self.checkEnding()
               if e == None:   
                    self.current = self.next(self.current)
                    self.remaining -= 1
                    n = 0
               else: 
                    break
          
          self.theEnd(e)