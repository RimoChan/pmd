import os,sys
import shlex
import 光標
import 命令
os.system('title pmd')

while True:
    p=光標.位置()
    光標.去頂()
    print('#'*60)
    s='Path= %s   '%os.getcwd()
    print('%s%s'%(s,'#'*(60-len(s))))
    print('#'*60)
    光標.去(*p)
    if 光標.位置()[1]<3:
        光標.去(0,3)


    t=input('>>')
    try:
        k=eval(t)
        if k!=None:
            print(k)
    except:
        try:
            exec(t)
        except:
            try:
                os.chdir(t)
            except:
                try:
                    a=shlex.split(t.replace('\\','/'))
                    m=eval('命令.%s'%a[0])
                except BaseException as e:
                    m=None
                    os.system(t)
                if m:
                    try:
                        m(*a[1:])
                    except BaseException as e:
                        print(e)