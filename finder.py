from os import sys, path, listdir
import shutil

fileList = []

def search(root, target):
    # fileList = []
    items = listdir(root)
    # print(items)
    for item in items:
        filepath = path.join(root, item)
        if path.isdir(filepath):
            search(filepath,target)
        elif path.isfile(filepath):
            if filepath.split('.')[-1] == target:
                fileList.append(filepath)
                print('[+]',filepath)

    return fileList

def moveFileToDest(files,dest):
    for file in files:
        shutil.copy(file,dest)
        # shutil.copy2(file,dest)
    

def main(argv):
    path = argv[1]
    target = argv[2]
    dest = argv[3]
    files = search(path,target)
    moveFileToDest(files,dest)
    # print(files)

if __name__ == '__main__':
    main(sys.argv)

