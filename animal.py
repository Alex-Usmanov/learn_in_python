# coding:utf-8
'''
动物标签(sn):象：8、 狮：7、虎：6、豹：5、狼：4、狗：3、猫：2、鼠：1  空：0
阵营（fraction）：敌我正营，敌为1，我为0

'''
'''
class Canvas():
    def __init__(self, width=7, height=9, clearChar=' ', pixelChar='0'):
        self.width = width
        self.height = height
        self.clearChar = clearChar
        self.pixelChar = pixelChar
        self.initCanvas()

    def initCanvas(self):
        self.canvas = [[self.clearChar] * self.width for i in range(self.height)]

    def display(self):
        for i in self.canvas:
            print ''.join(i)

    def drawPixel(self, x, y):
        # lack of validation
        self.canvas[y][x] = self.pixelChar

'''
class Animal():
    def __init__(self,sn=0,faction=0,location=[]):
        self.sn=sn                # 标签,序列
        self.faction=faction      # 敌我正营，敌为1，我为0
        self.location=location    # 位置

    # 画棋子
    def start(self):
        self.move()

    # 移动步骤
    # '''
    def move(self):
        # print("a：←  d:→  w:↑  s:↓")
        flag=1
        while flag:
        # def operate_left(location):
            operate=raw_input("输入行动（a：←  d:→  w:↑  s:↓）：")
            if(operate=="a"):
                if(self.location[0]==0):
                    print("你已经在最左边上了，再往左会死哦。")
                elif((2<self.sn<7 or self.sn==8)and((self.location[0]==3 or self.location[0]==6)and(2<self.location[1]<5))):
                    print("你的左边是河，跳进去会死哦。")
                     # 一般动物不能过河
                    '''
                elif((2<self.sn<7 or self.sn==8)&((self.location[0]==3) and (2<self.location[1]<5))):
                    print("你的左边是河，跳进去会死哦。")
                elif((2<self.sn<7 or self.sn==8)&((self.location[0]==6) and (2<self.location[1]<5))):
                    print("你的左边是河，跳进去会死哦。")
                    '''
                elif((5<self.sn<8)and((self.location[0]==3 or self.location[0]==6)and(2<self.location[1]<5))):
                    self.location[0]-=3
                    # 狮子老虎可以跳过河
                else:
                    self.location[0]-=1
                    frag=0
            elif(operate=="d"):
                if(self.location[0]==6):
                    print("你已经在最右边上了，再往右会死哦。")
                elif((2<self.sn<7 or self.sn==8)and((self.location[0]==0 or self.location[0]==3)and(2<self.location[1]<5))):
                    print("你的右边是河，跳进去会死哦。")
                     # 一般动物不能过河
                elif((5<self.sn<8)and((self.location[0]==0 or self.location[0]==3)and(2<self.location[1]<5))):
                    self.location[0]+=3
                    # 狮子老虎可以跳过河
                else:
                    self.location[0]+=1
                    flag=0
            elif(operate=="w"):
                if(self.location[1]==8):
                    print("你已经在最前边上了，再往前会死哦。")
                elif((2<self.sn<7 or self.sn==8)and((0<self.location[0]<3 or 3<self.location[0]<6)and(self.location[1]==2))):
                    print("你的前边是河，跳进去会死哦。")
                     # 一般动物不能过河
                elif((5<self.sn<8)and((0<self.location[0]<3 or 3<self.location[0]<6)and(2<self.location[1]==2))):
                    self.location[1]+=4
                    # 狮子老虎可以跳过河
                else:
                    self.location[1]+=1
                    flag=0
            elif(operate=="s"):
                if(self.location[1]==0):
                    print("你已经在最后边上了，再往后会死哦。")
                elif((2<self.sn<7 or self.sn==8)and((0<self.location[0]<3 or 3<self.location[0]<6)and(self.location[1]==6))):
                    print("你的后边是河，跳进去会死哦。")
                    # 一般动物不能过河
                elif((5<self.sn<8)and((0<self.location[0]<3 or 3<self.location[0]<6)and(self.location[1]==6))):
                    self.location[1]-=4
                    # 狮子老虎可以跳过河
                else:
                    self.location[1]-=1
                    flag=0
            else:
                print ("你想去哪里呢？")
        return self.location

    # 判定敌人
    def is_enemy(self,another):
        return self.faction is not another.faction

    # 吃子
    def Eat(self,another):
        if self.is_enemy(another) is False:
            print("这是小伙伴，不可以吃的。重新走一步")
            self.move()
        else:
            if another.trap() is True:
                temp_location=self.location
                self.location=another.location
                another.sn=0
                another.location=temp_location
            else:
                if(self.sn==1 and another.sn==8):
                    if(0<self.location[0]<3 or 3<self.location[0]<6)and(2<self.location[1]<6):
                        print("大笨象在河岸上，小老鼠要跳上去才能吃大象哦。")
                        self.move()
                    else:
                        temp_location=self.location
                        self.location=another.location
                        another.sn=0
                        another.location=temp_location
                elif(self.sn==8 and another.sn==1):
                    print("大笨象，这是老鼠，会钻鼻子里，赶快逃。重新走一步")
                    self.move()
                elif(self.sn>=another.sn):
                    temp_location=self.location
                    self.location=another.location
                    another.sn=0
                    another.location=temp_location
                else:
                    print("笨蛋，你太弱了，吃不了对方。赶快逃命吧。。。")
                    self.move()

    # 陷入陷阱
    def is_trap(self):
        if self.faction is 0:
            if self.location==[7,3]:
                return True
            elif self.location==[8,2]:
                return True
            elif self.location==[8,4]:
                return True
            else:
                return False
        else:
            if self.location==[1,3]:
                return True
            elif self.location==[0,2]:
                return True
            elif self.location==[0,4]:
                return True
            else:
                return False

    # 判定胜利
    def is_win(self):
        if self.faction is 0:
            if self.location==[8.3]:
                print("恭喜小伙伴，你成功进驻了敌人的兽穴，你赢了")
                return 0
            else:
                return 1
        else:
            if self.location==[0,3]:
                print("对不起，你的兽穴已经被进攻，你输了")
                return 0
            else:
                return 1

