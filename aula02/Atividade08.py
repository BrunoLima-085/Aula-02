frase = input("\nDigite uma frase: ")
palavra = input("\nDigite qualquer palavra: ")
resultado = palavra.lower() in frase.lower()

print(resultado)