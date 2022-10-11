def dinero(dO,vP,pC):
    dO=dO*11760
    vP=vP*56
    pC=dO+vP+pC
    return pC

while True:
    try:
        print("a continuacion ingrese en orden:")
        dO=int(input("ingrese los dragones de oro que posee :"))
        vP=int(input("ingrese los venados de plata que posee: "))
        pC=int(input("ingrese los peniques de cobre que posee: "))
        break
    except ValueError:
        print("los valores ingresados deben ser numericos y enteros")

totalEnPeniques=dinero(dO,vP,pC)

dO=totalEnPeniques//11760
resto=totalEnPeniques%11760
vP=resto//56
pC=resto%56
print("su dinero antes de la compra es",dO," dragones de oro ",vP,"venados de plata",pC,"peniques de cobre")
totalEnPeniques=dinero(dO,vP,pC)

comprar=input("si quiere comprar ingrese s/n: ")
if comprar=="s" :
    while True:
        try:
            costo=dinero(int(input("ingrese el costo en dragones de oro: ")),int(input("ingrese el costo en venados de plata: ")),int(input("ingrese el costo en peniques de cobre: ")))
            if totalEnPeniques >= costo:
                totalEnPeniques=totalEnPeniques-costo
                print("compra realizada")
                break
            else:
                print("no te alcanza")
                break
        except ValueError:
            print("los valores deben ser numericos")
            
dO=totalEnPeniques // 11760
resto=totalEnPeniques % 11760

vP=resto // 56
pC=resto % 56
print(dO," dragones de oro ",vP,"venados de plata",pC,"peniques de cobre")

