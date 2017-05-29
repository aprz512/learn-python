# -*- coding: utf-8 -*-
cars = 100
print cars

print "Hello world!!!"
print 'Wish me lucky!!!'
# 只要是引号包起来的就是字符串，不管是双引号还是单引号

print "Hello %s!!!" % "world"
# 想要使用参数的形式来打印字符串 需要用到 % 操作符，% 左边的是要显示的字符串 右边的是参数列表，有多个参数可以使用 (xxx, xxx, xxx) 的形式，当然参数也可以使用变量， 如下：
w = "world"
print "Hello %s!!!" % w

print "Hello",
print "W" * 5

print "Hello", "W" * 5

print "Hello world"
print 'Hello world'
print "That's good!"	# 这里只能使用双引号

# 开始 py
print "That's", "good!"	# 用逗号分隔，输出会连接起来，中间有个空格
print "That's",
print "good!"			# 同上

print "That's %s" % "good!"		# %s 中间需要用 % 将参数隔开，有个参数使用 (args1, args2, ...)

print "That's good!\n" * 5		# 将字符串重复 5 次，输出

print "%s" % 5
print "%d" % 5 + 10
