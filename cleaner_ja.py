import os
# Made with love by ZiAzusa
print(f'ようこそChromiumのキャッシュの目録清掃員!')
input(f'「Enter」を押して始めてください...')
f = open('deleted_files.log', 'w')

for d in range(ord("A"), ord("Z") + 1):
    dir_path = chr(d) + f':\\'
    if not os.path.exists(dir_path):
        continue
    print(chr(d) + 'ディスク内の検索')
    for (this_dir, child_dir, child_file) in os.walk(dir_path):
        if f'C:\\Windows' in this_dir:
            continue
        print(f'フォルダ内:' + this_dir)
        if f'Code Cache' in this_dir:
            f.write(f'フォルダ内:' + this_dir + f'\n')
            print(f'Chromiumのキャッシュの目録を見つけた.')
            f.write(f'Chromiumのキャッシュの目録を見つけた.\n')
            if os.path.exists(this_dir + f'\\..\\Cache'):
                for (this_dir2, child_dir2, child_file2) in os.walk(this_dir + f'\\..\\Cache'):
                    for i in child_file2:
                        try:
                            os.remove(this_dir + f'\\..\\Cache\\' + i)
                            print(f'削除されたファイル:' + this_dir + f'\\..\\Cache\\' + i)
                            f.write(f'削除されたファイル:' + this_dir + f'\\..\\Cache\\' + i + f'\n')
                        except:
                            continue
            for i in child_file:
                try:
                    os.remove(this_dir + f'\\' + i)
                    print(f'削除されたファイル:' + this_dir + f'\\' + i)
                    f.write(f'削除されたファイル:' + this_dir + f'\\' + i + f'\n')
                except:
                    continue

f.close()
print(f'完了! ファイル削除ログ (deleted_files.log) はすでにスクリプトの同じディレクトリの下に生成されている.')
input(f'「Enter」を押して終了してください...')
exit()
