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
    data, temp = os.pipe()
    os.write(temp, bytes("5", "utf-8"))
    os.close(temp)
    with open("outputPython.txt", "wb") as f:
        subprocess.check_call(["python", "ReversePyramid.py"], stdin=data, stdout=f)
        print("Python code execute successfully!")

    shutil.move(path + '\outputPython.txt', file_path + '\outputPython.txt')
    print("Python Output file created in " + time_string + " directory")
    print("*******************************************")


def executeCppFile():
    data, temp = os.pipe()
    os.write(temp, bytes("5", "utf-8"))
    os.close(temp)

    with open('outputCpp.txt', 'wb') as f:
        subprocess.check_output("g++ ReversePyramid.cpp -o ReversePyramid", shell=True)
        s = subprocess.check_output("ReversePyramid", stdin=data, shell=True)
        print("C++ code execute successfully!")
        # print(s.decode("utf-8"))
        f.write(s)

    shutil.move(path + '\outputCpp.txt', file_path + '\outputCpp.txt')
    print("C++ Output file created in " + time_string + " directory")
    print("*******************************************")


def executeJavaFile():
    data, temp = os.pipe()
    os.write(temp, bytes("5", "utf-8"))
    os.close(temp)

    with open('outputJava.txt', 'wb') as f:
        subprocess.check_output("javac ReversePyramid.java", shell=True)
        s = subprocess.check_output("java ReversePyramid", stdin=data, shell=True)
        print("Java code execute successfully!")
        # print(s.decode("utf-8"))
        f.write(s)

    shutil.move(path + '\outputJava.txt', file_path + '\outputJava.txt')
    print("Java Output file created in " + time_string + " directory")
    print("*******************************************")


if __name__ == "__main__":
    executePythonFile()
    executeCppFile()
    executeJavaFile()
