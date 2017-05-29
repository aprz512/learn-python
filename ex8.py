formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    # 注意下面的字符串有个单引号 所以用 %r 输出会是双引号
    "But it didn't sing.",
    "So I said goodnight."
)
