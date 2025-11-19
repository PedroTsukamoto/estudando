def e_par(valor):
    if valor % 2 == 0:
        print("É par")
        return True
    else:
        print("É impar")
        return False


valores=[]

while True:
    entrada=(input("Digite um valor ou sair: ")).strip()
    if entrada.lower() == "sair":
        break
    valores.append(int(entrada))


for valor in valores:
    e_par(valor)



