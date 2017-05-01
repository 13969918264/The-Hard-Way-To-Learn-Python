# -*- coding: utf-8 -*-
# 给变量formatter赋值字符串（且字符串内容为格式控制符）
formatter = "%r %r %r %r"
# 将formatter中的格式控制符带入打印字句
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# 且前一个变量formatter是格式控制符，后一个是输出参数（即被打印的字符串）
print formatter % (formatter,formatter, formatter, formatter)
print formatter % (
		"I had this thing,",
		"That you could type up right.",
		"But it didn't sing,",
		"So Isaid goodnight."
)
