# 1 ULESANNE
#Ask_P=""
#while type(Ask_P)!=int:
#	try:
#		Ask_P=int(input("Сколько чисел вы хотите ввести?  "))
#	except ValueError:
#		print("Только целые числа!")
	
#if Ask_P>0:
#	Ask_N=int(input("Какое число вводим?  "))
#	Ask_P-=1
#	maks=Ask_N
#	while Ask_P>0:
#		Ask_N=int(input("Какое число вводим?  "))
#		Ask_P-=1
#		if Ask_N>maks: maks=Ask_N
#	print("Самое большее число", Ask_N)
#else:
#	print("Не можем найти макс.число!")
# 3 ULESANNE
#km=s_pikkus=10
#print("Esimesel päeval pikkus oli", km)
#for p in range(2,8):
#	km*=1.1
#	print(p,". päeval pikkus oli", km)
#	s_pikkus+=km
#	print(p,". päeval terve tee pikkus oli",round(s_pikkus,2))
# 4 ULESANNE 
#from random import *
#M=randint(100,1000)
#print("Poes on",M,"m")
#while M>0:
#	m=int(input("Mitu meetri tahad ostaAAAA??????"))
#	if M>=m:
#		M-=m
#		print("Meil on jäänud ",M,"m")
#	else:
#		print("MEIL EI OLE ROHKEM, KUI MEIL ON!!!")
#		v=input("Kas te tahete osta?")
#		if v=="jah":
#			print("Kang on teile oma")
#			M=0
#		else:
#			print("Ei taha; siis ei taha!")
#print("Pood on tühi!")

#from random import *
#from keyboard import *

#while True:
#	a=read_key()
#	if a=="esc": break 
#	print("HAllo?!")



#while True:
#	a=0.0
#	while type(a)!=int and a<=0:
#		try:
#			a=int(input("Введите число для значения a  "))
#		except ValueError:
#			print("Только числа!")
#	b=0.0
#	while type(b)!=int and b<=0:
#		try:
#			b=int(input("Введите число для значения b  "))
#		except ValueError:
#			print("Только числа!")
#	h=0.0
#	while type(h)!=int and h<=0:
#		try:
#			h=int(input("Введите число для значения h  "))
#		except ValueError:
#			print("Только числа!")
#	S=(a+b)*h/2
#	print("Площадь трапеции ",S)
#	q=input("Продолжаем?  ")
#	if q!="да": quit()



##Lottery
random import
a=randint(1,10)
b=int(input("Введите число  "))
if b==a:
	print("Победа!")
else:
	print("Попробуй ещё раз!")