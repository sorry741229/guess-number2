import random
r = random.randint(1, 100)
count = 0 #猜的次數
while True:
	count = count + 1 # count += 1 簡寫
	num = input('請猜數字: ')
	num = int(num)
	if num == r :
		print('恭喜你猜對了!')
		break
	else:
		if r > num :
			print('答錯了!，答案比你猜的大')
		else :
			print('答錯了!，答案比你猜的小')
	print('這是你猜的第', count, '次')