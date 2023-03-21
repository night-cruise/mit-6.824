import os
import tempfile
import shutil

# 指定要遍历的目录
dir_path = "D:\code\projects\mit-6.824\src"


def traverse_directory(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            # 处理文件
            if filename.startswith('README'):   
                with open(file_path, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    content = content.replace('{% hint style="info" %}', '')
                    content = content.replace('{% endhint %}', '')
                    f.seek(0)
                    f.truncate()
                    f.write(content)
            elif filename.startswith('SUMMARY'):
                temp_file_path = os.path.join(dir_path, 'SUMMARY-TEMP.md')
                temp_file = open(temp_file_path, 'w', encoding='utf-8')
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = ' '.join(map(lambda x: '[' if x.startswith('[') and x[1].isdigit() else x, line.split(' '))).replace('[ ', '[')
                        temp_file.write(line)
                temp_file.close()
                os.remove(file_path)
                os.rename(temp_file_path, file_path)
        elif os.path.isdir(file_path):
            # 处理子目录
            traverse_directory(file_path)  # 递归遍历子目录下的文件


if __name__ == "__main__":
    traverse_directory(dir_path)