
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

def converter(telefones):
    return(int(telefone) for telefone in telefones)

def verifica_tipo(telefones):
    for num in telefones:
        if not isinstance(num, int):
            return("Erro na conversão")
    return ("Todos os números foram convertidos corretamente.")

telefones_convertidos=converter(telefones)
print(verifica_tipo(telefones_convertidos))
