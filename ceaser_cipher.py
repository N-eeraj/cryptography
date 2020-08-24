from termcolor import colored #module to change colors in terminal

def errorMsg(error): #to make the error message red
	print(colored(error, 'red'))

def isLetter(word): #to check if input has only letters & space
	for letter in word:
		input_ascii = ord(letter)
		if  input_ascii== 32:
			continue
		if not 64 < input_ascii  < 90:
			errorMsg(letter + ' is an Invalid input')
			return True

def inputMsg(msg): #to make input prompt white
	return (input(colored(msg, 'white')))

while True:
	txt = inputMsg('Enter Text : ').upper()
	if isLetter(txt):
		errorMsg('Error! Should have only letters\n')
	else:
		break

while True:
	try:
		key = int(inputMsg('Enter Key : '))
		if not 0 < key < 26:
			errorMsg('Error! Invalid Key\n')
			continue
		break
	except ValueError:
		errorMsg('Error! Should be a number\n')

cipher = ''

#changing plain text to cipher text
for ltr in txt:
	ascii = ord(ltr)
	if ascii == 32:
		cipher += ' '
		continue
	ascii = ((ascii + key) % 90) #ASCII value of 'Z' = 90
	if ascii < 64: #ASCII value of 'A' = 65
		ascii += 64
	cipher += chr(ascii)

print(cipher)
