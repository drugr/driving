country = input('你是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣' or '臺灣' or 'Taiwan':
	if age >= 18:
		print('你可以考駕照囉')
	else:
		print('你還不能考駕照')