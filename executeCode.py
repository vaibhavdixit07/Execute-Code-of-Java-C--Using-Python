import os
import subprocess
import shutil
import time

named_tuple = time.localtime()
time_string = time.strftime("%d%m%Y%H%M", named_tuple)

path = os.getcwd()
file_path = path + '\\' + time_string

if os.path.isdir(file_path):
    print('Directory already exist!')
else:
    os.mkdir(time_string)


def executePythonFile():
    with open("output.txt", "wb") as f:
        subprocess.check_call(["python", "file.py"], stdout=f)


def executeCppFile():
    data, temp = os.pipe()
    os.write(temp, bytes("5", "utf-8"))
    os.close(temp)

    with open('outputCpp.txt', 'wb') as f:
        subprocess.check_output("g++ ReversePyramid.cpp -o ReversePyramid", shell=True)
        s = subprocess.check_output("ReversePyramid", stdin=data, shell=True)
        # print(s.decode("utf-8"))
        f.write(s)

    shutil.move(path + '\outputCpp.txt', file_path + '\outputCpp.txt')


def executeJavaFile():
    data, temp = os.pipe()
    os.write(temp, bytes("5", "utf-8"))
    os.close(temp)

    with open('outputJava.txt', 'wb') as f:
        subprocess.check_output("javac ReversePyramid.java", shell=True)
        s = subprocess.check_output("java ReversePyramid", stdin=data, shell=True)
        # print(s.decode("utf-8"))
        f.write(s)

    shutil.move(path + '\outputJava.txt', file_path + '\outputJava.txt')


if __name__ == "__main__":
    executeCppFile()
    executeJavaFile()
