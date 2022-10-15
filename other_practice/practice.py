#practice
#2022/10/4
# #author:linxu
# num=[i**3 for i in range(1,11)]
# print(num)
'''
需求  给你个目录，目录里有几张图片文件
1. 打印出所有文件的文件名
2. 打印出文件数量
3. 扔几个视频进去，打印出视频和图片各有多少个
4. 给所有文件重命名为“linxu_序号”
5. 按照不同的文件类型，分成不同的目录，不存在的目录用代码创建，剪切文件
视频文件夹   图片文件夹  pdf文件夹
第5.5题，你把目录改活。现在目录写死了
6. 打印所有目录(视频目录，图片目录等)  下的所有文件
打印出类似于这样的树型结构
--视频目录
---------video_001.avi
---------video_002.mp4
--图片目录
---------img_001.jpg
---------img_002.png
第七题 知识点try-catch
捕获异常后删除已经创建的目录（还原执行前的目录结构），并且打印，程序有误
第8题: 所有功能
都写一个函数里，
webp，png, pdf等
同样的逻辑写了好几个两个if太啰嗦了，
抽象拆成一个函数
'''
import os
import re
import shutil

jpg_num=0
move_list=[]
path='C:\\Users\\linxu\\Desktop\\testImag'
listpath=os.listdir(path)
for i in listpath:
    if not os.path.isdir(i):
        filename,filetype=i.split('.')
        os.rename(os.path.join(path,i),os.path.join(path,"linxu_page" + str(jpg_num)+'.'+filetype))
        jpg_num= jpg_num + 1
        os.chdir(path)
        move_list.append(i)
        if not os.path.exists(filetype):
            os.mkdir(filetype)
            print(f"{filetype}目录创建成功")
    for move_file in move_list:
        source = path + '\\' + move_file
        destination = path + '\\' + filetype
        move_file=move_file[:-1]
        print(source+'\n'+destination)
        shutil.move(source,destination)
        print(f"{filetype}文件移动成功")
        print(source+'\n'+destination)
print(f"文件夹下所有的文件个数为{len(listpath)}")