class Board():
    def __init__(self):
        # self.board=[[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9]
        self.board=[[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7]

    def show(self):
        for r in self.board:
                print r

    def locate(self,Animal):
        # dict=[' ','鼠','猫','狗','狼','豹','虎','狮','象']
        if Animal.location[0]<9:
            self.board[Animal.location[1]][Animal.location[0]]=Animal.sn
            # self.board[Animal.location[1]][Animal.location[0]]=dict[Animal.sn]


def game():
    # 初始化棋子的位置数据
    mouse0=Animal(1,0,[0,2])
    cat0=Animal(2,0,[2,2])
    dog0=Animal(3,0,[1,1])
    wolf0=Animal(4,0,[4,2])
    leopard0=Animal(5,0,[2,2])
    tiger0=Animal(6,0,[6,0])
    lion0=Animal(7,0,[0,0])
    elephant0=Animal(8,0,[6,2])

    mouse1=Animal(1,1,[6,6])
    cat1=Animal(2,1,[1,7])
    dog1=Animal(3,1,[2,6])
    wolf1=Animal(4,1,[2,2])
    leopard1=Animal(5,1,[4,6])
    tiger1=Animal(6,1,[0,8])
    lion1=Animal(7,1,[6,8])
    elephant1=Animal(8,1,[0,6])

    #target=input()
    goon=1    # 继续标志
    player=1  # 下棋方标志
    board=Board()
    board.show()
    print "——————————现在开始下棋啦————————————"

    while goon:
        board.locate(mouse0)
        board.locate(cat0)
        board.locate(dog0)
        board.locate(wolf0)
        board.locate(leopard0)
        board.locate(tiger0)
        board.locate(lion0)
        board.locate(elephant0)

        board.locate(mouse1)
        board.locate(cat1)
        board.locate(dog1)
        board.locate(wolf1)
        board.locate(leopard1)
        board.locate(tiger1)
        board.locate(lion1)
        board.locate(elephant1)

        board.show()

        chess=input("你要走哪只棋子呢？:")
        chess.move()
        goon=chess.is_win()
        print "_____________________________"



if __name__ =='__main__':
    game()
