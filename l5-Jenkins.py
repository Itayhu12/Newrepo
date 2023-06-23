import shutil
import os
import sys


def freespace():
    total, used, free = shutil.disk_usage("c:\\")
    print("drive c:\\")
    print("Total: %d GiB" % (total // (2 ** 30)))
    print("Used: %d GiB" % (used // (2 ** 30)))
    print("Free: %d GiB" % (free // (2 ** 30)))

def movefile():
    os.rename('C:\\users\itay\desktop\\newfile.txt', "C:\\users\itay\documents\\newfile.txt")


def createfile():

    f = open('c:\\users\itay\desktop\\newfile.txt','w')
    f.write('This is my test')
    f.close()

def readfile():
    f = open('c:\\users\itay\desktop\\newfile.txt','r')
    print(f.readline())

if sys.argv[1] == '--readfile':
    readfile()
elif sys.argv[1] == '--movefile':
    movefile()
elif sys.argv[1] == '--freespace':
    freespace()
elif sys.argv[1] == '--createfile':
    createfile()
else:
    print('must have one of this argumants : \n--readfile\n--createfile\n--movefile\n--freespace')

