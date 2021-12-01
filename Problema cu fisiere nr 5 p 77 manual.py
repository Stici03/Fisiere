#Într-un fişier sunt înscrise caractere arbitrare. 
#Elaboraţi un program care afişează pe ecran numărul vocalelor din fişier.
y = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'ă', 'Ă', 'â', 'Â',  'Î', 'î']
w = 0 # nr de vocale

with open("Desktop\\info.txt", "w") as f:
	f.write(eval(input("introdu textul dorit:")))

with open("Desktop\\info.txt", "r") as f:
	x = f.read()

for i in range(0, len(x)):
	for j in range(0, len(y)):
		if x[i] == y[j]:
			w+=1

print("NR DE VOCALE DIN FISIER=", w)