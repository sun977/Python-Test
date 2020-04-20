import os;

def rename():
    count = 1; #文件名自增器
    path = input("Input the path:"); #输入文件夹路径
    newname = input("Input new filename:"); #输入新的文件名
    newfiletype = input("Input new filetype:"); #输入新的文件类型

    filelist = os.listdir(path) #文件夹下所有的文件
    for files in filelist: 
        olddir = os.path.join(path,files);
        if os.path.isdir(olddir): #跳过文件夹
            continue;
        #filename = os.path.splitext(files)[0] #文件名
        #filetype = os.path.splitext(files)[1] #文件后缀名
        newdir = os.path.join(path,newname+'_'+str(count)+'.'+newfiletype);#新文件路径
        os.rename(olddir,newdir);#重命名
        count +=1;
    print("Rename Successfully !");  

rename();

