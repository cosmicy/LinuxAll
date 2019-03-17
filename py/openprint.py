file_name = 'fib.py'
def openpy(filename):
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())
