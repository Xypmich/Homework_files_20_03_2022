import os

basepath = os.getcwd()
files_list = os.listdir()


def files_sort(basepath:str):
    files_dict = {}
    for file_name in files_list:
        if '.txt' in file_name and file_name != 'sorted_file.txt':
            file_path = os.path.join(basepath, file_name)
            with open(file_path, 'r', encoding='utf-8') as file_read:
                files_dict[file_name] = file_read.read().count('\n') + 1

        else:
            continue
    files_dict_sorted = sorted(files_dict, key=files_dict.get)
    for sort_file_name in files_dict_sorted:
        file_path = os.path.join(basepath, sort_file_name)
        with open(file_path, 'r', encoding='utf-8') as file_read, open('sorted_file.txt', 'a', encoding='utf-8') as file_write:
            file_write.write(file_read.read() + '\n')

files_sort(basepath)