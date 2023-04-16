import os
# Made with love by ZiAzusa
print(f'欢迎使用Chromium缓存目录清理工具!')
input(f'请按回车键（Enter）以开始清理...')
f = open('deleted_files.log', 'w')

for d in range(ord("A"), ord("Z") + 1):
    dir_path = chr(d) + f':\\'
    if not os.path.exists(dir_path):
        continue
    print(f'正在查找：' + chr(d) + '盘')
    for (this_dir, child_dir, child_file) in os.walk(dir_path):
        if f'C:\\Windows' in this_dir:
            continue
        print(f'正在检索目录：' + this_dir)
        if f'Code Cache' in this_dir:
            f.write(f'正在检索目录：' + this_dir + f'\n')
            print(f'提示：找到Chromium缓存目录！')
            f.write(f'提示：找到Chromium缓存目录！\n')
            if os.path.exists(this_dir + f'\\..\\Cache'):
                for (this_dir2, child_dir2, child_file2) in os.walk(this_dir + f'\\..\\Cache'):
                    for i in child_file2:
                        try:
                            os.remove(this_dir + f'\\..\\Cache\\' + i)
                            print(f'删除文件：' + this_dir + f'\\..\\Cache\\' + i)
                            f.write(f'删除文件：' + this_dir + f'\\..\\Cache\\' + i + f'\n')
                        except:
                            continue
            for i in child_file:
                try:
                    os.remove(this_dir + f'\\' + i)
                    print(f'删除文件：' + this_dir + f'\\' + i)
                    f.write(f'删除文件：' + this_dir + f'\\' + i + f'\n')
                except:
                    continue

f.close()
print(f'清理工作已完成！已在脚本同目录下生成文件删除日志（deleted_files.log）')
input(f'请按回车键（Enter）以退出脚本...')
exit()
