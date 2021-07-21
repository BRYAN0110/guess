import random
r = random.randint(1,100)
i = 1
while i > 0:
	figure = input('請猜一個數字:')
	print('第', i , '次猜測')
	if r == int(figure):
		print('答對了!!!')
		break
	elif r > int(figure):
		print('再大一點!')
	else :
		print('再小一點!')
	i = i + 1