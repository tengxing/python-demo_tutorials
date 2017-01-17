import os,os.path
import shutil,string

dir = "tensor"
outdir = "tensor"
label = "1"

fileList = os.listdir(dir)
#file = os.mkdir("data")

fileinfo = open("list.csv","w")

for i in fileList:
    curname = os.path.join(outdir,i)
    print curname
    fileinfo.write(curname+"\t1"+"\n")
fileinfo.close()