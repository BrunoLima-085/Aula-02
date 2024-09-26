idade = int(input("\nDigite sua idade: "))
temhab = input("\nVocê possui habilitação? Sim ou Não: ").lower()
if idade >= 18 and temhab == "sim":
    print("\nVocê está apto para dirigir!")
else:
    print("\nVocê não está apto para dirigir!")