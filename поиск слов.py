spisok = []
spisok1 = []
for i in range(int(input())):
	spisok.append(input())
poisk = input().lower()
for k in range(len(spisok)):
	x = spisok[k]
	x1 = x.lower()
	if poisk in x1:
		spisok1.append(x)
print(spisok1)