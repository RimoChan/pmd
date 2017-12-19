import os
import shlex

import 光標
os.system('title pmd')

def 跑命令(字串):
    import 命令
    if os.path.isdir(字串):
        os.chdir(字串)
        return
        
    a=shlex.split(字串.replace('\\','/'))
    首=a[0]
    if 首 in dir(命令):
        try:
            m(*a[1:])
        except BaseException as e:
            print(e)
    elif os.path.isfile(首) and 首.split('.')[-1]=='py':            
        os.system('python '+字串)
    else:
        os.system(字串)
    
def 畫上條(): 
    p=光標.位置()
    光標.去頂()
    print('#'*60)
    s='Path= %s   '%os.getcwd()
    print('%s%s'%(s,'#'*(60-len(s))))
    print('#'*60)
    光標.去(*p)
    if 光標.位置()[1]<3:
        光標.去(0,3)

while True:
    畫上條()

    _输入=input('>>')
    try:
        _=eval(_输入)
        if _!=None:
            print(_)
    except:
        try:
            exec(_输入)
        except:
            跑命令(_输入)
