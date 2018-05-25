# -*- coding: UTF-8 –*-
### 
#实现Linux下文件全备份和差异备份
#python 2.7
#version 1.0
#2018.4.12
###
import time
import os
import sys
import cPickle

fileInfo = {}

#记录日志
def logger(time,fileName,status,fileNum):
    f = open('backup.log','a')
    f.write("%s\t%s\t%s\t\t%s\n" % (time,fileName,status,fileNum))

##打包
def tar(sDir,dDir,fileNum):
    command = "tar zcf %s  %s >/dev/null 2>&1" % (dDir + ".tar.gz",sDir)
    ##判断打包命令有没有执行成功
    if os.system(command) == 0:
        logger(time.strftime('%F %X'),dDir + ".tar.gz",'success',fileNum)
    else:
        logger(time.strftime('%F %X'),dDir + ".tar.gz",'failed',fileNum)
##全备份
def fullBak(path):
    fileNum = 0
    #遍历文件
    for root,dirs,files in os.walk(path):
        for name in files:
            file = os.path.join(root, name)
            #mtime在写入文件时随文件内容的更改而更改
            mtime = os.path.getmtime(file)
            #在写入文件、更改所有者、权限或链接设置时随Inode的内容更改而更改
            ctime = os.path.getctime(file)
            # 文件时间信息存入字典
            fileInfo[file] = (mtime,ctime)
            fileNum += 1
    f = open(P,'w')
    #将文件字典信息从内存写入文件
    cPickle.dump(fileInfo,f)
    f.close()
    #将需要备份的文件打包
    tar(S,D,fileNum)

##差异备份
def diffBak(path):
    for root,dirs,files in os.walk(path):
        for name in files:
            file = os.path.join(root,name)
            mtime = os.path.getmtime(file)
            ctime = os.path.getctime(file)
            fileInfo[file] = (mtime,ctime)
    if os.path.isfile(P) == 0:
        f = open(P,'w')
        f.close()
    if os.stat(P).st_size == 0:
        f = open(P,'w')
        cPickle.dump(fileInfo,f)
        fileNum = len(fileInfo.keys())
        f.close()
        print fileNum
        tar(S,D,fileNum)
    else:
        f = open(P)
        old_fileInfo = cPickle.load(f)
        f.close()
        difference = dict(set(fileInfo.items())^set(old_fileInfo.items()))
        fileNum = len(difference)
        print fileNum
        difference_file = ' '.join(difference.keys())
        print difference_file
        tar(difference_file,D,fileNum)
        f = open(P,'w')
        cPickle.dump(fileInfo,f)
        f.close()

def Usage():
    print '''
        Syntax:  python backcup.py pickle_file model source_dir filename_bk
            model:  1:Full backup 2:Differential backup
        example: python backup.py fileinfo.pk 2 /etc etc_$(date +%F)
            explain:  Automatically add '.tar.gz' suffix
    '''
    sys.exit()
##固定备份某文件时，可将下列参数写死，放在定时任务只执行
if len(sys.argv) != 5:
    Usage()
P = sys.argv[1]
M = int(sys.argv[2])
S = sys.argv[3]
D = sys.argv[4]
if M == 1:
    fullBak(S)
elif M == 2:
    diffBak(S)
else:
    print "\033[;31mDoes not support this mode\033[0m"
    Usage()