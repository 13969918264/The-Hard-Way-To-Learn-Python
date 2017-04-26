# -*- coding: utf-8-*-

#使用变量便于修改，修改初始值即为修改全部


#	有100辆车
cars = 100
#	每辆车可以坐4.0个人
space_in_a_car = 4.0
# 	有30位驾驶员
drivers = 30
# 	有90位乘客
passengers = 90
#	无驾驶员的车有多少辆？
cars_not_driven = cars - drivers
#	有多少个驾驶员就可以驾驶多少辆车
cars_driven = drivers
#	可乘坐的位置有多少个（包括驾驶员）
carpool_capacity = cars_driven * space_in_a_car
#	平均每辆车坐几个人
average_passengers_per_car = passengers / cars_driven

#输出有多少车
print "there are", cars, "cars available."
#输出有多少司机
print "there are only", drivers, "drivers availanlle."
#输出多少车不能用
print "there will be", cars_not_driven, "empty cars today."
#输出今天能坐多少人
print "we can transport", carpool_capacity, "people today."
#输出我们有多少人
print "we have", passengers, "to carpool today."
#输出我们需要每辆车坐几个人
print "we need to put about", average_passengers_per_car, "in each car."


