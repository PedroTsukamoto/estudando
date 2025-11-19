
valores=[]

while True:
    entrada=input("Escreva o valor da compra ou sair: ").strip()
    if entrada.lower() == "sair":
        break
    valores.append(float(entrada.replace(",",".")))

total=sum(valores)

print(f"Valores digitados {valores}")
print(f"Soma total {total:.3f}")