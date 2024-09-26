preço = float(input("\nInsira o preço do seu produto: R$ "))
preço -= 5*preço/100

print(f"\nVocê ganhou desconto de 5% na sua compra, o valor ficou R${preço: .2f}")