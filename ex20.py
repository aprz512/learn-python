# -*- coding: utf-8 -*-
from sys import argv

script, file_name = argv

def print_file_content (file):
    print file.read()

def seek_to_start(file):
    file.seek(0)

def print_one_line(file, line_number):
    print "%d: %r" % (line_number, file.readline())

target_file = open(file_name)

print "This is file content:"
print_file_content(target_file)

print "Seek to start ....."
seek_to_start(target_file)

line_number = 1
print_one_line(target_file, line_number)

line_number = line_number + 1
print_one_line(target_file, line_number)

line_number = line_number + 1
print_one_line(target_file, line_number)
