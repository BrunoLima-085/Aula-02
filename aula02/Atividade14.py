preço = float(input("\nInsira o preço do seu produto: R$ "))
qtde = float(input("\nInsira a quantidade adquirida: "))

if qtde > 10:
    preço -= 10*preço/100
    print(f"\nVocê ganhou desconto de 10% na sua compra, o valor ficou R${preço*qtde: .2f}")
else:
    print("\nObrigado pela compra.")