import os 
import ctypes

此處=os.path.dirname(os.path.abspath(__file__))
a=ctypes.WinDLL(os.path.join(此處,'cursor.dll'))
a.init()

def 去頂():
    a.gotoH()

def 去(x,y):
    a.gotoXY(x,y)

def 位置():
    t=a.getXY()
    return t//65536,t%65536

if __name__=='__main__':
    for i in range(4):
        print(i)
    a.gotoH()
    print('哈哈哈')