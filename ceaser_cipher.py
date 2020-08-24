def hasNum(word):
	for letter in word:
		if letter.isnumeric():
			return True

while True:
	txt = input('Enter Text : ').upper()
	if hasNum(txt):
		print('Error! Should have only letters\n')
	else:
		break

while True:
	try:
		key = int(input('Enter Key : '))
		if not 0<key<26:
			print('Error! Invalid Key\n')
			continue
		break
	except ValueError:
		print('Error! Should be a number\n')

cipher = ''
for ltr in txt:
	ascii = ((ord(ltr) + key) % 90)
	if ascii < 64:
		ascii += 64
	cipher += chr(ascii)

print(cipher)
