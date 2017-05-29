# -*- coding: utf-8 -*-
from os.path import exists

print "This script can copy a file to another!"
source_file = raw_input("choose a file to copy : ")
target_file = raw_input("choose a file to save : ")

file_data = open(source_file).read()
print "%s length = %d" % (source_file, len(file_data))
print "%s exist? %r" % (target_file, exists(target_file))
open(target_file, "w").write(file_data)

# 没有使用变量保存文件，程序结束后，python会自动关闭文件，不用调用 close
