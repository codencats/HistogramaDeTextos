import os
from matplotlib.pylab import hist, show

palabras = []
contador = []
os.chdir("Textos")
list = os.listdir(".")
print("Select a literature...")
for i in range(len(list)):
    print(str(i)+".- "+list[i])
print("Selection: ")
sel = -1
while sel == -1:
    sel = input()
    if sel > -1 and sel < len(list):
        break
    print("Not existing file...")
    sel = -1

f = open(list[sel])
ext = list[sel].split(".")
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
os.chdir("..")
out = open("out.txt","w")
out.write(str(contador))
out.close()
f.close()

#Graficación
hist(contador,len(contador),max(contador))
show()

#for i in range(len(palabras)):
#    print (palabras[i]+": "+str(contador[i]))
#print palabras[contador.index(max(contador))]+": "+str(max(contador))
