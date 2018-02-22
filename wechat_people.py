# -*- coding: utf-8-*- 
import itchat
import os
import time
import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 
itchat.auto_login(hotReload = True) 
friends = itchat.get_friends(update = True)
male = female = other = 0
for i in friends:
	sex = i["Sex"]
	if sex == 1:
		male += 1
	elif sex == 2:
		female += 1
	else:
		other += 1
i =  "男性好友： %d"%(int(male))+"\n"+"女性好友: %d"%(int(female))+"\n"+"其他好友： %d"%(int(other))+"\n"
j = "总共好友数 ：%d"%total+"\n"
k = "男性好友比例：%.2f%%"%(float(male)/total*100)+"\n"+"女性好友比例： %.2f%%"%(float(female)/total*100)+"\n"+"其他好友比例： %.2f%%"%(float(other)/total*100)
s = i+j+k
print (s)