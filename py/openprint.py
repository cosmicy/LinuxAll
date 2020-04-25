file_name = 'fib.py'
def openpy(filename):
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip()) #删除string字符串末尾的指定字符(默认为空格)
