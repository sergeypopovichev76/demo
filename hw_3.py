file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'

with open(file_name_1, 'r') as f1:
    row_count_file1 = len(f1.readlines())
with open(file_name_2, 'r') as f2:
    row_count_file2 = len(f2.readlines())
with open(file_name_3, 'r') as f3:
    row_count_file3 = len(f3.readlines())


def read_and_write(file_name_read, file_name_write, row_count_file):
    with open(file_name_read, 'r') as f1:
        file_name_write.write(f'{file_name_read}\n')
        file_name_write.write(f'{row_count_file}\n')
        for i in range(row_count_file):
            file_name_write.write(f'{f1.readline()}')
        file_name_write.write('\n')


with open('full_file.txt', 'w') as full_file:
    read_and_write(file_name_2, full_file, row_count_file2)
    read_and_write(file_name_1, full_file, row_count_file1)
    read_and_write(file_name_3, full_file, row_count_file3)
