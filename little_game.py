# -*- coding: utf-8 -*-
from sys import exit
prompt = "> "

global power
global monkey_status   # 1 不管 2 沾血 3 救活

power = 0
monkey_status = 0

def get_choice(start, end):
    while True:
        input_str = raw_input(prompt)
        if input_str.isdigit():
            input_num = int(input_str)
            if input_num in range(start, end + 1):
                return input_num
            else:
                print "输入1, 2, 3，好伐！！！"
        else:
            print "输入数字，好伐！！！"

def die(why):
    print why
    print "哈哈哈哈哈，你个垃圾！"
    print "你受到了未知的嘲讽！！！"
    exit(0)

def choose_power():
    print "你醒了，天空传来一道声音：请选择一项能力或物品！"
    print "1. 锋利的长剑"
    print "2. 火球术"
    print "3. 恢复术"
    print "智商250的你很快就接受了这项设定，于是你做出选择："

    global power
    power = get_choice(1, 3)
    if power == 1:
        print "你获取的锋利的长剑"
    elif power == 2:
        print "你学会了火球术"
    else:
        print "你学会了恢复术"

def hurted_monkey():
    print "沿着道路前行了一段路程，你遇到了一只受伤的猴子。看着那只对你龇牙咧嘴的猴子，你准备："
    print power
    print "1. 不理它"
    if power == 1:
        print "2. 杀了它"
    elif power == 2:
        print "2. 烤了它"
    else:
        print "2. 帮它治疗"

    choice = get_choice(1, 2)

    global monkey_status
    if choice == 1:
        print "你不屑的瞟了瞟猴子，大步走开了。"
        monkey_status = 1
    elif choice == 2 and power == 1:
        print "你偷袭了那只猴子，身上沾满了鲜血。"
        monkey_status = 2
    elif choice == 2 and power == 2:
        die("你对猴子施展了火球术，猴子临时前的惨叫声引来了其他的猴子，你被围攻而死！！！")
    else:
        print "你治好了猴子，猴子深情的望了望你，然后biu的一下就不见了。"
        monkey_status = 3

def river():
    print "继续往前，一条河挡在了前面，水性不错的你完全可以游过去，你准备："
    print "1. 直接游过去"
    print "2. 往河里丢砖头，看看有没有什么东西"

    choice = get_choice(1, 2)
    if choice == 1:
        if monkey_status == 2:
            die("你身上的血腥味吸引来了鲨鱼，你被吃了。")
        else:
            print "你安全的游过去了。"
    else:
        print "你引来了鲨鱼。"
        if power == 3:
            die("你没有办法杀死鲨鱼，你饿死了。")
        elif power == 2:
            print "你用火球术杀死了鲨鱼，安全的过河了。"
        else:
            print "你用剑杀死了鲨鱼，安全的过河了。"

def dark_forest():
    print "天黑了，你准备在森林里面休息一个晚上，显然这里并不安全。"
    if monkey_status == 3:
        print "正当你绞尽脑汁想找一个安全的地方休息的时候，那只你救过的猴子向你跑了过来，它想带你去一个地方。"
        print "你准备:"
        print "1. 跟它走"
        print "2. 不理它"

        choice = get_choice(1, 2)
        if choice == 1:
            print "你和猴子到了一个隐蔽的地方，安全的度过了一个晚上。"
        else:
            die("你随便找了一个地方休息，但是半夜里，有恐怖的动物袭击了你，你死了。")
    elif power == 3:
        die("你随便找了一个地方休息，但是半夜里，有恐怖的动物袭击了你，你死了。")
    else:
        if power == 1:
            print "你准备:"
            print "1. 用树枝加固自己休息的地方"
            print "2. 找个地方将就一下"
            choice = get_choice(1, 2)
            if choice == 1:
                print "你安全的度过了这个晚上。"
            else:
                die("你随便找了一个地方休息，但是半夜里，有恐怖的动物袭击了你，你死了。")
        else:
            print "你准备:"
            print "1. 在休息的地方点篝火"
            print "2. 找个地方将就一下"
            choice = get_choice(1, 2)
            if choice == 1:
                print "你安全的度过了这个晚上。"
            else:
                die("你随便找了一个地方休息，但是半夜里，有恐怖的动物袭击了你，你死了。")

def walk_out():
    print "you win！"
    exit(0)

def game_start():
    choose_power()
    hurted_monkey()
    river()
    dark_forest()
    walk_out()

game_start()
