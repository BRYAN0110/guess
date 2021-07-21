import random


while True:
	start = input('請輸入初始值:')
	end = input('請輸入最大值:')
	start = int(start)
	end = int(end)

	if start > end:
		print('數值設定錯誤!')
	else:
		r = random.randint(start, end)
		i = 1
		while i > 0:
			number = input('請猜一個數字:')
			number = int(number)

			if number == r:
				print('這是你第', i, '次猜測，恭喜你答對了!!')
				break
			if r > number:
				print('這是你第', i, '次猜測，再大一點!')
			if r < number:
				print('這是你第', i, '次猜測，再小一點!')
			i = i + 1
		break
	