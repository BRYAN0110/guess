import random
r = random.randint(1,100)

while True:
	figure = input('請猜一個數字:')
	if r == int(figure):
		print('答對了!!!')
		break
	elif r > int(figure):
		print('再大一點!')
	else :
		print('再小一點!')