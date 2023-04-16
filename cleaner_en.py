import os
# Made with love by ZiAzusa
print(f'Welcome to use Chromium Cache Dir Cleaner!')
input(f'Please press "Enter" to start...')
f = open('deleted_files.log', 'w')

for d in range(ord("A"), ord("Z") + 1):
    dir_path = chr(d) + f':\\'
    if not os.path.exists(dir_path):
        continue
    print(f'Finding in ' + chr(d) + 'disk.')
    for (this_dir, child_dir, child_file) in os.walk(dir_path):
        if f'C:\\Windows' in this_dir:
            continue
        print(f'Reading dir:' + this_dir)
        if f'Code Cache' in this_dir:
            f.write(f'Reading dir:' + this_dir + f'\n')
            print(f'Finded Chromium Cache Dir.')
            f.write(f'Finded Chromium Cache Dir.\n')
            if os.path.exists(this_dir + f'\\..\\Cache'):
                for (this_dir2, child_dir2, child_file2) in os.walk(this_dir + f'\\..\\Cache'):
                    for i in child_file2:
                        try:
                            os.remove(this_dir + f'\\..\\Cache\\' + i)
                            print(f'Deleted file:' + this_dir + f'\\..\\Cache\\' + i)
                            f.write(f'Deleted file:' + this_dir + f'\\..\\Cache\\' + i + f'\n')
                        except:
                            continue
            for i in child_file:
                try:
                    os.remove(this_dir + f'\\' + i)
                    print(f'Deleted file:' + this_dir + f'\\' + i)
                    f.write(f'Deleted file:' + this_dir + f'\\' + i + f'\n')
                except:
                    continue

f.close()
print(f'Success!')
input(f'Please press "Enter" to exit...')
exit()
