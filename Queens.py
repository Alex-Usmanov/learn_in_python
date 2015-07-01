# coding:utf-8

SIZE=8
CHESSBOARD=[[0 for col in range(SIZE)] for row in range(SIZE)]

class Queen():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def queen_attack_area(self,chessboard):
        # mark chess borad row (x)
        for i in range(SIZE):
            chessboard[self.x][i]=1
            chessboard[i][self.y]=1
            chessboard[(self.x+i)%SIZE][(self.y+i)%SIZE]=1
            chessboard[(self.x+self.y)%SIZE-i][i]=1


        for row in chessboard:
            print row

        return chessboard


def test0():
    q=Queen(2,2)
    q.queen_attack_area(CHESSBOARD)
    # chessboard[(self.x+self.y)%SIZE-i][i]=1
    '''
[1, 0, 1, 0, 1, 0, 0, 0]
[0, 1, 1, 1, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 0, 0, 0, 0]
[1, 0, 1, 0, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 1, 0, 1]
[0, 0, 1, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 1, 0, 1]
    '''

def test1():
    q=Queen(1,3)
    q.queen_attack_area(CHESSBOARD)
'''
[0, 0, 1, 1, 1, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 1, 1, 1, 0, 0, 0]
[0, 1, 0, 1, 0, 1, 0, 0]
[1, 0, 0, 1, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 0, 0, 1]
[1, 0, 0, 1, 0, 0, 1, 0]
[0, 1, 0, 1, 0, 1, 0, 0]

'''
if __name__=='__main__':
    test1()
