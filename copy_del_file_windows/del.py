#coding=utf-8
import os
import shutil 

#递归复制文件夹内的文件
def copyFiles(sourceDir,targetDir): 
    #忽略某些特定的子文件夹
    if sourceDir.find("exceptionfolder")>0: 
        return 
    #列出源目录文件和文件夹
    for file in os.listdir(sourceDir): 
        #拼接完整路径
        sourceFile = os.path.join(sourceDir,file) 
        targetFile = os.path.join(targetDir,file) 

        #如果是文件则处理
        if os.path.isfile(sourceFile): 
            #如果目的路径不存在该文件就创建空文件,并保持目录层级结构
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            #如果目的路径里面不存在某个文件或者存在那个同名文件但是文件有残缺，则复制，否则跳过
            if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
                print (targetFile+" copy succeeded")

        #如果是文件夹则递归
        if os.path.isdir(sourceFile): 
            copyFiles(sourceFile, targetFile)

#遍历某个目录及其子目录下所有文件拷贝到某个目录中
def copyFiles2(srcPath,dstPath): 
    if not os.path.exists(srcPath): 
        print ("src path not exist!") 
    if not os.path.exists(dstPath): 
        os.makedirs(dstPath)  
    #递归遍历文件夹下的文件，用os.walk函数返回一个三元组
    for root,dirs,files in os.walk(srcPath): 
        for eachfile in files: 
            shutil.copy(os.path.join(root,eachfile),dstPath) 
            print( eachfile+" copy succeeded")


#删除某目录下特定文件
def removeFileInDir(sourceDir):
    for file in os.listdir(sourceDir):
        file=os.path.join(sourceDir,file) #必须拼接完整文件名
        if os.path.isfile(file) and file.find(".txt")>0:
            os.remove(file)
            print( file+" remove succeeded" )

if  __name__ =="__main__": 
    copyFiles("./dir1","./dir2")
    removeFileInDir("./dir1")
 
