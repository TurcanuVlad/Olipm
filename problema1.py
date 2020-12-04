x=int(input("dati numarul total de pasari: "))
h=x//2
f=h//4
k=x-h-f
if(h>0 and f >0 and k>0):
    print(f"Exista {h} gaini,{f} rate si {k} gaste")
else:
    print("Nr. mic de pasari domestice")