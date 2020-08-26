plain_text = input('Enter Text: ').upper()
PT_len = len(plain_text)

cipher_text = ''
up = []
down = []

for i in range(0, PT_len, 2):
	up.append(plain_text[i])
	try:
		down.append(plain_text[i + 1])
	except:
		pass

cipher_text = cipher_text.join(up + down)

print(cipher_text)
