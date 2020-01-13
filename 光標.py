import ctypes
a=ctypes.WinDLL('./cursor.dll')

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