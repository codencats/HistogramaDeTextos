import os
#from matplotlib.pylab import hist, show
def cleaning(words,c1,c2):
    i=0
    while i < len(c1):
        if c1[i]<11:
            c1.pop(i)
            words.pop(i)
            if c2 != NULL:
                c2.pop(i)
            i=i-1
        i=i+1

def save(contador):
    files = os.listdir(".")
    i=1
    filename = "out"+str(i)+".txt"
    while filename in files:
        i=i+1
        filename = "out"+str(i)+".txt"
    out = open(filename,"w")
    out.write(str(contador))
    out.close()

def lector(lista,archivo, palabras, contador):
    f = open(lista[archivo])
    ext = lista[archivo].split(".")
    if ext[1] != "txt":
        print "No se puede abrir el archivo..."
        f.close()
        exit()
    lines = f.readlines()
    for l in lines:
        words = l.split()
        for w in words:
            w=w.lower()
            if w in palabras:
                i = palabras.index(w)
                contador[i] = contador[i]+1
            else:
                palabras.append(str(w))
                contador.append(1)
    f.close()

palabras = []
c1 = []
c2 = []
sel = []

os.chdir("Textos")
list = os.listdir(".")
print("Select a max of 2 literatures...")
for i in range(len(list)):
    print(str(i)+".- "+list[i])
sel = input("Selection: ")
i=0
while i < len(sel):
    if sel[i] >= len(list):
        sel.pop(i)
        i=i-1
    else:
        if i==0:
            lector(list,sel[i],palabras,c1)
            save(c1)
        else:
            for i in range(len(c1)):
                c2.append(0)
            lector(list,sel[i],palabras,c2)
            save(c2)
    i=i+1





#Graficacion
#hist(contador,len(contador),max(contador))
#show()

#for i in range(len(palabras)):
#    print (palabras[i]+": "+str(contador[i]))
#print palabras[contador.index(max(contador))]+": "+str(max(contador))
