# coding:utf-8

SIZE=4
CHESSBOARD=[[0 for col in range(SIZE)] for row in range(SIZE)]
queens=[]
# size_queens=[]

class Queen():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def queen_attack_area(self,chessboard):
        # mark chess board row (x)
        for i in range(SIZE):
            chessboard[self.x][i]=1
            chessboard[i][self.y]=1
            # chessboard[(self.x+i)%SIZE][(self.y+i)%SIZE]=1
            # chessboard[(self.x+self.y)%SIZE-i][i]=1
        if self.x+self.y<SIZE:
            for i in range(self.x+self.y+1):
                chessboard[self.x+self.y-i][i]=1
                # (0,14)(1,13)(2,12)(3,11)(4,10)
        else:
            for i in range(self.x+self.y-SIZE+1,SIZE):
                chessboard[i][self.x+self.y-i]=1
                # (2,14)(3,13)(4,12)(5,11)(6,10)

        if self.x>self.y:
            for j in range(SIZE+self.y-self.x):
                chessboard[self.x+j-self.y][j]=1
                # (1,0)(2,1)(3,2)(4,3)(5,4)
        else:
            for j in range(SIZE+self.x-self.y):
                chessboard[j][self.y-self.x+j]=1
                # (0,1)(1,2)(2,3)(3,4)(4,5)

        chessboard[self.x][self.y]=2

        '''
        for row in chessboard:
            print row
        '''
        return chessboard

def print_split_line():
    print "》"*SIZE*4

def print_chessboard(chessboard):
    for row in chessboard:
        print row

def set_queens(chessboard=CHESSBOARD):
    for i in range(SIZE):
        for j in range(SIZE):
            if not chessboard[i][j]:
                tempQueen=Queen(i,j)
                queens.append([i,j])
                chessboard=tempQueen.queen_attack_area(chessboard)
                set_queens(chessboard)
    return queens


def set_first_queens(first_queen=Queen(0,0),chessboard=CHESSBOARD):
    # first_queen=Queen(0,0)
    # queens=[]
    size_queens=[]
    x,y=first_queen.x,first_queen.y
    print x,y
    size_queens.append([x,y])
    x_mark=first_queen.x
    chessboard=first_queen.queen_attack_area(chessboard)
    for i in range(x_mark+1,SIZE):
        x_mark+=1
        for j in range(SIZE):
            if not chessboard[i][j]:
                tempQueen=Queen(i,j)
                # queens.append([i,j])
                size_queens.append([i,j])
                chessboard=tempQueen.queen_attack_area(chessboard)
                set_first_queens(tempQueen,chessboard)
    if len(size_queens)!=SIZE:
        if y<SIZE-1:
            # size_queens=[]
            set_first_queens(Queen(x,y+1),chessboard=CHESSBOARD)
        else:
            print "Sorry,I can't..."
    # else:
    return size_queens

def test3():
    print set_queens()
    print set_first_queens()


def test0():
    q=Queen(6,7)
    q.queen_attack_area(CHESSBOARD)
    # chessboard[(self.x+self.y)%SIZE-i][i]=1

def test1():
    q=Queen(1,3)
    q.queen_attack_area(CHESSBOARD)

if __name__=='__main__':
    # test0()
    print_split_line()
    # test1()
    test3()
