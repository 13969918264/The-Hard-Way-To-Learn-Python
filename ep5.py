# -*- coding: utf-8 -*-
name = 'zhao zihao'
age = 21	# not a lie
height = 182	#	cm
weight = 90	#	kg
eyes = 'black'
teeth = 'write'
hair = 'black'

print "Let's talk about %s." % age
print "He's %d cm tall." % height
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depedng on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight)
