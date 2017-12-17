import os
def pinst(*d):
    a=''
    for i in d:
        a+=' '+i
    os.system('pip install'+a)

