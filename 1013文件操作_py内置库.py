import os
import os.path

    # read([size]) 读取至结束，返回文件整体字符串
    # readline([size]) 读取整行内容，返回该行字符串
    # readlines([size]) 读取所有行，返回字符串列表
    # write([str]) 写入参数字符串
    # writelines(seq) 写入参数序列（如列表等）
    # 文件其他操作 -- 查书

    # 目录操作
    # os.getcwd() 获取当前目录位置
    # os.makedirs(path,mode) 创建子目录
    # os.renames(oldpath,newpat) 目录重命名
    # os.listdir(path) 获取目录下所有内容（文件和目录）的列表
    # os.rmdir(path) 删除空目录
    # os.removedir(path) 删除目录
    # os.rename(path) 目录重命名
    # os.walk(path) 遍历文件夹，返回生成器三元组对象
    # os.path.abspath(path) 返回path规范化的绝对路径
    # os.path.split(path) 返回目录和文件名二元组
    # os.path.basename(path) 返回文件名
    # os.path.commonprefix(list) 返回列表中所有path共有的最长路径
    # os.path.exists(path) 返回是否存在该路径
    # os.path.isfile(path) 返回path是否存在的文件
    # os.path.isdir(path) 返回path是否存在的目录
    # os.path.splittext(path) 返回文件名和其拓展名二元组
    # os.path.getsize(path) 返回path的文件的大小
if False:
    with open('File_dir\Stu_Data.txt') as file_obj:
        contents=(file_obj.read()).split()
    print(contents)

    # 读文件
    # 注意转义字符
    # with语句打开文件
    with open('File_dir\Stu_Data.txt') as file_obj:
        contents=file_obj.read()
    print(contents)

    with open('File_dir\Stu_Data.txt') as file_obj:
        contents=file_obj.read().split()
    print(contents)

    '''在使用readlines()不可使用split()'''
    # with open('File_dir\Stu_Data.txt') as file_obj:
    #     contents=file_obj.readlines.split()
    # print(contents)



    file_path="File_dir\Stu_Data.txt"
    contents=''
    for line in open(file_path):
        # contents+=line.rstrip() # 去除每行后面的换行符号
        contents+=line.replace('\n',' ') # 把换行符改成' '
    print(contents)


    file_path=r'File_dir\file.txt'
    with open(file_path,'a') as fp:
        fp.write('\nThis is a test2\n')
        fp.write("This is a test3")
    fp.close

    sentence='write a sentence into a file'
    fp=open(file_path,'a')
    fp.writelines(sentence)
    fp.close


else:
    # 遍历文件夹总和案例
    while True:
        rootdir=input("请输入遍历目录的绝对路径:(q退出)")
        if rootdir=='q':
            break
        if not(os.path.exists(rootdir)):
            print("输入的路径不存在，请重新输入!!")
            continue
        for parent,dirnames,filenames in os.walk(rootdir):
            # 三个参数:分别返回
            # 1.父目录
            # 2.所有文件夹的名字(不含路径)
            # 3.所有文件的名字
            for dirname in dirnames:
                print("parent is:"+parent)
                print("dirname is:"+dirname)
            for filename in filenames:
                print("parent is:"+parent)
                print("filename is:"+filename)
                print("the full name of the file is:"+os.path.join(parent,filename))
                # 输出文件的路径信息
