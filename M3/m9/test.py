

with open('foo.txt', 'r') as file_read:
    for line in file_read:  # NOTA: mejor que file_read.readlines():
        print(line, end='')
        