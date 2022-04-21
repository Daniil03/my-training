words = []
for i in range(int(input())):
	s = input()
	if s not in words:
		words.append(s)
print(*words, sep='\n')