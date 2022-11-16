import os 
import shutil 
from_dir="/Users/venkatatammana/Desktop/102/f1"
to_dir="/Users/venkatatammana/Desktop/102/f2"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name) 
    print(extension)
if extension in ['.gif','.png','.jpg','.jpeg','jfif']:
    path1=from_dir+'/'+file_name
    path2=to_dir+'/'+'Image_Files'
    path3=to_dir+'/'+'Image_Files'+'/'+file_name
    print("path1",path1)
    print("path3",path3)
if os.path.exists(path2):
    print("moving"+file_name+".....")
    shutil.move(path1,path3)
else:
    os.makedirs(path2)
    print("moving"+file_name+".....")
    shutil.move(path1,path3)    