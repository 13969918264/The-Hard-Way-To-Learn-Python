# -*- coding: utf-8 -*-
# 给字符串变量x赋值字符串
x = "There are %d types of people." % 10
# 给字符串变量binary赋值字符串
binary = "binary"
# 给字符串变量do_not赋值字符串
do_not = "don't"
# 给字符串变量y赋值字符串
y = "There who know %s and those who %s."	% (binary, do_not)

# 打印字符串变量x中的值
print x
#打印字符串变量y中的值
print y

# 打印字符串且字符串中嵌套字符串变量x中的字符串
print "I said: %r." % x
# 打印字符串且字符串中嵌套字符串变量y中的字符串
print "I also said: '%s'." % y

# 给字符串变量hilarious赋值字符串
hilarious = False
# 给字符串变量joke_evaluation赋值字符串且其中嵌套字符串但未指明
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印字符串变量joke_evaluation并为其指明中间的字符串
print joke_evaluation % hilarious

# 为字符串变量w和e赋值字符串
w = "This is the left side of ..."
e = "a string with a right side."

# 打印出w和e中的字符串且用+字符连接两个字符串成为一个
print w + e
