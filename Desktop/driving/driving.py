country = input('你是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照囉')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照囉')
	else:
		print('你還不能考駕照')	


else:
	print('請輸入"台灣" "美國"，而且字要一模一樣喔!!!')