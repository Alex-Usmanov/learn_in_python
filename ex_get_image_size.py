# coding:utf-8
import os

pic_dir="F://NRG//lab//python//TryPyhtonGame//image"
filelist=[]
# filename="F:\\NRG\\lab\\python\\TryPythonGame\\image\\3.jpg"  win8
# filename="F://NRG//lab//python//TryPyhtonGame//image//3.jpg"  win7

def get_jpg_size(jpg_file):
    img=jpg_file.read()
    # print(img.encode('hex'))
    print jpg_file
    lst=str(img.encode('hex'))
    print lst
    mark_SOF0=lst.index('ffc0')
    img_height=int(str(lst[mark_SOF0+10:mark_SOF0+14]),16)
    img_width=int(str(lst[mark_SOF0+14:mark_SOF0+18]),16)

    print img_width,"x",img_height

    if img_height<=img_width:
        filelist.append(pic)
    jpg_file.close()

    return (img_width,img_height)

def get_png_size(png_file):
    img=png_file.read()
    # print(img.encode('hex'))
    lst=str(img.encode('hex'))
    print lst
    # mark_head=lst.index('0000004c')
    # print mark_head #32
    img_width=int(str(lst[32:40]),16)
    img_height=int(str(lst[40:48]),16)

    print img_width,"x",img_height

    if img_height<=img_width:
        filelist.append(pic)
        newBMP=open(str(pic.replace('png','bmp')),'w')
        newBMP.write(img)
        newBMP.close()
    return (img_width,img_height)

for pic in os.listdir(pic_dir):
    # print pic
    mark_dot=pic.index('.')
    pic_path=os.path.join(pic_dir,pic)
    with open(pic_path,'rb') as f:
        if pic[mark_dot+1:]=='jpg':
            print pic
            get_jpg_size(f)
        if pic[mark_dot+1:]=='png':
            print pic
            result=get_png_size(f)
            pic.replace('png','bmp')

print filelist

'''
# by the test,I want to figure out the difference between PNG and BMP but fail
def test1():
    for pic in os.listdir(pic_dir):
        # print pic
        mark_dot=pic.index('.')
        pic_path=os.path.join(pic_dir,pic)

        with open(pic_path,'rb') as f:
            if pic[mark_dot+1:]!='jpg':
                print pic
                get_png_size(f)

def test2():
    print "*"*10+"test2"+"*"*10
    f1='F://NRG//lab//python//TryPyhtonGame//image//name.png'
    f2='F://NRG//lab//python//TryPyhtonGame//image//name_bmp0.bmp'
    f3='F://NRG//lab//python//TryPyhtonGame//image//name_bmp16.bmp'
    f4='F://NRG//lab//python//TryPyhtonGame//image//name_bmp24.bmp'
    f5='F://NRG//lab//python//TryPyhtonGame//image//name_bmp256.bmp'
    lst1=open(f1,'rb+').read().encode('hex')
    print lst1
    lst2=open(f2,'rb+').read().encode('hex')
    print lst2
    lst3=open(f3,'rb+').read().encode('hex')
    print lst3
    lst4=open(f4,'rb+').read().encode('hex')
    print lst4
    lst5=open(f5,'rb+').read().encode('hex')
    print lst5


    lst1_2=int(str(lst1),16)-int(str(lst2),16)
    print "lst1_2: "+str(lst1_2)
    lst1_3=int(str(lst1),16)-int(str(lst3),16)
    print "lst1_3: "+str(lst1_3)
    lst1_4=int(str(lst1),16)-int(str(lst4),16)
    print "lst1_4: "+str(lst1_4)
    lst1_5=int(str(lst1),16)-int(str(lst5),16)
    print "lst1_5: "+str(lst1_5)

    print "*"*10

    ff1='F://NRG//lab//python//TryPyhtonGame//image//yezi0.png'
    ff2='F://NRG//lab//python//TryPyhtonGame//image//yezi0_bmp0.bmp'
    ff3='F://NRG//lab//python//TryPyhtonGame//image//yezi0_bmp16.bmp'
    ff4='F://NRG//lab//python//TryPyhtonGame//image//yezi0_bmp24.bmp'
    ff5='F://NRG//lab//python//TryPyhtonGame//image//yezi0_bmp256.bmp'
    llst1=open(f1,'rb+').read().encode('hex')
    print llst1
    llst2=open(f2,'rb+').read().encode('hex')
    print llst2
    llst3=open(f3,'rb+').read().encode('hex')
    print llst3
    llst4=open(f4,'rb+').read().encode('hex')
    print llst4
    llst5=open(f5,'rb+').read().encode('hex')
    print llst5


    llst1_2=int(str(llst1),16)-int(str(llst2),16)
    print "lst1_2: "+str(llst1_2)
    llst1_3=int(str(llst1),16)-int(str(llst3),16)
    print "lst1_3: "+str(llst1_3)
    llst1_4=int(str(llst1),16)-int(str(llst4),16)
    print "lst1_4: "+str(llst1_4)
    llst1_5=int(str(llst1),16)-int(str(llst5),16)
    print "lst1_5: "+str(llst1_5)

    print "name-yezi0"+"*"*10
    lst1_1=int(str(lst1),16)-int(str(llst1),16)
    print "lst1_1: "+str(lst1_1)
    lst2_2=int(str(lst2),16)-int(str(llst2),16)
    print "lst2_3: "+str(lst2_2)
    lst3_3=int(str(lst3),16)-int(str(llst3),16)
    print "lst3_3: "+str(lst3_3)
    lst4_4=int(str(lst4),16)-int(str(llst4),16)
    print "lst4_4: "+str(lst4_4)
    lst5_5=int(str(lst5),16)-int(str(llst5),16)
    print "lst5_5: "+str(lst5_5)

    print "name+yezi0"+"*"*10
    llst1_1=int(str(lst1),16)-int(str(lst1_1),16)
    print "llst1_1: "+str(llst1_1)
    llst2_2=int(str(lst2),16)-int(str(lst2_2),16)
    print "llst2_3: "+str(llst2_2)
    llst3_3=int(str(lst3),16)-int(str(lst3_3),16)
    print "llst3_3: "+str(llst3_3)
    llst4_4=int(str(lst4),16)-int(str(lst4_4),16)
    print "llst4_4: "+str(llst4_4)
    llst5_5=int(str(lst5),16)-int(str(lst5_5),16)
    print "llst5_5: "+str(llst5_5)

if __name__=='__main__':
    test2()
    
'''
