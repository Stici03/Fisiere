with open("C:\\Users\\STICI\\Desktop\\Lista clasei 11C.txt", "r", encoding="utf-8") as f:
	qw = f.read()
franc=[]
engl=[]
n_franc=[] # notele copiilor ce studiaza franceza
n_engl=[] # notele copiilor ce studiaza engleza
for i in qw.split("\n"):
	camp=i.split()
	if str(camp[3]) == 'Engleza': 
		n_engl.append(int(camp[2]))
		engl.append(camp)
	elif str(camp[3]) == 'Franceza': 
		n_franc.append(int(camp[2]))
		franc.append(camp)

with open ("C:\\Users\\STICI\\Desktop\\Media grupei anglofone.txt", "w", encoding="utf-8") as f: 
	f.writelines("Nume Prenume Nota Limba Straina\n")
	for z in range(0, len(engl)):
		for q in range(0, len(engl[0])):
			f.write(str(engl[z][q])+" ")
		f.write("\n")
	f.writelines("\nMedia grupei engleze este "+ str(round(sum(n_engl)/len(n_engl), 3)))

with open ("C:\\Users\\STICI\\Desktop\\Media grupei francofone.txt", "w", encoding="utf-8") as f:
	f.write("Nume Prenume Nota Limba Straina\n")
	for w in range(0, len(franc)):
		for k in range(0, len(franc[0])):
			f.write(str(franc[w][k])+str(" "))
		f.write("\n")
	f.writelines("\nMedia grupei franceze este "+ str(round(sum(n_franc)/len(n_franc), 3))) 