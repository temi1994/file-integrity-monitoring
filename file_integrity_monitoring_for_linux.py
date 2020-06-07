import hashlib
import time
import datetime
import ctypes
import os


#print(os.listdir('C:/Windows/System32'))
#for filename in os.listdir("C:\\"):
#    print(filename)

id = 1
print("Enter your file name with absolute directory:")
file_1 = input()
hasher = hashlib.md5()
with open(file_1, 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
    test_1 = hasher.hexdigest()
    content_1 = buf
#print(test_1)

while id > 0:

    time.sleep(10)

    #print("Sleep Working!")

    hasher = hashlib.md5()
    with open(file_1, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
        test_2 = hasher.hexdigest()
        now = datetime.datetime.now()
        content_2 = buf
    #print(test_2)


    if test_1 != test_2 :
        test_1 = test_2
        print("Alert!")
        with open("log.txt", "w") as text_file:
            text_file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            text_file.write("  ")
            text_file.write("Warning! File ")
            text_file.write(file_1)
            text_file.write(" is Modified!")
            text_file.write("\n")
            text_file.write("\t")
            text_file.write("Before Modified >> ")
            text_file.write(str(content_1))
            text_file.write("\n")
            text_file.write("\t")
            text_file.write("After Modified >>  ")
            text_file.write(str(content_2))
        

