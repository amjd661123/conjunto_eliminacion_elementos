def llenado(l):
    x = []
    for i in range(0,l):
        x.append(input(f"Elemento {i+1} de {l}: "))
    print(f"Lista final: {x}")
    return x

def eliminar(a,b):
    x = []
    for i in a:
        if i not in b:
            x.append(i)
    print(f"Lista resultado de eliminar los elementos de la segunda presentes en la primera lista: {x}")

a = llenado(int(input("Ingresa la lingitud de la lista a: ")))
b = llenado(int(input("Ingresa la lingitud de la lista b: ")))

eliminar(a,b)

